# Blackjack

## For dependencies, all that is required to run the game is:
* Python 3.7
##### Note: I'm pretty sure this works with other Python 3.x versions, with Python 2.x versions **possibly** working as well, but I haven't tested it, I only have Python 3.7.4 installed on my machine. The only modules I imported are 'time' and 'random', but both are built-in to Python.
## To get the game running itself, all that is required is a Unix/Linux system with the dependencies installed.
1. Open your terminal and navigate to the directory where main.py and cards.py are located. ***Both files must be in the same directory***.
2. Once you have navigated to your terminal containing both file, run the following command within your terminal `python3 main.py`
3. The game should then start. Once it has started, you can read the instructions on how to play the game and then play the game! Once the game has decided on a winner, the game will automatically end, to play again, simply redo step 2.
##### Note: This tutorial has been written for Unix/Linux systems, and not WindowsOS. This isn't because of a technical issue (I think atleast), but because I don't own a Windows machine to test it on.

## Technical choices
#### One of the hardest technical choices I had to make was to write the program using functional programming over object-oriented programming. I specifically chose to use functional programming because to me it is easier to understand the problem and find the solution, given the constraints of the problem, specifically a self imposed time-limit. Though the trade-offs with using functional programming is heavier memory usage and not as scalable. ***With that being said***, had the problem had less contraints to it, such as a longer time-limit, multiple players, or Vegas-styled rules, I would have used object-oriented programming as that would have allowed me to not have to write as much code and it would have allowed me to scale easier than what I have written.
#### One choice I'd like to talk about, is the choice of using a list of list rather then something like a set. While at face-value it may seem that the former is better, mostly for it's O(1) time-complexity in deletion compared to O(n) time-complexiy of a list, a set would not have allowed me to randomly choose a card from the deck. I kept running into errors, and sources online, kept saying that other data strucutes would have work better for what I was trying to do.
#### Another choice I made is to seperate all the functions and data into different files than the game code. This was done because I wanted to keep the code clean and easy to read.

## Assumptions made
#### The Ace cards can be counted either as a 1 or 11, whenever it's more convienent for the player. For example, if the player has a total of 19, with an Ace card counting at 11 (8 + 11 = 19), and then the player decides to hit, and the next card put the count over 21, then the player's count will change. So, for example, if the player has a total of 19, and the player decides to hit and the next card is a 5, the players hand will change to 14 because 11 changes to 1 (8 + 1 + 5 = 14). Also another assumption was made that regardless of the amount of Aces you have, only two options will be available to the player. I decided to go with this, because, for example, let's say a player's hand contains only 4 Aces. There are a total of 5 different summations that can be made with 4 Aces (4, 14, 24, 34, 44) but only the first two matter, as the other 3 will result in a bust. That trend follows for if the player has 2-4 Aces in there hand.
#### Another assumption I made was that there is only one player against the dealer and that the game starts with only 1 deck. Unlike Vegas, since this game was made for only 1 person splitting isn't included, furthering the notion that having multiple decks would not have made sense.
#### A choice I made was the way the game calculates the 'ideal' count. I made it so the hand count closest to 21 will always be the one shown. Of course if there is a choice between a number <21 and a number >21, it will calculate and return the value that is <21. But if the both combinations of hand value is >21, then the final handcount will be the smaller number of the two.

## Personal Choices
#### There were a few personal touches I added to the game that I thought would make the game seem a bit more interactive. I don't think they were techincal choices per se, but I thought they were still worth mentioning.
#### One thing I added was time.sleep(1) throughout the game. This is purely added for the game feel more smooth and not to feel like the game is running too fast or was robotic (even though it is). Importing time does take some memory, but I think it was worth it, and if needed we can take it out without affecting the game.
#### Another thing I added was the ability to see the cards name with the value. Again this was done purely for user experience. I could've just made a simple array, like  `deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4`, which would have represented the cards in the deck, but I liked, and think it was worth it, to have the cards name with the value.

# Testing
## Dependencies
* Python 3.6+
* pytest
  * To install pytest, run the following command: `pip3 install -U pytest`
##### Note: If you'd like to learn more about pytest, you can read the [pytest documentation here](https://docs.pytest.org/en/latest/). Python 3.6 and higher is required to run pytest, so if the game does run with Python 2.x, it won't be able to run the test.
## Running the Test
1. Open your terminal and navigate to the directory where cards.py and test.py are located. You then can install pytest in here.
2. Once you have installed pytest, run the following command within your terminal `pytest test.py`
3. The test will then run. If the test passes, then all will pass and no at the bottom, it will show that all test passed. If the test fails, then it will throw an error and show the test that failed and why it failed. 
## Type of testing
#### The test that I implemented was a unit test, meaning that it tests a single function. The reason I did unit testing was because the entire code is made using functions, and I felt this was the best way to catch errors. I did some manually testing as well, by playing the game serveral times, but to cover any corner cases with the functions, unit testing was the best for this project.
