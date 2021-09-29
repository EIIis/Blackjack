import time
import random
from cards import *

# Set of all cards represented in a matrix format with a list a list
# Each card is represented by the two numbers in each element, the card representation is [rank, suit]
# The first number is the rank, so 1 = Ace, 2 = 2, 3 = 3, 4 = 4, 5 = 5, 6 = 6, 7 = 7, 8 = 8, 9 = 9, 10 = 10, 11 = Jack, 12 = Queen, 13 = King
# The second number is the suit, so 1 = Spades, 2 = Hearts, 3 = Diamonds, 4 = Clubs
# So the card representation is [rank, suit]
myCards = [[1, 1], [1, 2], [1, 3], [1, 4],
[2, 1], [2, 2], [2, 3], [2, 4],
[3, 1], [3, 2], [3, 3], [3, 4],
[4, 1], [4, 2], [4, 3], [4, 4],
[5, 1], [5, 2], [5, 3], [5, 4],
[6, 1], [6, 2], [6, 3], [6, 4],
[7, 1], [7, 2], [7, 3], [7, 4],
[8, 1], [8, 2], [8, 3], [8, 4],
[9, 1], [9, 2], [9, 3], [9, 4],
[10, 1], [10, 2], [10, 3], [10, 4],
[11, 1], [11, 2], [11, 3], [11, 4],
[12, 1], [12, 2], [12, 3], [12, 4],
[13, 1], [13, 2], [13, 3], [13, 4]]

# Count for player's hand
playerHand = 0
# Count for dealer's hand
dealerHand = 0

# List to hold the player's hand
playerCards = []

# List to hold the dealer's hand
dealerCards = []
print(len(myCards))
print(myCards)
# Function to randomly deal two cards to whoever, and appends it to a list
def dealTwoCards(array, deck):
    '''
    Parameters: List, List(List)
    Returns: None, Affects given list in parameter
    '''
    # Randomly choose a card from the deck
    card = random.choice(range(len(deck)))
    card2 = random.choice(range(len(deck)))
    # Append the card to the list
    array.append(card)
    array.append(card2)
    # Remove the card from the deck
    deck.pop(card)
    deck.pop(card2)

    return card, card2

print(dealTwoCards(playerCards, myCards))
print(dealTwoCards(dealerCards, myCards))
print(myCards)
print(len(myCards))
print(playerCards)
print(dealerCards)


'''
dealCards(playerCards, myCards)
print(myCards)
dealCards(dealerCards, myCards)
print(myCards)
print(playerCards)
print(dealerCards)
'''
'''
print("You have been delt two cards. Your count is: " + str(playerHand))
playerChoice = str.lower(input("Choose to hit or stand!: "))

# This is the main game loop. It will keep going until the player decides to stand
while(1):

    if playerChoice == "h":
        print("You chose to hit.")
        playerHand += 1
        print("Your current hand is " + str(playerHand))

        # Conditional statement to check if player has went over 21
        if playerHand > 21:
            print("You have busted! You lose!")
            quit()
        # Conditional statement to check if player hit 21
        if playerHand == 21:
            print("You have won! You have a blackjack!")
            quit()

        playerChoice = str.lower(input("Hit or stand?: "))

    elif playerChoice == "s":
        print("You chose to stand.")
        print("Your final hand is " + str(playerHand))
        break

    else:
        playerChoice = str.lower(input("Invalid choice, please choose to (H)it or (S)tand: "))


# Dealer's turn
print("\nThe dealer is now playing.")
print("The dealer's hand is: " + str(dealerHand) + "\n")
while (1):
    if dealerHand < 17:
        dealerHand += 1
        print("The dealer has hit.")
        print("The dealer's hand is now " + str(dealerHand))
        if dealerHand > playerHand and dealerHand < 22:
            print("You have lost!")
            quit()
        else:
            continue
        time.sleep(1)
    elif dealerHand >= 17 and dealerHand <= 21:
        print("The dealer has stopped hitting.")
        print("The dealer's hand is now " + str(dealerHand))
        if dealerHand < playerHand:
            print("You have won!")
        elif dealerHand == playerHand:
            print("You have tied!")
        else:
            print("You have lost!")
        quit()
    else:
        print("The dealer's hand is now " + str(dealerHand))
        print("The dealer has busted! You have won!")
        quit()
'''














'''
# Instructions on how to play the game, nothing special here you can choose to
# keep this or not.
print("Welcome to Blackjack!")
print("Assuming you know the rules of Blackjack, this game is a copy")
print("to the real thing. You will be dealt two cards at the start round.")
print("You will then be able to choose whether to hit or stay. If you hit,")
print("you will be dealt another card. If you stay, you will be given a")
print("score of your hand. If you have a higher score than the dealer, you")
print("win. If you have a lower score than the dealer, you lose. If you")
print("tie, then you tie! \n")
print("The controls are relatively simple. To hit just type 'H' in")
print("the command line and press enter. To stand, just press 'S' in the")
print("command line and press enter. Let's begin! \n")
'''
