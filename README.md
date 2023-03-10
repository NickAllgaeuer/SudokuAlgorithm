# Solving Sudoku Algorithmically with Python and Numpy

In this project, we will use Python and Numpy to create a Sudoku solver. We will start by creating a class Sudoku which will contain all the methods and variables required for solving the Sudoku. We will then use the numpy library to create a 2D array representing the Sudoku board.

```python
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
```

In the __init__ method, we initialize the class variables starting_board, draw, and print_step. We create a copy of the starting board as board and determine its size. If the draw variable is set to True, we call the draw_board() method to plot the Sudoku board using matplotlib. We create an empty dictionary tried to keep track of the numbers that have been tried at each empty cell of the board. We set completed to False, actions to 0, and create a list states to keep track of the different states of the board during the solving process.

```python

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
```

The draw_board() method plots the Sudoku board using matplotlib. We loop through the rows and columns of the board to plot the lines separating the cells. We then loop through the cells to plot the numbers in the cells. If a number is present in the starting board, it is plotted in black. If it is added during the solving process, it is plotted in red.

```python

    def increment_coords(self, row, col):
        if col < self.size-1:
            return row, col+1
        else:
            return row+1, 0
```
The increment_coords() method increments the coordinates of the current cell to move to the next cell in the solving process.

```python

    def step(self):
        self.actions += 1
        row, col = self.states[-1][1]
        self.board = np.copy(self.states[-1][0])
        
        if not self.board[row, col]:
            for num
```
