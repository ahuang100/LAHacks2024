import reflex as rx
from LAHacks2024.server import DBServer


class LandingState(rx.State):
    is_admin: bool = False
    room_key: str = ""
    
    def create_room(self):
        server = DBServer.DBServer()
        self.room_key = server.create_room()
        print("Created room with room key %s" % (self.room_key))
    
    def join_room(self, room_key: dict):
        room_key = room_key['room_key']
        print("Trying to join with room key %s" % (room_key))
        server = DBServer.DBServer()
        self.room_key = room_key
        try:
            server.join_room(self.room_key)
            print("Joined room with room key %s" % (self.room_key))
        except Exception as e: 
            print(e)

def index():
    return rx.center(
        #main middle content
        rx.flex(
            rx.heading("Power Parley", align="center", font_size="6em", padding="2px", color_scheme="gold"),
            rx.divider(orientation="horizontal", size="4"),
            rx.button(
                "Create Room",
                on_click=LandingState.create_room,
                border_radius="1em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(144deg,#FDFD96,#673AB7 50%,#800020)",
                box_sizing="content-box",
                color="white",
                opacity=1,
                _hover={
                    "opacity": 0.9,
                },
            ),
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="room_key",
                        placeholder="Enter Code", 
                        max_length="8", 
                        required=True,
                        radius="full", 
                        style={"width": "92px"}
                    ),
                    rx.button(
                        "Join", 
                        type="submit",
                        color_scheme="blue", 
                        radius="full",
                        background_image="linear-gradient(144deg,#FDFD96,#673AB7 50%,#800020)",
                    ),
                ),
                on_submit=LandingState.join_room,
            ),
            direction="column",
            align="center",
            justify="center",
            style={"margin-bottom": "20%"},
            spacing="8",
            
            height="100vh",  # This ensures the flex container fills the viewport height
        ),

        
        # 'how to play' bottom box
        rx.box(
            rx.center(
                rx.chakra.popover(
                    rx.chakra.popover_trigger(
                        rx.chakra.button("How to Play")
                    ),
                    rx.chakra.popover_content(
                        rx.chakra.popover_header("Game Rules"),
                        rx.list.ordered(
                            rx.list.item("Join a game"),
                            rx.list.item("Select an ability"),
                            rx.list.item(""),
                        ),
                        
                        rx.chakra.popover_close_button(),
                    ),
                ),
                # rx.link("How to Play...", href="/guide"),
                underline="auto",
                position="fixed",
                bottom="0",
                left="0",
                right="0",
                padding="20px",
                background_color="lightgray",
            )
        ),
        width="100%",
        height="100vh",
        # background_color= "#90EE90",
        # background="linear-gradient(45deg, var(--tomato-9), var(--plum-9))",

        # background_image="linear-gradient(144deg,#FDFD96,#673AB7 50%,#800020)",

        background="radial-gradient(circle at 22% 11%, rgba(62, 180, 137, .40), hsla(0, 0%, 0%, 0) 19%), radial-gradient(circle at 82% 25%, rgba(33, 150, 243, .36), hsla(0, 0%, 0%, 0) 35%), radial-gradient(circle at 25% 61%, rgba(250, 128, 114, .56), hsla(0, 0%, 0%, 0) 55%)",
        ext_align="center",
    ),
    



