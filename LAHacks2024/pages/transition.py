import reflex as rx


# Run the Reflex app
def index():
    return rx.center(
        rx.chakra.text("So you think you'd win, huh?", 
            fontFamily="IM Fell DW Pica SC", lineHeight="1.3",
            fontWeight="regular",
            fontSize="95px",
            color="#E6E6C0",
                        
        ),        
        background_color="black",
        width="100%",
        height="100vh",
    )
    