from Socket import sendMessage

def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024).decode()
        #temp = string.split(readbuffer, "\n")
        temp = readbuffer.split("\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)

    sendMessage(s, "If anyone's curious, I'm working on an alternate OwlBalls system, with blackjack and hookers.")


def loadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True