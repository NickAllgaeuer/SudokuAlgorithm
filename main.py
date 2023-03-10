import numpy as np
import matplotlib.pyplot as plt

class Sudoku:
    def __init__(self, starting_board, draw, print_step):
        self.draw = draw
        self.print_step = print_step
        self.starting_board = starting_board
        self.board = np.copy(starting_board)
        self.size = self.board.shape[0]
        if self.draw:
            self.draw_board()
        self.tried = {}
        for row in range(self.size):
            for col in range(self.size):
                if not self.board[row, col]:
                    self.tried[(row, col,)] = []
        self.completed = False
        self.actions = 0
        self.states = [(np.copy(self.board), (0,0,),)]
    
    def draw_board(self):
        for i in range(self.size+1):
            if i % 3:
                linewidth = 1
            else:
                linewidth = 5
            plt.plot([0, self.size], [i, i], color="black", linewidth=linewidth)
            plt.plot([i, i], [0, self.size], color="black", linewidth=linewidth)
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i, j] and self.starting_board[i, j]:
                    plt.text(abs(j)+0.4, abs(i-self.size)-0.7, self.board[i, j], color="black")
                elif self.board[i, j]:
                    plt.text(abs(j)+0.4, abs(i-self.size)-0.7, self.board[i, j], color="red")
        plt.axis("off")
        plt.plot()
        plt.show()
    
    def increment_coords(self, row, col):
        if col < self.size-1:
            return row, col+1
        else:
            return row+1, 0
    
    def step(self):
        self.actions += 1
        row, col = self.states[-1][1]
        self.board = np.copy(self.states[-1][0])
        
        if not self.board[row, col]:
            for num in range(1,self.size+1):
                if self.is_safe(row, col, num) and num not in self.tried[(row, col,)]:
                    self.tried[(row,col,)].append(num)
                    self.board[row, col] = num
                    self.states.append((np.copy(self.board), (self.increment_coords(row, col)),))
                    break
            if not self.board[row, col]:
                self.tried[self.states[-1][1]] = []
                self.states.pop()
        else:
            self.states[-1] = np.copy(self.states[-1][0]), self.increment_coords(row, col)

    def solve(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row, col] and not self.is_safe(row, col, self.board[row, col], True):
                    if self.draw:
                        print("This puzzle is corrupt.")
                    return False
                    
        try:
            while np.count_nonzero(self.board == None):
                if self.draw and not self.actions % self.print_step:
                    self.draw_board()
                self.step()
            if self.draw:
                print(f"Solved Sudoku, took {self.actions} actions.")
            self.draw_board()
            return True

        except IndexError:
            if self.draw:
                print("This Sudoku can´t be Solved.")
            return False
        
    def is_safe(self, row, col, num, check_corruption=False):
        if check_corruption:
            tollerance = 1
        else:
            tollerance = 0
            
        if num is None:
            return True
        if np.count_nonzero(self.board[:,col] == num) > tollerance:
            return False
        elif np.count_nonzero(self.board[row,:] == num) > tollerance:
            return False
        elif np.count_nonzero(self.board[row//3 * 3: row//3 * 3+3, col//3 * 3: col//3 * 3+3] == num) > tollerance:
            return False
        else:
            return True

board = np.array([
       [None, None, 1, None, None, None, None, 9, None],
       [None, 7, 3, 4, None, None, None, None, None],
       [None, None, 6, None, None, 1, 5, 4, None],
       [9, None, 8, None, None, 2, 3, 6, 7],
       [None, None, None, None, 8, None, None, None, None],
       [None, None, None, 7, 1, 3, None, 8, 2],
       [1, None, None, None, None, None, None, 3, None],
       [None, None, 5, None, None, None, 6, None, None],
       [3, None, 2, None, None, None, 4, None, 5]], dtype=object)

draw = True     # Should the Sudoku be plotted?
step = 100      # Only show every nth step to save on runtime

game = Sudoku(board, draw, step)
solved = game.solve()

