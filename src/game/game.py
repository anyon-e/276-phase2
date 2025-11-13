import json

import daily
from nicegui import Event, ui

# NiceGUI elements go here

# display the game (guess input, guess feedback, timer, # of guesses, etc.)
"""
game

    - guess entry box
    - guess button
    - guess feedback

    - win/loss popup
"""

# TODO: Replace with data type containing actual guess feedback
guess_graded = Event[str]()
game_ended = Event[bool]()


def try_guess(guess_input, feedback):
    if guess_input.validate():
        daily.handle_guess(guess_input.value)
        guess_input.clear()


@game_ended.subscribe
def display_results(won: bool):
    pass


@ui.page("/")
def index():
    options = []
    with open("src/game/countries.json") as file:
        options = json.load(file)

    with ui.column(align_items="center").classes("mx-auto w-full max-w-md p-4"):
        columns = [
            {"name": "name", "label": "Name"},
            {"name": "population", "label": "Population"},
            {"name": "size", "label": "Size"},
            {"name": "region", "label": "Region"},
            {"name": "languages", "label": "Languages"},
            {"name": "currencies", "label": "Currencies"},
            {"name": "timezones", "label": "Timezones"},
        ]
        rows = []
        feedback = ui.table(rows=rows, columns=columns, row_key="name")

        with ui.card(align_items="center"):
            guess_input = ui.input(
                label="Guess",
                placeholder="Enter a country",
                autocomplete=options,
                validation={"Not a valid country!": lambda value: value.lower() in options},
            ).without_auto_validation()
            ui.button("Submit", on_click=lambda: try_guess(guess_input, feedback))


# button to display leaderboards
"""
leaderboard

    - by default, display ~250 entries around the user
    - allow switch to friends-only or global leaderboard
    - allow jumping to top-ranked players
"""

# button to open account management menu
"""
account management

    - create account
    - see account stats
    - edit account info (username/password/email)
    - friends/friend requests
"""

ui.run(title="CMPT276 Project", dark=None)
