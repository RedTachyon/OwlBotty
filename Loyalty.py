import csv
import json
from urllib.request import urlopen
from Settings import CHANNEL


def getData(file):
    data = []
    with open(file, 'r') as f:
        datareader = csv.reader(f)
        for row in datareader:
            data.append(row)
    return list(data)

def processLoyalty(users):
    pass

def getUsers():
    url = "https://tmi.twitch.tv/group/user/" + CHANNEL + "/chatters"
    data = json.loads(urlopen(url).read().decode())
    users = data['chatters']['moderators'] + data['chatters']['viewers']
    return users
