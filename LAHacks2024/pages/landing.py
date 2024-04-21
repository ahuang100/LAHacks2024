import reflex as rx
from LAHacks2024.server import DBServer



# @rx.page(route="/landing")
class LandingState(rx.State):
    is_host: bool = False
    room_key: str = ""

    def create_room(self):
        server = DBServer.DBServer()
        self.room_key = server.create_room()
        self.is_host = True
        print("Created room with room key %s" % (self.room_key))
        self.join_room({'room_key': self.room_key})
        return rx.redirect('/naming/%s' % (self.room_key))
    
    def join_room(self, room_key: dict):
        room_key = room_key['room_key']
        print("Trying to join with room key %s" % (room_key))
        self.room_key = room_key
        self.is_host = False
        try:
            server = DBServer.DBServer()
            server.join_room(self.room_key)
            print("Joined room with room key %s" % (self.room_key))
            return rx.redirect('/naming/%s' % (self.room_key))
            
        except Exception as e: 
            print(e)


def index():
    return rx.box(
    rx.center(
        #main middle content
        rx.flex(
            rx.chakra.text("Power Parley", fontFamily="IM Fell DW Pica SC", lineHeight="1.3",
                fontWeight="regular",
                fontSize="80px",
                # color="#FFFFFF",
                
            ),
            rx.divider(orientation="horizontal", size="4"),
            rx.button(
                "Create Room",
                on_click=LandingState.create_room,
                border_radius="1em",
                box_shadow="rgba(88, 204, 100, 0.5) 0 15px 30px -10px",
                # box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_color="#58CC64",
                box_sizing="content-box",
                color="white",
                opacity=1,
                size="4",

                _hover={
                    "opacity": 0.9,
                },
            ),
            # rx.hstack(
            #     rx.button(
            #         "Join", 
            #         border_radius="1em",
            #         box_shadow="rgba(88, 204, 100, 0.5) 0 15px 30px -10px",

            #         background_color="#58CC64",
            #         radius="full",
            #         color="white",
            #         opacity=1,
            #         # background_image="linear-gradient(144deg,#FDFD96,#673AB7 50%,#800020)",
            #         size="4",
            #         _hover={
            #             "opacity": 0.9,
            #         }
            #     ),
            #     rx.input(placeholder=" Enter Code", max_length="20", radius="full", style={"width": "92px", "height": "48px"}),
            # ),
            rx.form.root(
                rx.hstack(
                    rx.button(
                        "Join", 
                        border_radius="1em",
                        box_shadow="rgba(88, 204, 100, 0.5) 0 15px 30px -10px",
                        background_color="#58CC64",
                        radius="full",
                        color="white",
                        opacity=1,
                        type="submit",
                        style={"width": "60px", "height": "48px"},
                    ),
                    rx.input(
                        name="room_key",
                        placeholder="Enter Code", 
                        max_length="8", 
                        required=True,
                        radius="full", 
                        style={"width": "92px", "height": "48px"},
                    ),
                    
                ),
                on_submit=LandingState.join_room,
            ),
            direction="column",
            align="center",
            justify="center",
            style={"margin-bottom": "20%", "z_index": "1"},
            spacing="8",
            
            
            height="100vh",  # This ensures the flex container fills the viewport height
        ),

        
        # 'how to play' bottom box
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
            # rx.center(
            #     rx.chakra.popover(
            #         rx.chakra.popover_trigger(
            #             rx.chakra.button("How to Play")
            #         ),
            #         rx.chakra.popover_content(
            #             rx.chakra.popover_header("Game Rules"),
            #             rx.list.ordered(
            #                 rx.list.item("Join a game"),
            #                 rx.list.item("Select an ability"),
            #             ),
                        
            #             rx.chakra.popover_close_button(),
            #         ),
            #     ),
            #     # rx.link("How to Play...", href="/guide"),
            #     underline="auto",
            #     position="fixed",
            #     bottom="0",
            #     left="0",
            #     right="0",
            #     padding="20px",
            #     background_color="lightgray",
            # )
            # background_color="#CC9E58",
            style={"position": "fixed", "bottom": "20px", "right": "20px"},
            background_color= "#CC9E58"
        ),
        # rx.video(
        #     url="/ezgif-3-6b6435d05b-000jpg-frame-interpolation-vmake_GzA2HIhj-vmake.mp4",
        #     width="100%",
        #     height="auto",
        #     controls=False,

        #     loop=True,
        #     playing=True,
        #     muted=True
        #     width = 
        # ),
        # rx.html("""
        #     <video autoplay muted loop id="myVideo" style="position: fixed; right: 0; bottom: 0; ">
        #     <source src="/ezgif-3-6b6435d05b-000jpg-frame-interpolation-vmake_GzA2HIhj-vmake.mp4" type="video/mp4">
        #     Your browser does not support HTML5 video.
        #     </video>
        #     """
        # ),
        
        width="100%",
        height="100vh",
        # background_color= "#90EE90",
        # background="linear-gradient(45deg, var(--tomato-9), var(--plum-9))",

        # background_image="linear-gradient(144deg,#FDFD96,#673AB7 50%,#800020)",
        
        # background-image= "linear-gradient(45deg, #ff0000, #00ff00)";
        # animation= "animateGradient 5s linear infinite";
        # background="radial-gradient(circle at 22% 11%, rgba(62, 180, 137, .40), hsla(0, 0%, 0%, 0) 19%), radial-gradient(circle at 82% 25%, rgba(33, 150, 243, .36), hsla(0, 0%, 0%, 0) 35%), radial-gradient(circle at 25% 61%, rgba(250, 128, 114, .56), hsla(0, 0%, 0%, 0) 55%)",
        # rx.video(url=""),
        
        style={
                    "z_index": "-10",
                },
        background="linear-gradient(180deg, #a45637 0%, #3e2115 100%)",

        ext_align="center",
    ),
    
    
        rx.box(
            
            rx.image(
                src="/courtroom.png",
                style={
                    "position": "fixed",
                    "left": "3vw",
                    "bottom": "23vh",
                    "width": "500px",  # Adjust image size as needed
                    "height": "auto",
                    "z_index": "0",
                }
            ),
            
            direction="column",
            align="center",
            justify="center",
            style={
                "width": "100%",
                "height": "100vh",
                "position": "relative", 
            },
        ),
        #lawyer gif
        rx.box(
            rx.image(
                src="/lawyer.gif",
                style={
                    "position": "fixed",
                    "left": "55vw",
                    "bottom": "38vh",
                    "width": "700px",  # Adjust image size as needed
                    "height": "auto",
                    "z_index": "0",
                }
            ),
            direction="column",
            align="center",
            justify="center",
            style={
                "width": "100%",
                "height": "100vh",
                "position": "relative"
            }
        ),
    )
    
    



