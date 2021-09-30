import time
from cards import *

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

dealTwoCards(playerCards, myCards)
dealTwoCards(dealerCards, myCards)
print("The dealer has been dealt two cards. His cards are hidden!")
print("You have been delt two cards. Your cards are:")
print(nameOfCards(playerCards))
playerHand = handValue(playerCards)
print("Your current handcount is: " + str(playerHand) + ".\n")
playerChoice = str.lower(input("Choose to hit or stand!: "))

# This is the main game loop. It will keep going until the player decides to stand
while(1):

    if playerChoice == "h":
        print("You chose to hit.")
        time.sleep(1)
        dealOneCard(playerCards, myCards)
        print("Your new hand is:")
        print(nameOfCards(playerCards))

        playerHand = handValue(playerCards)
        print("Your hand count is " + str(playerHand) + "!\n")

        # Conditional statement to check if player has went over 21
        if playerHand > 21:
            time.sleep(1)
            print("You have busted! You lose!")
            quit()
        # Conditional statement to check if player hit 21
        elif playerHand == 21:
            time.sleep(1)
            print("You have won! You have a blackjack!")
            quit()

        playerChoice = str.lower(input("Hit or stand?: "))

    elif playerChoice == "s":
        if playerHand == 21:
            print("You chose to stand.")
            print("Your final hand is " + str(playerHand))
            print("You have won! You have a blackjack!")
            quit()
        else:
            print("You chose to stand.")
            print("Your final hand is " + str(playerHand))
            break
    else:
        playerChoice = str.lower(input("Invalid choice, please choose to (H)it or (S)tand: "))


# Dealer's turn
print("\nThe dealer is now playing.")
time.sleep(1)
print("The dealer's cards are: ")
print(nameOfCards(dealerCards))
dealerHand = handValue(dealerCards)
time.sleep(1)
print("Dealer's current handcount is: " + str(dealerHand) + ".\n")

while (1):
    time.sleep(1)
    if dealerHand < 17:
        time.sleep(1)
        print("The dealer has hit.")
        dealOneCard(dealerCards, myCards)
        print("Dealer's new hand is:")
        print(nameOfCards(dealerCards))

        dealerHand = handValue(dealerCards)
        print("Dealer's handcount is " + str(dealerHand) + "!\n")

        if dealerHand > playerHand and dealerHand < 22:
            print("You have lost!")
            quit()
        else:
            continue
        time.sleep(1)
    elif dealerHand >= 17 and dealerHand <= 21:
        print("The dealer's hand is now " + str(dealerHand))
        print("The dealer has stopped hitting.")
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
