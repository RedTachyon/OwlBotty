import random


JOKES = [
    "What's the difference between a good joke and a bad joke timing",
    "I couldn't figure out why the baseball kept getting larger. Then it hit me.",
    "Communism jokes aren't funny unless everyone gets them.",
    "I used to be addicted to soap, but now I'm clean.",
    "What's the difference between a hippo and a zippo? One is really heavy, and the other is a little lighter.",
    "What did the pirate say when he turned 80 years old? Aye matey!",
    "This is my step ladder. I never knew my real ladder.",
]

OWLJOKES = [
    "Why did the Owl invite her friends over? She didn’t want to be owl by herself.",
    "What do you call an owl with an attitude? A scowl!"
]


def owlBotCommand(message, user=''):
    pass

def processMessage(message, user=''):
    response = ''
    messageTemp = message.strip()
    spam = False

    if messageTemp == "!gg":
        response = "G to the Jizzles!"

    elif messageTemp == "!owlbot joke":
        response = random.choice(JOKES)

    elif messageTemp == "!owlbot owljoke":
        response = random.choice(OWLJOKES)

    elif messageTemp == "!owlbot azax":
        response = "Ban yourself Azax."

    elif messageTemp == "!owlbot is dumb":
        response = "You're dumb, you asshat! BibleThump"

    elif messageTemp.startswith("!owlbot say:") and user == "burashi_kuteru":
        response = messageTemp.split(':', 2)[1]

    elif messageTemp == "!owlbot":
        response = "Hello, friends! So wonderful to see you again! Type !owlbot to get more spam. " \
                   "I have a problem with talking too much too quickly, so you may need to wait a moment."

    return response