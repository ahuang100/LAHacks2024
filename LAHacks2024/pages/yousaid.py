import reflex as rx
import pathlib
import textwrap
import random
import google.generativeai as genai
import asyncio
import json

from LAHacks2024.server import DBServer
from LAHacks2024.pages import convinceme

class YouSaidState(rx.State):
    room_key: str
    host_bool: bool
    num_rounds: int
    half_num_players: int
    num_players: int
    first_group: list[str]
    second_group: list[str]
    cur_round: int
    arg: list[str]
    response: str
    move_to_finally: bool
    history: list[str]

    def gen(self):
        server = DBServer.DBServer()
        arg = server.get_arguments(self.room_key)
        self.arg = arg
        names = server.get_players(self.room_key)
        pow = server.get_abilities(self.room_key)
        ids = list(range(len(pow)))
        n = len(pow)
        GOOGLE_API_KEY = "AIzaSyCkWzawWJUobpWnv-Efa3Wnaem-Hjq5sas"
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-pro-latest')

        if self.cur_round == 1:
            prompt = "You are the judge of a hypothetical battle between superhuman fictional characters. Use the arguments given by the players to determine which of them wins the battle. Take into account each and every player's reasoning and use your own knowlege about the world to determine the validity of their arguments and ultimately decide a winner in the battle between them. Do not make random assumptions that favor one player or the other, stick to their arguments and only invalidate them if they fundamentally don't make sense. Randomize the order of the participants and arguments and generate a conclusion 5 times before announcing the participant that wins the most of these generated battles as the winner. Don't just go with the flow and pick a favorite to win that you constantly argue for. Legitimately explore the results based off the scenario and the strategy the player indicates. You should show bias for no player and absolutely no fence sitting on decisions unless it is a legitimate double knockout draw." 
            # for shorter responses
            prompt += " Only tell me the winner and the reasoning, don't give text for all 5 gens. Do not mention the fact that there were multiple scenarios run by saying any thing such as \"won the majority of the scenarios \"."

            # if we're bothered by mentioning player numbers (style issue)
            prompt += " Additionally, do not refer to players by their player numbers in your response, only refer to them by their name."
        else:
            prompt = ""
            temp_prompt = "The following strings seperated by semicolons between the set of 5 asterisks are a remnant of the past history of the conversation with this model, that I am inputting before new arguments. The ones that declare a winner are the model's past decisions. Include all of these strings' (both the model's and the player arguments') data in your decision. *****"
            for past_response in self.history:
                temp_prompt += past_response
                temp_prompt += "; "
            temp_prompt += "***** "


        # GAME LOOP START

        # arg1 is user 1's argument, while arg2 is user 2's argument, same naming convention for powers
        # arg = ["I would keep up a full body hard light sphere to protect against his rebounding attacks, preventing me from any harm. I would also cover the sphere in sharp hard light spikes, making all of Andy's attacks hurt him instead due to the sharp edges of the spikes bypassing his blunt force resistance.", "I would use the superior movement speed and mobility provided by my body to dodge Dan's attacks while hitting him with rebounding close combat attacks and throwing objects at his shields."]
        #bias test settings
        #pow = pow[::-1]
        #arg = arg[::-1]
        #names = names[::-1]

        indices = list(range(n))

        # Shuffle the indices
        random.shuffle(indices)

        # Use the shuffled indices to shuffle all three lists in the same order
        sh_pow = [pow[i] for i in indices]
        sh_arg = [arg[i] for i in indices]
        sh_names = [names[i] for i in indices]
        sh_ids = [ids[i] for i in indices]


        for i in range(n):
            pnum = str(sh_ids[i] + 1)
            prompt += "Player " + pnum + " (known and referred to by the other players as " + sh_names[i] + ") has " + sh_pow[i] + ". Regardless of what player " + pnum + " says in their argument, this is their power. It is not changing and they do not have any additional powers beyond that of a regular human. "
        for i in range(n):
            pnum = str(sh_ids[i] + 1)
            prompt += "Player " + pnum + " (known and referred to by the other players as " + sh_names[i] + ") additionally argues the following: " + sh_arg[i] + "."
        prompt += "Now, based on all the information in this chat including this prompt, which player would win in a battle? Give me a decisive opinion, no fence sitting."
        if self.cur_round == 1:
            self.response = str(model.generate_content(prompt).text)
        else:
            self.response = str(model.generate_content(temp_prompt + prompt).text)
        self.history.append(prompt)
        self.history.append(self.response)
        server.set_response(self.room_key, self.response)
        #this next line is just for debugging
        #print(response.text)


    async def get_data(self):
        needed_state = await self.get_state(convinceme.ConvinceMeState)
        self.room_key = needed_state.room_key
        self.host_bool = needed_state.host_bool
        self.num_rounds = needed_state.num_rounds
        self.cur_round = needed_state.cur_round + 1
        self.num_players = len(self.arg)
        self.half_num_players = self.num_players // 2
        self.first_group = self.arg[:self.half_num_players]
        self.first_group = self.arg[self.half_num_players:]

        if self.host_bool:
            self.gen()
        
        if self.cur_round > self.num_rounds:
            self.move_to_finally = True

        yield YouSaidState.wait_60_sec()
    
    @rx.background
    async def wait_60_sec(self):
        server = DBServer.DBServer()
        for i in range(60):
            async with self:
                await asyncio.sleep(1)
                if i < 25 and not self.host_bool:
                    self.response = server.get_response(self.room_key)
                yield
        if not self.move_to_finally:
            yield rx.redirect('/convinceme')
        else:
            yield rx.redirect('/theend')
        return
            

