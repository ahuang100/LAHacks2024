import reflex as rx
from LAHacks2024.server import DBServer
from LAHacks2024.pages import landing

class NamingState(rx.State):
    name: str = ""
    room_key: str = ""
    is_host: bool = False

    @rx.var
    def room_id(self) -> str:
        return self.router.page.params.get("room_id", "no room_id")
    
    async def get_data(self):
        landing_state = await self.get_state(landing.LandingState)
        self.room_key = landing_state.room_key
        print("Room key (get_data): " + self.room_key)
        self.is_host = landing_state.is_host

        # If going directly here instead of from landing, initialize vars
        # if self.room_key == '':
        #     if self.room_key != '': 
        #         self.room_key = self.room_id
        #     else:
        #         return rx.redirect('/')

    async def submit_name(self, name: dict):
        name = name['name']
        print("Trying to use name %s" % (name))
        self.name = name
        try: 
            print("Room key: " + self.room_key)
            server = DBServer.DBServer()
            server.check_username(self.room_key, self.name)
            print("Joined room %s using name %s" % (self.room_key, self.name))
            return rx.redirect('/room-page/%s' % (self.room_key))
        except Exception as e:
            print(e)

@rx.page(route="/naming/[room_id]", on_load=NamingState.get_data)
def naming_page():
    return rx.center(
        #main middle content
        rx.flex(
            rx.chakra.text("Please Enter Player Name", fontFamily="IM Fell DW Pica SC", lineHeight="1.3",
                fontWeight="regular",
                fontSize="80px",
                # color="#FFFFFF",
                
            ),
            rx.divider(orientation="horizontal", size="4"),

            rx.form.root(
                rx.input(
                    name="name",
                    placeholder="Enter Name", 
                    max_length="20", 
                    required=True,
                    radius="full", 
                    style={"width": "92px", "height": "48px"}
                ),
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
                on_submit=NamingState.submit_name,
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
    