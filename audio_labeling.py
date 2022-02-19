from playsound import playsound
import os
import json

def audio_labeling(folder_path):
    out_file = open("audio_labeling.json", "w")
    data = dict()
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            playsound(filename)
            user_input = input("Enter 'n' for noise or 'c' for clean ")
            if filename not in data.keys():
                data[filename] = "noise" if user_input == 'n' else "clean"
    json.dump(data, out_file, indent=6)
    out_file.close()
    return out_file