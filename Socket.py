import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    passw = "PASS " + PASS + "\r\n"
    s.send(passw.encode())
    nick = "NICK " + IDENT + "\r\n"
    s.send(nick.encode())
    channel = "JOIN #" + CHANNEL + "\r\n"
    s.send(channel.encode())
    return s

def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
    s.send(messageTemp.encode())
    print("Sent: " + messageTemp)