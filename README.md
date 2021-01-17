This is an attempt at the coding challenge set here:
https://github.com/DiUS/coding-tests/blob/master/dius_bowling.md

The plan was to write it in a sensible refactorable manner for the possibility of requirement or use changes.

As such I've written in a few extra features as it met the minimum viable product and they would be easiest to add when first building the project:
Multiple players
User input
Input validation (if you're going to let users near it...)

The unit tests are not exhaustive: the cover most of the posbilities within the original spec 

For validation I would have prefered to use regex but a try: int works well to attempt to validate that it is an integer, further checks that it is
within the possibilities of bowling. As the validation is on the user input I haven't run validation on the scoring, if you manually were to give it
a score outside the what should be possible for a round (i.e. 11) it will happily calculate with that number.

If you run the entire game it will run from frame to frame until you reach ten frames.  If your last frame was a spare or a strike you should be able
to input 1 or two more bowls respectively.

The file bowling.py contains the class, bowls_test.py contains a series of assert statements and a commented out game if you wish to run it.

The class functions are as follows:
__init__: Initialises an instance of the class, with a list of players a dictionary of their regular scores and a seperate dictionary for their bonuses
display_score: displays the score of the player
calculate_score: calculates score of a player.  It assumes that that a full game has been played can be adapted to work with incomplete score set
play: goes through the frames taking input for each players score
frame: takes input for each players score in the frame
validator: confirms that the input is a valid score 
roll: accepts input of a single roll, calls the validator
bonus_rounds: takes input of final round, if the 10 bowl was a spare or a score


