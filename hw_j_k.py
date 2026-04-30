import json
import pickle

b_and_s = {}
def add_band():
    band = str(input("Enter name of band: "))
    b_and_s[band] = []

def add_song():
    song = str(input("Enter name of song: "))
    band = str(input("Enter name of band: "))
    if band in b_and_s:
        b_and_s[band].append(song)
        return
    print("No band found, add a band first")

def save_data(data: dict[str, list[str]]):
    with open("b_and_s.json", "w") as f:
        json.dump(data, f)

def save_data_pickle(data: dict[str, list[str]]):
    with open("b_and_s.pickle", "wb") as f:
        pickle.dump(data, f)

def load_data_json():
    global b_and_s
    with open("b_and_s.json", "r") as f:
        b_and_s = json.load(f)

def load_data_pickle():
    global b_and_s
    with open("b_and_s.pickle", "rb") as f:
        b_and_s = pickle.load(f)


