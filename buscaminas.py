from random import randint


class Buscaminas:
    
    def __init__(self, rows=None, cols=None, bombs=None):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs


    def play(self, mov, row, bomb):
        pass

    def questions(self):
        pass

    def board(self):
        board = []
        val = ' '
        for i in range (self.rows):
            board.append([])
            for j in range (self.cols):
                board[i].append(val)
        return board

    def show(self,board):
        for self.rows in board:
            for elem in self.rows:
                print(elem, end="")
        print()
    
    def lay_bombs(self,board):
        hidden_bombs = []
        num = 0
        while num <= self.bombs:
            y = randint(0,self.rows - 1)
            x = randint(0,self.cols - 1)
            if board[y][x] !=9:
                board[y][x] =9
                numero += 1
                minas_ocultas.append((y,x))
        return board, lay_bombs

    def clues(self, board, row, col):
        row = self.rows
        col = self.cols
        for x in range(row):
            for y in range(col):
                if board[x][y] == 9:
                    for i in [-1,0,1]:
                        for j in [-1,0,1]:
                            if 0 <= y+i <= col-1 and 0 <= x+j <= col-1:
                                if board[y+i][x+j] != 9:
                                    board[y+i][x+j] += 1
        return board

    def full_board(self, board, row, col):
        row = self.rows
        col = self.cols
        for y in range(row):
            for x in range(col):
                if board[y][x] == ' ':
                    return False
        return True


    def win(self):
        pass

    def lose(self):
        pass
