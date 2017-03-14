from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Logic import processMessage

s = openSocket()
joinRoom(s)
readbuffer = ''

while True:
    persist = True
    readbuffer = readbuffer + s.recv(1024).decode()
    temp = readbuffer.split("\n")
    readbuffer = temp.pop()
    for line in temp:
        print(line)
        if line.startswith("PING"):
            #s.send(line.replace("PING", "PONG"))
            s.send("PONG :tmi.twitch.tv\r\n".encode())
        else:
            user = getUser(line)
            message = getMessage(line)
            print(user + " typed: " + message)
            response = ''
            i = 0
            response = processMessage(message, user=user)
            if response:
                print('Sending a message')
                sendMessage(s, response)
                print('Sent message')