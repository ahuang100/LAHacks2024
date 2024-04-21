import reflex as rx
import random
import time
import asyncio
from LAHacks2024.server import DBServer
from LAHacks2024.states import roomStates

# Define a list of words to display
class AbilitiesState(rx.State):
    player_names: list[str]
    num_players: int
    room_key: str = ""
    user_id: str = ""
    host_bool: bool = False
    num_rounds: int
    cur_round: int
    text = list[str]

    async def get_data(self):
        room_state = await self.get_state(roomStates.RoomState)
        self.host_bool = room_state.host_bool
        self.room_key = room_state.room_key
        self.user_id = room_state.user_id
        self.num_rounds = room_state.num_rounds
        server = DBServer.DBServer()
        self.player_names = server.get_players(self.room_key)
        self.num_players = len(self.player_names)

        # Set player abilities
        powers = ["fire", "water", "earth", "air", "reflexes", "instincts", "intelligence"]
        indices = list(range(len(powers)))
        random.shuffle(indices)
        sh_powers = [powers[i] for i in indices]
        pow = sh_powers[:self.num_players]
        
        for i in range(self.num_players):
            self.text.append(self.player_names[i] + ": " + pow[i])

        server.set_abilities(self.room_key, pow)
        yield AbilitiesState.wait_10_sec()
    
    @rx.background
    async def wait_10_sec(self):
        for i in range(10):
            async with self:
                await asyncio.sleep(1)
                yield
        yield rx.redirect('/transition') # deal with dynamic routing later
        return

    # Create a label widget for displaying the words
    # label = rx.Text("", width=200, height=50, font_size=20)
    # app.add(label)

    # Function to update the label with the next word
    # def update_word(self):
    #     while True:
    #         for word in self.words:
    #             label.text = word
    #             # Redraw the app to update the display
    #             app.update()
    #             # Pause for a short duration before displaying the next word
    #             time.sleep(1)

# Start the word carousel in a separate thread
# rx.thread(update_word)

# Run the Reflex app
rx.page(on_load=AbilitiesState.get_data)
def abilities_page():
    # Create the vertical stack
    vstack = rx.vstack(
        rx.foreach(
            AbilitiesState.text,
            lambda word, index: rx.box(
                rx.text(word),
                bg=AbilitiesState.text,
                border_radius="1em",
                box_shadow="rgba(88, 204, 100, 0.5) 0 15px 30px -10px",
                background_color="#58CC64",
                box_sizing="content-box",
                color="white",
                opacity=1,
                size="4",
            )
        ),
        columns=str(AbilitiesState.num_players),
    )
    
    # Create a container to center the vstack
    container = rx.box(vstack, align="center", justify="center", height="100vh")

    return container
