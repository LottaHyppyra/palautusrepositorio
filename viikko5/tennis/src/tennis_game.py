START_POINTS = 0
ROUND_WIN = 1
FORTY_POINTS = 4

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = {player1_name: START_POINTS, player2_name: START_POINTS}

    def won_point(self, player_name):
        self.players[player_name] += ROUND_WIN

    def player_one(self):
        return list(self.players.keys())[0]

    def player_two(self):
        return list(self.players.keys())[1]

    def player_one_points(self):
        return self.players[self.player_one()]

    def player_two_points(self):
        return self.players[self.player_two()]

    def is_even(self):
        return self.player_one_points() == self.player_two_points()

    def score_diff(self):
        diff = self.player_one_points() - self.player_two_points()

        if diff >= 2:
            return 2

        elif diff <= -2:
            return -2

        return diff

    def scores_higher_than_four(self):
        return self.player_one_points() >= FORTY_POINTS or self.player_two_points() >= FORTY_POINTS

    def score_outputs(self, score: int):
        outputs = ["Love", "Fifteen", "Thirty", "Forty"]
        return outputs[score]

    def when_even(self, score: int):
        if score >= FORTY_POINTS:
            return "Deuce"
        
        return self.score_outputs(score) + "-All"

    def winning_outputs(self, diff: int):
        outputs = ["-", "Advantage player1", "Win for player1", "Win for player2", "Advantage player2"]
        return outputs[diff]

    def get_score(self):
        if self.is_even():
            return self.when_even(self.player_one_points())

        elif self.scores_higher_than_four():
            return self.winning_outputs(self.score_diff())

        else:
            return self.score_outputs(self.player_one_points()) + "-" + self.score_outputs(self.player_two_points())
