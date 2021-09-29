import random
# File contains functions that will be called to run the game

# Function to randomly deal two cards to whoever, and appends it to a list
def dealTwoCards(array, deck):
    '''
    Parameters: List, List[List]
    Returns: None, Affects given List[List] in parameter
    '''
    # Randomly choose a card from the deck
    # Append the element to the list
    # Remove the card from the deck
    card = random.choice(range(len(deck)))
    array.append(deck[card])
    deck.pop(card)
    card2 = random.choice(range(len(deck)))
    array.append(deck[card2])
    deck.pop(card2)

# Function to randomly deal one card to whoever, and appends it to a list
def dealOneCard(array, deck):
    '''
    Parameters: List, List[List]
    Returns: None, Affects given List[List] in parameter
    '''
    # Randomly choose a card from the deck
    card = random.choice(range(len(deck)))
    # Append the element to the list
    array.append(deck[card])
    # Remove the card from the deck
    deck.pop(card)

# Function to check the face of the card
def faceOfCard(card):
    if card[0] == 1:
        return "Ace"
    elif card[0] == 11:
        return "Jack"
    elif card[0] == 12:
        return "Queen"
    elif card[0] == 13:
        return "King"
    else:
        return card[0]

# Function to check the suit of the card
def suitOfCard(card):
    if card[1] == 1:
        return "Spades"
    elif card[1] == 2:
        return "Hearts"
    elif card[1] == 3:
        return "Diamonds"
    elif card[1] == 4:
        return "Clubs"

# Function to turn the list of numbers into the name of cards
def nameOfCards(listOfCards):
    '''
    Parameters: List
    Returns: Array of Strings
    '''
    # Create an empty list to store the names of the cards, we can't
    # modify the original list, because we need to keep the original to keep
    # track of all the cards we've pulled
    listOfNames = []

    # Loop through our hand
    for card in listOfCards:
        # variable to store the suit of the card
        suit = suitOfCard(card)
        # variable to store the face of the card
        face = faceOfCard(card)
        # appending the full name of the variable to the list we made earlier
        listOfNames.append(str(face) + " of " + suit)
    return listOfNames

# Function to calculate the total value of the hand we have
def handValue(listofCards):
    '''
    Parameter: list of cards
    Return: the value of the hand
    '''
    # Using a 0 to start the value of the hand at 0, since we have to recalculate 
    # the entire list each time we add a card. But that's okay, since we have to 
    # check if the value of the hand is over 21 anyway
    value = 0
    # Loop through the list of cards
    for card in listofCards:
        # Checking if the numbers are 2-10, if they are we can add there value to the hand
        if card[0] >= 2 and card[0] <= 10:
            value += card[0]
        # Any value that is over 11 is worth 10, is >= 11 will be a face card
        elif card[0] >= 11:
            value += 10
        # Running and checking if the it's an Ace. If it is, we need to check if the value of the hand is over 21.
        elif card[0] == 1:
            if value + 11 > 21:
                value += 1
            else:
                value += 11
    return value

