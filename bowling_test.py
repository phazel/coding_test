
from blank import this_class

from bowling import bowling_game

def test_answer():
    #this = this_class()
    assert this_class.func(3) == 4

#
def test_calculate_open_frame():
    frame = 0
    two_gutters = [[0,0]]
    result = bowling_game.calculate_standard_frame(frame, two_gutters)
    assert result == 0

# calculates a frame with a strike
def test_calculate_strike_frame():
    frame = 0
    strike = [[10],[3,3]]
    result = bowling_game.calculate_standard_frame(frame, strike)
    assert result == 16

# calculates a spare score
def test_calculate_spare_frame():
    frame = 0
    spare = [[3,7],[3,3]]
    result = bowling_game.calculate_standard_frame(frame, spare)
    assert result == 13
