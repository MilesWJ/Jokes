from urllib import request
import json


class Joke(object):
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline


def get_joke():
    while True:

        ask = str(input("\nWould you like to hear a joke? ")).lower()

        if "yes" in ask:

            url = "https://official-joke-api.appspot.com/random_joke"
            r = request.urlopen(url)

            data = r.read()
            json_data = json.loads(data)

            Joke.setup = json_data["setup"]
            Joke.punchline = json_data["punchline"]

            print(Joke.setup, Joke.punchline)
            continue

        elif "no" in ask:
            print("Maybe another time!")
            break

        else:
            print("Invalid response! Yes or No.")
            continue


get_joke()