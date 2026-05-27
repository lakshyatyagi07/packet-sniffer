import json

LOG_FILE = "logs/packets.json"

def save_to_json(packet_data):

    with open(LOG_FILE, "a") as file:

        json.dump(packet_data, file)
        file.write("\n")