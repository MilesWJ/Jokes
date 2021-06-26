import PySimpleGUI as sg
import json
import random
from urllib import request


# Makes a request to the official joke API.
def request_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    r = request.urlopen(url)

    data = r.read()
    json_data = json.loads(data)

    information = [json_data["setup"], json_data["punchline"]]

    joke = f"{information[0]} {information[1]}"

    return joke


# Returns a random window configured color.
def generate_color():
    colors = ["DarkBlue5", "DarkBlue6", "DarkBlue7"]
    return random.choice(colors)

# Returns a random "greeting" message.


def generate_message():
    messages = ["Would you like to here a joke?", "I have a funny joke to tell you.",
                "Listen to this joke!", "Let me tell you this funny joke.", "I have the funniest joke to tell you."]
    return random.choice(messages)


# Creates Joke Machine window.
sg.theme(generate_color())
layout = [
    [sg.Text(generate_message(), justification='center', size=(100, 1))],
    [sg.Button("Tell Me A Joke", size=(50, 1))]
]
window = sg.Window("The Joke Machine", layout, size=(290, 75))


# Opens and runs the Joke Machine.
def run_joke_machine():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Tell Me A Joke":
            sg.Popup(request_joke(), title="Joke")
    window.close()


run_joke_machine()
