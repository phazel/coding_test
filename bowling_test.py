
from blank import this_class
from bowling import bowling_game

def describe_standard_frame():
    def test_two_gutters_frame():
        frame = 0
        two_gutters = [[0,0]]
        result = bowling_game.calculate_standard_frame(frame, two_gutters)
        assert result == 0

    def test_strike_frame():
        frame = 0
        strike = [[10],[3,3]]
        result = bowling_game.calculate_standard_frame(frame, strike)
        assert result == 16

    def test_doublestrike_frame():
        frame = 0
        double_strike = [[10],[10], [2,6]]
        result = bowling_game.calculate_standard_frame(frame, double_strike)
        assert result == 22

    def test_triplestrike_frame():
        frame = 0
        triple_strike = [[10],[10],[10]]
        result = bowling_game.calculate_standard_frame(frame, triple_strike)
        assert result == 30

    def test_spare_frame():
        frame = 0
        spare = [[2,8],[3,5]]
        result = bowling_game.calculate_standard_frame(frame, spare)
        assert result == 13

def describe_round_nine():
    def test_two_gutters_frame():
        frame = 9
        two_gutters = [[],[],[],[],[],[],[],[],[0,0]]
        result = bowling_game.calculate_round_nine( two_gutters)
        assert result == 0
