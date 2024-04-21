from rxconfig import config

import reflex as rx


#string named winner is given to me, now just display 

#winner name is given to me


def final_page() -> rx.Component:
    return rx.center(
       rx.heading("The AI believes " + winner + "held the most convincing argument." , fontFamily="Kadwa", color="#FFFFFF")
    )