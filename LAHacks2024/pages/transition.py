import reflex as rx
import asyncio

class TransitionState(rx.State):
    async def get_data(self):
        print("got in get_data")
        yield TransitionState.wait_5_sec()

    @rx.background
    async def wait_5_sec(self):
        for i in range(5):
            async with self:
                await asyncio.sleep(1)
                yield
        print("should redirect now")
        yield rx.redirect('/convinceme') # deal with dynamic routing later
        return

@rx.page(route="/transition",on_load=TransitionState.get_data)
def transition_page():
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
    