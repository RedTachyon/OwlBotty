import csv
import json
from urllib.request import urlopen
from Settings import CHANNEL


def getData(file):
    with open(file, 'r') as f:
        datareader = csv.reader(f)
        data = {row[0]: row[1] for row in datareader}


    return data


def changePoints(data, user, change=None, total=None):
    if change:
        data[user] += change
    elif total:
        data[user] = total
    return data


def writeData(file, data: dict):
    with open(file, 'w') as f:
        writer = csv.DictWriter(f, data.keys())
        writer.writerow(data)



def processLoyalty(users):
    pass

def getUsers():
    url = "https://tmi.twitch.tv/group/user/" + CHANNEL + "/chatters"
    data = json.loads(urlopen(url).read().decode())
    users = data['chatters']['moderators'] + data['chatters']['viewers']
    return users
