import random
# File contains functions that will be called to run the game

def chooseCard(myCards):
    card = random.choice(myCards)
    return card

def faceOfCard(card):
    if card[0] == 1:
        return "Ace"
    elif card[0] == 2:
        return 2
    elif card[0] == 3:
        return 3
    elif card[0] == 4:
        return 4
    elif card[0] == 5:
        return 5
    elif card[0] == 6:
        return 6
    elif card[0] == 7:
        return 7
    elif card[0] == 8:
        return 8
    elif card[0] == 9:
        return 9
    elif card[0] == 10:
        return 10
    elif card[0] == 11:
        return "Jack"
    elif card[0] == 12:
        return "Queen"
    elif card[0] == 13:
        return "King"

def suitOfCard(card):
    if card[1] == 1:
        return "Spades"
    elif card[1] == 2:
        return "Hearts"
    elif card[1] == 3:
        return "Diamonds"
    elif card[1] == 4:
        return "Clubs"
