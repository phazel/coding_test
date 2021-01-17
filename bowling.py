class bowling_game:
    def __init__(self, players):
        self.players = players
        self.score = {}
        self.bonus = {}
        for player in players:
            self.score[player] = []
        for player in players:
            self.bonus[player] = []

    def display_score(self, player):
        print("the score of player {} is {}".format(player, self.calculate_score(player)))

    def calculate_score(self, player):
        bowls = self.score[player]
        total_score = 0
        for i in range(8): # for the first 8 rounds we don't have to worry about bonus two bowls
            if bowls[i][0] == 10: #strike sccore
                frame_score = 10
                if bowls[i+1][0] == 10:
                    frame_score += 10 + bowls[i+2][0]
                else:
                    frame_score += sum(bowls[i+1])
            elif sum(bowls[i]) == 10: #spare score
                frame_score = 10 + bowls[i+1][0]
            else:
                frame_score = sum(bowls[i])
            total_score += frame_score
        # round nine scoring
        if bowls[8][0] == 10:
            frame_score = 10
            if bowls[9][0] == 10:
                frame_score += (bowls[9][0] + self.bonus[player][0])
            else:
                frame_score += sum(bowls[9])
        elif sum(bowls[8]) == 10: #spare score
            frame_score = 10 + bowls[9][0]
        else:
            frame_score + sum(bowls[8])
        total_score+= frame_score
        # round ten scoring
        if bowls[9][0] == 10:
            total_score += (10 + sum(self.bonus[player]))
        elif sum(bowls[9]) == 10:
            total_score += (10 + self.bonus[player][0])
        else:
            total_score += (sum(bowls[9]))
        return total_score

    def update_score(self, player, score):
        self.score[player] = score

    def play(self):
        for i in range(10):
            self.frame((i+1)) # people don't like counting from 0
        self.bonus_rounds()
        for player in self.players:
            self.display_score(player)

    def frame(self, frame_number):
        print("frame {}".format(frame_number))
        frame_bowls = []
        for player in self.players:
            print("input player {}'s number of pins taken".format(player))
            frame_bowls.append(self.roll())
            if frame_bowls[0] < 10:
                print("player {} scored {}, input the next lot of pins taken".format(player, frame_bowls[0]))
                frame_bowls.append(self.roll(limit = (10-frame_bowls[0])))
            self.score[player].append(frame_bowls)

    def roll(self, limit = 10): # we need to have valiation that the roll is an integer, less than the limit still need to confirm what happens when you give it a decimal
        bowl = input()
        try:
            bowl = int(bowl)
        except:
            print("Please enter a valid integer")
            bowl = roll()
        if bowl > limit:
            print("You can't roll higher than {}, please enter a real bowling score".format(limit))
            bowl = roll()
        return bowl

    def bonus_rounds(self):
        for player in self.players:
            bonus_scores = []
            if sum(self.score[player][9]) < 10:
                   pass
            elif self.score[player][9][0] == 10:
                bonus_scores.append(self.roll())
                bonus_scores.append(self.roll())
            else:
                bonus_scores.append(self.roll())
            self.bonus[player] = bonus_scores
