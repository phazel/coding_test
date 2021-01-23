
from blank import this_class

from bowling import bowling_game

def test_answer():
    #this = this_class()
    assert this_class.func(3) == 4

def test_calculate_standard_frame():
    frame = 0
    three_gutters = [[0],[0],[0]]
    result = bowling_game.calculate_standard_frame(frame, three_gutters)
    assert result == 0
