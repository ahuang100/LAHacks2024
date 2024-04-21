from rxconfig import config

import reflex as rx
#what we need from states: 
#state.hostname, state.roomcode, state.player2, state.player3,... state#ofrounds



def room_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.chakra.text("Hostname",  fontFamily="IM FELL DW Pica SC", padding="25px 25px 25px 25px", font_size="32px", color="#FFFFFF", width="100%", height="67px", max_width="100%", text_align="center"),
            rx.chakra.text("Room Code:", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center"),
            
            rx.hstack(
            rx.chakra.text("Host Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),width="100%", justify="between", padding_x="40px"), 
            rx.hstack(
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),width="100%", justify="between", padding_x="40px")
            , 
            rx.hstack(
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text("Player Name", fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),width="100%", justify="between", padding_x="40px")
            , 

            
            height="100vh",
            width="100%",
            align_items="center"
        ),
        width="100%",
        background="linear-gradient(180deg, #a45637 0%, #3e2115 100%)",
    )


