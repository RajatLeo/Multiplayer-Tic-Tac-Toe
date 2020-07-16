class Game:
    def __init__(self, id):
        self.id = id
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.p1move = False
        self.p2move = True
        self.ready = False
        self.total_move = 0

    def connected(self):
        return self.ready

    def play(self, player, move):
        self.board[move[0]][move[1]] = player + 1
        if player == 0:
            self.p1move = True
            self.p2move = False
        else:
            self.p1move = False
            self.p2move = True

    def game_winner(self):
        winner = -1
        if self.board[0].count(1) == 3 or self.board[1].count(1) == 3 or self.board[2].count(1) == 3:
            winner = 0
            self.p1move = True
            self.p2move = True
        elif self.board[0].count(2) == 3 or self.board[1].count(2) == 3 or self.board[2].count(2) == 3:
            winner = 1
            self.p1move = True
            self.p2move = True
        elif (self.board[0][0] == 1 and self.board[1][0] == 1 and self.board[2][0] == 1) or (
                self.board[0][1] == 1 and self.board[1][1] == 1 and self.board[2][1] == 1) or (
                self.board[0][2] == 1 and self.board[1][2] == 1 and self.board[2][2] == 1):
            winner = 0
            self.p1move = True
            self.p2move = True
        elif (self.board[0][0] == 2 and self.board[1][0] == 2 and self.board[2][0] == 2) or (
                self.board[0][1] == 2 and self.board[1][1] == 2 and self.board[2][1] == 2) or (
                self.board[0][2] == 2 and self.board[1][2] == 2 and self.board[2][2] == 2):
            winner = 1
            self.p1move = True
            self.p2move = True
        elif (self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1) or (
                self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1):
            winner = 0
            self.p1move = True
            self.p2move = True
        elif (self.board[0][0] == 2 and self.board[1][1] == 2 and self.board[2][2] == 2) or (
                self.board[0][2] == 2 and self.board[1][1] == 2 and self.board[2][0] == 2):
            winner = 1
            self.p1move = True
            self.p2move = True
        elif self.total_move == 9:
            self.p1move = True
            self.p2move = True
            winner = None
        return winner

    def move(self):
        return self.board

    def resetgame(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.p1move = False
        self.p2move = True
        self.total_move = 0
