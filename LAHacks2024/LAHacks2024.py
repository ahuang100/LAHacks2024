"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
from LAHacks2024.pages import landing
from LAHacks2024.pages import naming
<<<<<<< HEAD
from LAHacks2024.pages import abilities
=======
from LAHacks2024.pages import room
>>>>>>> b8d748391324515115b1c1bd8ef2989567b47332
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
<<<<<<< HEAD
app.add_page(naming.index, route="/naming")
app.add_page(abilities.index, route="/abilities")

=======
app.add_page(naming.naming_page, route="/naming")
app.add_page(room.room_page)
>>>>>>> b8d748391324515115b1c1bd8ef2989567b47332