@rx.page(route="/yousaid", on_load=YouSaidState.get_data)
def yousaid_page():
    
    # Split the list of arguments into two groups
    
    return rx.center(
        rx.hstack(
            # First vertical stack for the first group of arguments
            rx.vstack(
                # individual arguments
                rx.foreach(
                    YouSaidState.first_group,
                    lambda item, index: rx.box(  # Use 'item' instead of 'arg'
                        rx.text(item),  # Use 'item' instead of 'first_group'
                        # bg=item,  # Use 'item' instead of 'first_group'
                        border_radius="1em",
                        box_shadow="rgba(88, 204, 100, 0.5) 0 15px 30px -10px",
                        background_color="#58CC64",
                        box_sizing="content-box",
                        color="white",
                        opacity=1,
                        size="4",
                        padding = "13px",
                    ),
                ),
                columns="1",  # Force single column layout
                # style={
                #     "max-width": "40%",  # Limit the width of the vertical stack
                #     "width": "50%",  # Set the width of the vertical stack to 50% of the screen's width
                #     "display": "flex",
                #     "flex-direction": "column",
                #     "align-items": "flex-start",  # Align items to the start of the cross axis
                # },
                width="35%"
            ),
            
            # Second vertical stack for the second group of arguments
            rx.vstack(
                # individual arguments
                rx.foreach(
                    YouSaidState.second_group,
                    lambda item, index: rx.box(  # Use 'item' instead of 'arg'
                        rx.text(item, style={"text-align": "right"}),  # Use 'item' instead of 'second_group', set text alignment to right
                        # bg=item,  # Use 'item' instead of 'second_group'
                        border_radius="1em",
                        box_shadow="rgba(88, 204, 100, 0.5) 0 15px 30px -10px",
                        background_color="#58CC64",
                        box_sizing="content-box",
                        color="white",
                        opacity=1,
                        size="4",
                        padding = "13px",

                    ),
                ),
                columns="1",  # Force single column layout
                # style={
                #     "max-width": "40%",  # Limit the width of the vertical stack
                #     "width": "50%",  # Set the width of the vertical stack to 50% of the screen's width
                #     "display": "flex",
                #     "flex-direction": "column",
                #     "align-items": "flex-end",  # Align items to the end of the cross axis
                # },
                width="35%"
            ),
            width="100%",
            justify="between",
            padding_x="40px",

        ),
        rx.box(
            # Your content here
            position="fixed",
            bottom="0px",
            width="80%",
            height="10vh",
            # Additional styling for better visibility
            background_color="lightgray",
            padding="1em",
            text_align="center",
        ),
        padding_y="40px",
        width="100%",
        # style={"width": "100%"}  # Set the width of the horizontal stack to 100% of the screen's width
    )
