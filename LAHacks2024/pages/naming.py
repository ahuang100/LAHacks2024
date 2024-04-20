import reflex as rx

def index():
    return rx.center(
        #main middle content
        rx.flex(
            rx.chakra.text("Please Enter Player Name", fontFamily="IM Fell DW Pica SC", lineHeight="1.3",
                fontWeight="regular",
                fontSize="80px",
                # color="#FFFFFF",
                
            ),
            rx.divider(orientation="horizontal", size="4"),
            rx.input(placeholder=" Enter Name", max_length="20", radius="full", style={"width": "92px", "height": "48px"}),

            rx.button(
                "Ready",
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
            
            direction="column",
            align="center",
            justify="center",
            style={"margin-bottom": "20%"},
            spacing="8",
            
            height="100vh",  # This ensures the flex container fills the viewport height
        ),

        
        
        
        width="100%",
        height="100vh",
        
        
        
        background="linear-gradient(180deg, #a45637 0%, #3e2115 100%)",

        ext_align="center",
    )
    