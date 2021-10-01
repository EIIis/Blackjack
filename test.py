from pytest import *
from cards import *

# Testing the nameOfCard function.
def test1():
    assert(nameOfCards([[3, 1], [4, 2], [13, 3], [13, 4]]) == (["3 of Spades", "4 of Hearts", "King of Diamonds", "King of Clubs"]))
    assert(nameOfCards([[2, 1], [4, 2], [5, 3], [13, 4]]) == (["2 of Spades", "4 of Hearts", "5 of Diamonds", "King of Clubs"]))
    assert(nameOfCards([[1, 1]]) == (['Ace of Spades']))
    assert(nameOfCards([]) == ([]))

# Testing that after dealing cards, the deck's length is changed because we're removing cards from it.
def test2():
    assert(dealTwoCards(playerCards, myCards) == None and (len(myCards) == 50))
    assert(dealOneCard(playerCards, myCards) == None and (len(myCards) == 49))
    assert(dealTwoCards(dealerCards, myCards) == None and (len(myCards) == 47))
    assert(dealOneCard(dealerCards, myCards) == None and (len(myCards) == 46))
    assert(dealTwoCards(playerCards, myCards) == None and (len(myCards) == 44))
    assert(dealOneCard(playerCards, myCards) == None and (len(myCards) == 43))
    assert(dealTwoCards(dealerCards, myCards) == None and (len(myCards) == 41))
    assert(dealOneCard(dealerCards, myCards) == None and (len(myCards) == 40))
    assert(dealTwoCards(playerCards, myCards) == None and (len(myCards) == 38))
    assert(dealOneCard(playerCards, myCards) == None and (len(myCards) == 37))

# Checking to faceOfCard function.
def test3():
    assert(faceOfCard([1, 4]) == "Ace")
    assert(faceOfCard([2, 4]) == 2)
    assert(faceOfCard([3, 4]) == 3)
    assert(faceOfCard([4, 4]) == 4)
    assert(faceOfCard([5, 4]) == 5)
    assert(faceOfCard([6, 4]) == 6)
    assert(faceOfCard([7, 4]) == 7)
    assert(faceOfCard([8, 4]) == 8)
    assert(faceOfCard([9, 4]) == 9)
    assert(faceOfCard([10, 4]) == 10)
    assert(faceOfCard([11, 4]) == "Jack")
    assert(faceOfCard([12, 4]) == "Queen")
    assert(faceOfCard([13, 4]) == "King")

# Checking to make sure the cards give out the right names.
def test4():
    assert(suitOfCard([1, 4]) == "Clubs")
    assert(suitOfCard([1, 3]) == "Diamonds")
    assert(suitOfCard([1, 2]) == "Hearts")
    assert(suitOfCard([1, 1]) == "Spades")
    assert(suitOfCard([2, 4]) == "Clubs")
    assert(suitOfCard([2, 3]) == "Diamonds")
    assert(suitOfCard([2, 2]) == "Hearts")
    assert(suitOfCard([2, 1]) == "Spades")
    assert(suitOfCard([3, 4]) == "Clubs")
    assert(suitOfCard([3, 3]) == "Diamonds")
    assert(suitOfCard([3, 2]) == "Hearts")
    assert(suitOfCard([3, 1]) == "Spades")
    assert(suitOfCard([12, 4]) == "Clubs")
    assert(suitOfCard([12, 3]) == "Diamonds")
    assert(suitOfCard([12, 2]) == "Hearts")
    assert(suitOfCard([12, 1]) == "Spades")
    assert(suitOfCard([13, 4]) == "Clubs")
    assert(suitOfCard([13, 3]) == "Diamonds")
    assert(suitOfCard([13, 2]) == "Hearts")
    assert(suitOfCard([13, 1]) == "Spades")

# Checking to make sure it returns the sumOfAllExceptAce
def test5():
    assert(sumOfAllExceptAce([[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4], [11, 4], [12, 4], [13, 4]]) == (84, 1))
    assert(sumOfAllExceptAce([[1, 1], [1, 2], [1, 3], [1, 4]]) == (0, 4))
    assert(sumOfAllExceptAce([[2, 1], [3, 4], [4, 3], [5, 1]]) == (14, 0))
    assert(sumOfAllExceptAce([[1, 1], [5, 2], [1, 3], [13, 4]]) == (15, 2))

# Checking to see that the bestValueOfHand returns the best possible value of the hand, whether given an Ace or not.
def test6():
    assert(bestValueOfHand([[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4], [11, 4], [12, 4], [13, 4]]) == 85)
    assert(bestValueOfHand([[1, 1], [1, 2], [1, 3], [1, 4]]) == 14)
    assert(bestValueOfHand([[8, 1], [1, 4], [4, 3]]) == 13)
    assert(bestValueOfHand([[8, 3], [1, 2], [2, 3]]) == 21)
    assert(bestValueOfHand([[13, 1], [11, 2], [1, 3]]) == 21)
    assert(bestValueOfHand([[12, 1], [10, 2]]) == 20)
