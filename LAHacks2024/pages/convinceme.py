import reflex as rx
import asyncio
from datetime import datetime
from LAHacks2024.pages import abilities
from LAHacks2024.server import DBServer

class ConvinceMeState(rx.State):
    names: list[str]
    room_key: str
    host_bool: bool
    deadline: int
    submitted: bool
    user_id: str
    num_rounds: int
    cur_round: int

    async def get_data(self):
        self.names = abilities.AbilitiesState.names
        self.room_key = abilities.AbilitiesState.room_key
        self.host_bool = abilities.AbilitiesState.host_bool
        self.user_id = abilities.AbilitiesState.user_id
        self.num_rounds = abilities.AbilitiesState.num_rounds
        self.cur_round = abilities.AbilitiesState.cur_round
        
        # Synchronization
        current_time = datetime.now().time()
        submit_deadline = current_time.hour * 3600 + current_time.minute * 60 + current_time.second + 30
        server = DBServer.DBServer()
        if self.host_bool:
            self.deadline = submit_deadline
            server.host_send_time(self.room_key, submit_deadline)
        else:
            self.deadline = server.get_host_send_time(self.room_key)
        yield ConvinceMeState.deadline()
        
    @rx.background
    async def deadline_counter(self):
        while True:
            async with self:
                await asyncio.sleep(1)
                yield
                current_time = datetime.now().time()
                current_time_sec = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
                # If game started, end it and go to game screen 
                if current_time_sec > self.deadline:
                    yield rx.redirect('/yousaid') # deal with dynamic routing later
                    return
    
    def submit_answer(self, answer: dict):
        answer = answer['answer']
        server = DBServer.DBServer()
        server.send_argument(self.room_key, self.user_id, answer)
        self.submitted = True

rx.page(on_load=ConvinceMeState.get_data)
def convincemepage():
    return rx.script('document.body.style.overflow = "hidden";'), rx.center(
        rx.box(
            rx.chakra.text("Convince Me", fontFamily="IM Fell DW Pica SC", lineHeight="1.3",
                fontWeight="regular",
                fontSize="80px",
                # color="#FFFFFF",
                
            ),
            
            
            
            direction="column",
            align="center",
            justify="center",
            style={"margin-bottom": "10%"},
            spacing="8",
            
            height="100vh",  # This ensures the flex container fills the viewport height
        ),

        # chat box
        rx.box(
            rx.chakra.popover(
                rx.chakra.popover_trigger(
                    rx.chakra.button("How to Play")
                ),
                rx.chakra.popover_content(
                    rx.chakra.popover_header("Game Rules"),
                    rx.list.ordered(
                        rx.list.item("Join a game."),
                        rx.list.item("Select an ability."),
                        rx.list.item("Prove you'd win."),
                    ),
                    rx.chakra.popover_close_button(),
                ),
            ),
            style={"position": "fixed", "bottom": "20px", "right": "20px"},
            background_color="#CC9E58"
        ),
        
        # text field at the bottom
        rx.form.root(
            rx.chakra.input(
                placeholder="Enter your text here...",
                style={
                    "position": "fixed",
                    "bottom": "10px",
                    "left": "50%",  # Aligning to the middle horizontally
                    "width": "65%",  # 60% width of the viewport
                    "transform": "translateX(-50%)",  # Centering the text field horizontally
                    "color": "#FFFFFF"  # Making the text white
                },
            ),
            rx.button(
                "Submit",
                disabled=ConvinceMeState.submitted
            ),
            on_submit=ConvinceMeState.submit_answer,
        ),


        # background
        background="center/cover url('/blurryRobot.png')",
        width="100%",
        height="100%",
        ext_align="center",
        style={
            "background-position": "bottom",  # Position the background image at the bottom
        }
    )
