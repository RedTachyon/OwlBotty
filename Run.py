import json
from time import time
from urllib.request import urlopen

from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Logic import processMessage
from Settings import CHANNEL
from Loyalty import processLoyalty, getUsers



def main():
    s = openSocket()
    joinRoom(s)
    readbuffer = ''

    last_time = time.time()
    #users = json.loads(urllib.request.urlopen(url).read())

    while True:
        readbuffer = readbuffer + s.recv(1024).decode()
        temp = readbuffer.split("\n")
        readbuffer = temp.pop()
        current_time = time.time()
        if current_time - last_time > 300:
            users = getUsers()
            processLoyalty(users)
            last_time = current_time
        for line in temp:
            print(line)
            if line.startswith("PING"):
                # s.send(line.replace("PING", "PONG"))
                s.send("PONG tmi.twitch.tv\r\n".encode())
            else:
                user = getUser(line)
                message = getMessage(line)
                print(user + " typed: " + message)
                response = processMessage(message, user=user)
                if response:
                    print('Sending a message')
                    sendMessage(s, response)
                    print('Sent message')

if __name__ == '__main__':
    main()
