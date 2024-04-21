from rxconfig import config
from LAHacks2024.states import roomStates 

import reflex as rx
#what we need from states: 
#state.hostname, state.roomcode, state.player2, state.player3,... state#ofrounds


@rx.page(route="/room-page/[room_id]", on_load=roomStates.RoomState.get_data)
def room_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.chakra.text(roomStates.RoomState.player_names[0] + '\'s Room',  fontFamily="IM FELL DW Pica SC", padding="25px 25px 25px 25px", font_size="32px", color="#FFFFFF", width="100%", height="67px", max_width="100%", text_align="center"),
            rx.chakra.text("Room Code: " + roomStates.RoomState.room_key, fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center"),
            
            rx.hstack(
            rx.chakra.text(roomStates.RoomState.player_names[0], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text(roomStates.RoomState.player_names[1], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text(roomStates.RoomState.player_names[2], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text(roomStates.RoomState.player_names[3], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),width="100%", justify="between", padding_x="40px"), 
            rx.hstack(
            rx.chakra.text(roomStates.RoomState.player_names[4], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text(roomStates.RoomState.player_names[5], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text(roomStates.RoomState.player_names[6], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text(roomStates.RoomState.player_names[7], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),width="100%", justify="between", padding_x="40px")
            , 
            rx.hstack(
            rx.chakra.text(roomStates.RoomState.player_names[8], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text(roomStates.RoomState.player_names[9], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text(roomStates.RoomState.player_names[10], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),
            rx.chakra.text(roomStates.RoomState.player_names[11], fontFamily="Kadwa", font_size="24px", color="#FFFFFF", padding="25px 25px 25px 25px", text_align="center", width="200px"),width="100%", justify="between", padding_x="40px")
            , 

                       rx.cond(
                roomStates.RoomState.host_bool, 
                rx.vstack(
                    #rx.chakra.text("Number of Rounds:" + roomStates.RoomState.num_rounds.to_string(), fontFamily="IM FELL DW Pica SC", ), 

                    rx.chakra.text("Number of Rounds: " + roomStates.RoomState.num_rounds.to_string(), fontFamily="IM FELL DW Pica SC", ), 
                    rx.slider(default_value=1, step=5, on_value_commit=roomStates.RoomState.set_end,),
                    rx.button("Start", on_click=roomStates.RoomState.start_game),
                    width="30%",
                ),
            ),

            height="100vh",
            width="100%",
            align_items="center"
        ),
        width="100%",
        background="linear-gradient(180deg, #a45637 0%, #3e2115 100%)",
    )


