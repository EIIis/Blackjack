# Blackjack - Freenome
## For dependecies, all that is required to run the game is:
* Python 3.7
##### Note: I'm pretty sure this works with other Python 3.x versions, but I haven't tested it, I only have Python 3.7.4 installed on my machine. The only module we imported in 'time'
## To get the game running itself, all that is required is a Unix/Linux system with the depencies installed.
1. Open your command line tool and navigate to the directory where main.py is located
2. Type `python3 main.py`
3. The game will start.
##### Note: This tutorial has been written for Unix-based/Unix-like machines, and not WindowsOS because I don't know how Windows command prompt works. It could be possible that this tutorial will work on Windows, but I don't know since I don't use WindowsOS.
## Technical choices
#### One choice I'd like to talk about, is the choice of using a list of list rather then something like a set. While at face-value it may seem that the former is better, mostly for it's O(1) time-complexity in deletion compared to O(n) time-complexiy of a list, a set is would not have allowed me to randomly choose a card from the deck. I kept running into errors, and sources online, kept saying that I other data strucutes would have work better for what I was trying to do.
## Assumptions made
#### The Ace card can be counted either as a 1 or 11 whenever it's more convienent for the player. For example, if the player has a total of 19, with the Ace card counting at 11 (8 + 11 = 19), and then the player decides to hit, and the next card put the count over 21, then the player's count will change. So, for example, if the player has a total of 19, and the player decides to hit and the next card is a 5, the players hand will change to 14 because 11 changes to 1 (8 + 1 + 5 = 14).

## Testing
#### I'm not sure how to run 'formal' test in Python but, I did add assert statements to the code. To run that, just do [ADD LATER HERE ELLIS!]  

