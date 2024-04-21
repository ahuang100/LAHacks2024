"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
from LAHacks2024.pages import landing
from LAHacks2024.pages import naming
from LAHacks2024.pages import abilities
from LAHacks2024.pages import room
from LAHacks2024.pages import convinceme
from LAHacks2024.pages import yousaid
from LAHacks2024.pages import transition

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""



app = rx.App(stylesheets=[
    "https://fonts.googleapis.com/css2?family=IM+Fell+DW+Pica+SC&display=swap",
    ],
)

app.add_page(landing.index)
#subpage
app.add_page(naming.naming_page, route="/naming")
app.add_page(abilities.index, route="/abilities")
app.add_page(convinceme.convincemepage, route="/convinceme")
app.add_page(yousaid.yousaid_page, route="/yousaid")
app.add_page(transition.index, route="/transition")
app.add_page(naming.naming_page, route="/naming")
app.add_page(room.room_page)
