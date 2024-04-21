import reflex as rx

arg = ["You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing.", "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare.", "I would keep up a full body hard light sphere to protect against his rebounding attacks, preventing me from any harm. I would also cover the sphere in sharp hard light spikes, making all of Andy's attacks hurt him instead due to the sharp edges of the spikes bypassing his blunt force resistance.", "I would use the superior movement speed and mobility provided by my body to dodge Dan's attacks while hitting him with rebounding close combat attacks and throwing objects at his shields."]
names = ["dan", "dandy", "andy", "pan"]

def yousaid_page():
    num_players = len(arg)
    half_num_players = num_players // 2  # Calculate the halfway point
    
    # Split the list of arguments into two groups
    first_group = arg[:half_num_players]
    second_group = arg[half_num_players:]
    
    return rx.center(
        rx.hstack(
            # First vertical stack for the first group of arguments
            rx.vstack(
                # individual arguments
                rx.foreach(
                    first_group,
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
                    second_group,
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
