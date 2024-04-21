import reflex as rx
import random
import time

# Define a list of words to display
names = ["dan", "dandy", "andy", "pan"]
num_players = len(names)
powers = ["fire", "water", "earth", "air", "reflexes", "instincts", "intelligence"]

indices = list(range(len(powers)))
random.shuffle(indices)
sh_powers = [powers[i] for i in indices]
pow = sh_powers[:num_players]




# Create a label widget for displaying the words
# label = rx.Text("", width=200, height=50, font_size=20)
# app.add(label)

# Function to update the label with the next word
def update_word():
    while True:
        for word in words:
            label.text = word
            # Redraw the app to update the display
            app.update()
            # Pause for a short duration before displaying the next word
            time.sleep(1)

# Start the word carousel in a separate thread
# rx.thread(update_word)


# Run the Reflex app
def index():
    text = []

    for i in range(num_players):
        text.append(names[i] + ": " + pow[i])
        
    # Create the vertical stack
    vstack = rx.vstack(
        rx.foreach(
            text,
            lambda word, index: rx.box(
                rx.text(word),
                bg=text,
                border_radius="1em",
                box_shadow="rgba(88, 204, 100, 0.5) 0 15px 30px -10px",
                background_color="#58CC64",
                box_sizing="content-box",
                color="white",
                opacity=1,
                size="4",
            )
        ),
        columns=str(num_players),
    )
    
    # Create a container to center the vstack
    container = rx.box(vstack, align="center", justify="center", height="100vh")

    return container
