class bowling_game:
    def __init__(self, players):
        self.players = players # while not a requirement it seems like building the capability of many players is easier done now
        self.score = {}
        self.bonus = {}
        for player in players:
            self.score[player] = []
        for player in players:
            self.bonus[player] = []

    def display_score(self, player):
        print("the score of player {} is {}".format(player, self.calculate_score(player)))

    def calculate_standard_frame(bowls):
        if bowls[0][0] == 10: #strike sccore
            frame_score = 10
            if bowls[1][0] == 10:
                frame_score += 10 + bowls[2][0]
            else:
                frame_score += sum(bowls[1])
        elif sum(bowls[0]) == 10: #spare score
            frame_score = 10 + bowls[1][0]
        else:
            frame_score = sum(bowls[0])
        return frame_score

    def calculate_round_nine(bowls, bonus):
        if bowls[8][0] == 10:
            frame_score = 10
            if bowls[9][0] == 10:
                frame_score += (bowls[9][0] + bonus[0])
            else:
                frame_score += sum(bowls[9])
        elif sum(bowls[8]) == 10: #spare score
            frame_score = 10 + bowls[9][0]
        else:
            frame_score = sum(bowls[8])
        return frame_score

    def calculate_round_ten(bowls, bonus):
        frame_score = 0
        if bowls[9][0] == 10:
            frame_score += (10 + sum(bonus))
        elif sum(bowls[9]) == 10:
            frame_score += (10 + bonus[0])
        else:
            frame_score += (sum(bowls[9]))
        return frame_score

    def calculate_score(self, player):
        bowls = self.score[player]
        total_score = 0
        for i in range(8): # for the first 8 rounds we don't have to worry about bonus two bowls
            frame_score = calculate_standard_frame(bowls[i:(i+2)])
            total_score += frame_score
        # round nine scoring
        total_score +=  calculate_round_nine(bowls, self.bonus[player])
        # round ten scoring
        total_score += calculate_round_ten(bowls, self.bonus[player])
        return total_score

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

    def validator(self, num, limit):
        try:
            num = int(num) # this leave the possibilty of someone inputting a decimal, this could be handled with a replace or regex
            # as we're avoiding imports and I would prefer regex rounding down will do for the moment
        except:
            print("Please enter a valid integer")
            return None
        if num > limit: # can't roll higher than the number of pins standing
            print("You can't roll higher than {}, please enter a real bowling score".format(limit))
            return None
        if num < 0: # sooner or later someone will do it
            print("Please explain to the programmer how your roll increased the number of pins present. \n Please enter a valid number greater than or equal to 0")
            return None
        return num

    def roll(self, limit = 10): # we need to have valiation that the roll is an integer, less than the limit still need to confirm what happens when you give it a decimal
        bowl = input()
        bowl = self.validator(bowl, limit)
        if not bowl:
            bowl = self.roll()
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
