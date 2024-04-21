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
    text: list[str]

    async def get_data(self):
        print("enter")
        room_state = await self.get_state(roomStates.RoomState)
        self.host_bool = room_state.host_bool
        self.room_key = room_state.room_key
        self.user_id = room_state.user_id
        self.num_rounds = room_state.num_rounds
        server = DBServer.DBServer()
        self.player_names = server.get_players(self.room_key)
        self.num_players = len(self.player_names)


        # Set player abilities
        powers = ["Flight","Super strength","Invisibility","Telekinesis (moving objects with the mind)","Telepathy (reading minds)","Mind control","Time manipulation","Energy manipulation","Super speed","Shapeshifting","Elasticity (stretching body parts)","Healing factor","X-ray vision","Pyrokinesis (ability to control fire)","Cryokinesis (ability to control ice)","Hydrokinesis (ability to control water)","Technopathy (ability to control and communicate with technology)","Magnetism manipulation","Enhanced senses (sight"," hearing"," smell"," etc.)","Precognition (seeing the future)","Teleportation","Intangibility (ability to phase through solid objects)","Animal communication","Elemental manipulation (control over earth"," air"," fire"," water)","Force field generation","Time travel","Super agility","Super durability","Size manipulation (shrinking or growing in size)","Astral projection","Probability manipulation","Sonic scream","Photographic memory","Duplication (creating copies of oneself)","Gravity manipulation","Dream manipulation","Molecular manipulation","Reality warping","Adaptation (quickly adapting to any environment or situation)","Electrokinesis (control over electricity)","Plant manipulation","Energy absorption","Force blasts","Cloning (creating duplicates of oneself)","Power negation (canceling out other powers)","Flight without wings (levitation)","Time freeze","Weather manipulation","Hypnosis","Luck manipulation"]
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
        for i in range(2):
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
@rx.page(route="/abilities", on_load=AbilitiesState.get_data)
def abilities_page() -> rx.Component:
    
    # Create a container to center the vstack
    container = rx.text("sat")

    return container
