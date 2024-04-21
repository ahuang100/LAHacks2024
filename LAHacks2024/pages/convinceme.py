import reflex as rx

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
        rx.chakra.input(
    placeholder="Enter your text here...",
    style={
        "position": "fixed",
        "bottom": "10px",
        "left": "50%",  # Aligning to the middle horizontally
        "width": "65%",  # 60% width of the viewport
        "transform": "translateX(-50%)",  # Centering the text field horizontally
        "color": "#FFFFFF"  # Making the text white
    }
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
