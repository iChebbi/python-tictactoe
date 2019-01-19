from copy import deepcopy

infinity = float("inf")


class Board:
    def __init__(self):
        self.player = 'X'
        self.ai = 'O'
        self.fields = {}
        self.size = 3

        for x in range(self.size):
            for y in range(self.size):
                self.fields[x, y] = ''

    def move(self, x, y):
        board = deepcopy(self)
        board.fields[x, y] = board.player
        (board.player, board.ai) = (board.ai, board.player)  # Swap Player
        return board

    def best_move(self):
        return self.minimax(True)[1]  # get best move case coordinates

    def minimax(self, is_player):

        if self.winning_position():
            return (-1, None) if is_player else (+1, None)
        if self.is_a_tie():
            return 0, None

        if is_player:
            best = -infinity, None  # start with min value and maximize it
            for x, y in self.fields:
                if self.fields[x, y] == '':  # continue executing minimax on empty cases
                    value = self.move(x, y).minimax(not is_player)[0]
                    if value > best[0]:
                        best = (value, (x, y))
            return best
        else:
            best = +infinity, None  # start with max value and minimize it
            for x, y in self.fields:
                if self.fields[x, y] == '':  # continue executing minimax on empty cases
                    value = self.move(x, y).minimax(not is_player)[0]
                    if value < best[0]:
                        best = (value, (x, y))
            return best

    def is_a_tie(self):
        for (x, y) in self.fields:
            if self.fields[x, y] == '':
                return False
        return True

    def winning_position(self):
        # horizontal
        for y in (range(self.size)):
            winning = []
            for x in (range(self.size)):
                if self.fields[x, y] == self.ai: winning.append((x, y))
            if len(winning) == self.size:
                return winning

        # vertical
        for x in (range(self.size)):
            winning = []
            for y in (range(self.size)):
                if self.fields[x, y] == self.ai: winning.append((x, y))
            if len(winning) == self.size:
                return winning
        # first diagonal
        winning = []
        for y in range(self.size):
            x = y
            if self.fields[x, y] == self.ai: winning.append((x, y))
        if len(winning) == self.size:
            return winning
        # second diagonal
        winning = []
        for y in range(self.size):
            x = self.size - 1 - y
            if self.fields[x, y] == self.ai: winning.append((x, y))
        if len(winning) == self.size:
            return winning
        return None
