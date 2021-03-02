from urllib import request
import json


class Joke(object):
    def __init__(self, setup, punchline, url, json_data):
        self.setup = setup
        self.punchline = punchline
        self.url = url
        self.json_data = json_data


def request_joke():
    Joke.url = "https://official-joke-api.appspot.com/random_joke"
    r = request.urlopen(Joke.url)

    data = r.read()
    Joke.json_data = json.loads(data)

    Joke.setup = Joke.json_data["setup"]
    Joke.punchline = Joke.json_data["punchline"]


def display_joke():

    while True:

        ask = str(input(f"\nWould you like to hear a joke? ")).lower()

        if "yes" in ask:
            request_joke()
            print(Joke.setup, Joke.punchline)
            continue

        elif "no" in ask:
            print("Maybe another time!")
            break

        else:
            print("Invalid response! Yes or No.")
            continue


display_joke()
