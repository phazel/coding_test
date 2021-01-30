
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
        frame = [[],[],[],[],[],[],[],[],[0,0]]
        bonus = []
        result = bowling_game.calculate_round_nine(frame, bonus)
        assert result == 0

    def test_strike_frame():
        frame = [[],[],[],[],[],[],[],[],[10],[2,2]]
        bonus = []
        result = bowling_game.calculate_round_nine(frame, bonus)
        assert result == 14

    def test_double_strike_frame():
        frame = [[],[],[],[],[],[],[],[],[10],[10]]
        bonus = [7,3]
        result = bowling_game.calculate_round_nine(frame, bonus)
        assert result == 27

    def test_triple_strike_frame():
        frame = [[],[],[],[],[],[],[],[],[10],[10]]
        bonus = [10,8]
        result = bowling_game.calculate_round_nine(frame, bonus)
        assert result == 30

    def test_spare_frame():
        frame = [[],[],[],[],[],[],[],[],[8,2],[4]]
        bonus = []
        result = bowling_game.calculate_round_nine(frame, bonus)
        assert result == 14

def describe_round_ten():
    def test_two_gutters_frame():
        frame = [[],[],[],[],[],[],[],[],[],[0,0]]
        bonus = []
        result = bowling_game.calculate_round_ten(frame, bonus)
        assert result == 0

    def test_strike_frame():
        frame = [[],[],[],[],[],[],[],[],[],[10]]
        bonus = [3,5]
        result = bowling_game.calculate_round_ten(frame, bonus)
        assert result == 18

    def test_double_strike_frame():
        frame = [[],[],[],[],[],[],[],[],[],[10]]
        bonus = [10,5]
        result = bowling_game.calculate_round_ten(frame, bonus)
        assert result == 25

    def test_triple_strike_frame():
        frame = [[],[],[],[],[],[],[],[],[],[10]]
        bonus = [10,10]
        result = bowling_game.calculate_round_ten(frame, bonus)
        assert result == 30

    def test_spare_strike_frame():
        frame = [[],[],[],[],[],[],[],[],[],[8,2]]
        bonus = [10]
        result = bowling_game.calculate_round_ten(frame, bonus)
        assert result == 20
