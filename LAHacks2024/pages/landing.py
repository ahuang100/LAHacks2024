import reflex as rx


class State1(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

# @rx.page(route="/landing")

def index():
    return rx.center(
        #main middle content
        rx.flex(
            rx.heading("Game", align="center", font_size="6em", padding="2px", color="grass"),
            rx.divider(orientation="horizontal", size="4"),
            rx.button(
                "Create Room",
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
            rx.hstack(
                rx.button(
                    "Join", color_scheme="blue", radius="full",
                    background_image="linear-gradient(144deg,#FDFD96,#673AB7 50%,#800020)",

                ),
                rx.input(placeholder="Enter Code...", max_length="20", radius="full"),
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
                rx.link("How to Play...", href="/guide"),
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
        background_image="linear-gradient(144deg,#FDFD96,#673AB7 50%,#800020)",

        # background="radial-gradient(circle at 22% 11%, rgba(62, 180, 137, .40), hsla(0, 0%, 100%, 0) 19%), radial-gradient(circle at 82% 25%, rgba(33, 150, 243, .36), hsla(0, 0%, 100%, 0) 35%), radial-gradient(circle at 25% 61%, rgba(250, 128, 114, .56), hsla(0, 0%, 100%, 0) 55%)",
        ext_align="center",
    ),
    



