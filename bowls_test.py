from bowling import bowling_game

# test one a see if a perfect score is calculated correctly
game = bowling_game(players = ['me'])
game.score['me'] = [[10],[10],[10],[10],[10],[10],[10],[10],[10],[10]]
game.bonus['me'] = [10,10]
game.display_score('me')


# an imperfect score
game.score['me'] = [[8,2],[10],[10],[3,4],[10],[5,4],[10],[10],[10],[10]]
game.bonus['me'] = [10,10]
game.display_score('me')

# a really bad score
game.score['me'] = [[0,2],[1,0],[1,0],[3,4],[10],[5,4],[1,0],[1,0],[1,0],[3,2]]
game.bonus['me'] = [10,10]
game.display_score('me')

# at this point scoring is working okay so it's time to move on to input

game.play()
