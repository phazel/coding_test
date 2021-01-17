from bowling import bowling_game

# test one a see if a perfect score is calculated correctly
game = bowling_game(players = ['me'])
game.score['me'] = [[10],[10],[10],[10],[10],[10],[10],[10],[10],[10]]
game.bonus['me'] = [10,10]
assert game.calculate_score('me') == 300
print('score calculator works for a perfect game')
game.display_score('me')

# an imperfect score
game.score['me'] = [[10],[10],[10],[10],[10],[10],[10],[10],[10],[8,2]]
game.bonus['me'] = [10]
assert game.calculate_score('me') == 278
game.display_score('me')
print('score calculator works for a game ending in a spare')


# a really bad score
game.score['me'] = [[0,2],[1,0],[1,0],[3,4],[10],[5,4],[1,0],[1,0],[1,0],[3,2]]
game.bonus['me'] = []
assert game.calculate_score('me') == 47
print('score calculator works for my typical score')
game.display_score('me')

# at this point scoring is working okay so it's time to move on to input
assert game.validator(9,10) == 9
print('valid interger returns correctly')
assert game.validator(11,10) is None
print('invalid interger returns correctly')
assert game.validator('a string', 10) is None
print('string returns correctly')

# bonus game is working correctly:
game.score['me'] = [[0,2],[1,0],[1,0],[3,4],[10],[5,4],[1,0],[1,0],[1,0],[3,2]]
game.bonus_rounds()
assert game.bonus['me'] == []
print('bonus round working correctly for a final round less than 10')

# try it for yourself:
game = bowling_game(players = ['bill', 'ted'])
game.play()
