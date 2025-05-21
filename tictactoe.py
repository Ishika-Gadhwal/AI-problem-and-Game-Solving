# There are 2 Player
# Max is Computer --> 'o'
# Min is human --> 'x'

# Creating a Board
board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
currentPlayer = 'Min'

# print Board Function
def print_board(board):
    for row in board:
        print(' | ', row[0], ' | ', row[1], ' | ', row[2], ' | ')
    print()
# initial board
print_board(board)

# Min move handling
def min_move(board):
    while True:
        try:
            x, y = map(int, input("Enter the position (row, column) : ").split())

            if x not in range(3) or y not in range(3):  # Check if input is within bounds
                print("Invalid position! Enter row and column between 0 and 2.")
                continue

            if board[x][y] != ' ':
                print("Position already occupied! Try again.")
                continue

            board[x][y] = 'x'  # Assign move
            print("Human Move: ")
            print_board(board)
            break  # Exit loop if valid move is made

        except ValueError:
            print("Invalid input! Please enter two numbers separated by space.")


# Checking the win or draw Condition
def check_winner(board):

  # Checking win condition
  if(board[0][0] == board[1][1] == board[2][2] == 'x' or board[0][2] == board[1][1] == board[2][0] == 'x' or board[0][0] == board[0][1] == board[0][2] == 'x'
    or board[1][0] == board[1][1] == board[1][2] == 'x'or board[2][0] == board[2][1] == board[2][2] == 'x' or board[0][0] == board[1][0] == board[2][0] == 'x'
    or board[0][1] == board[1][1] == board[2][1] == 'x'or board[0][2] == board[1][2] == board[2][2] == 'x'):
    return 'Min'
  elif(board[0][0] == board[1][1] == board[2][2] == 'o' or board[0][2] == board[1][1] == board[2][0] == 'o' or board[0][0] == board[0][1] == board[0][2] == 'o'
    or board[1][0] == board[1][1] == board[1][2] == 'o'or board[2][0] == board[2][1] == board[2][2] == 'o' or board[0][0] == board[1][0] == board[2][0] == 'o'
    or board[0][1] == board[1][1] == board[2][1] == 'o'or board[0][2] == board[1][2] == board[2][2] == 'o'):
    return 'Max'

  # Checking draw condition
  found = any(' ' in row for row in board)
  if not found:
    return 'Draw'

  return None

# calculating Score
def evaluate(board):
  if(check_winner(board) == 'Max'):
    return 1
  elif(check_winner(board) == 'Min'):
    return -1
  elif(check_winner(board) == 'Draw'):
    return 0
  return None   # Game still ongoing

# Main Function
def minimax(board, isMax):
  score = evaluate(board)

  # Base case: If the game is over, return the score
  if(score is not None):
    return score

  if isMax:  # Maximizing player (Computer)
    bestScore = -float('inf') # -float('inf') represents the lowest possible value, ensuring that any valid move will be better than the initial value.
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'o'  # Try move
                bestScore = max(bestScore, minimax(board, False))
                board[i][j] = ' '  # Undo move
    return bestScore
  else:  # Minimizing player (Human)
      bestScore = float('inf') # float('inf') represents a very high number, effectively the worst possible scenario for Min.
      for i in range(3):
          for j in range(3):
              if board[i][j] == ' ':
                  board[i][j] = 'x'  # Try move
                  bestScore = min(bestScore, minimax(board, True))
                  board[i][j] = ' '  # Undo move
      return bestScore

# Find the best move for the computer (Max)
def max_move(board):
  bestScore = -float('inf')
  bestMove = None

  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':  # Check empty cells
          board[i][j] = 'o'  # Try move
          moveScore = minimax(board, False)
          board[i][j] = ' '  # Undo move

          if moveScore > bestScore:  # Find best move
              bestScore = moveScore
              bestMove = (i, j)

  if bestMove:
    board[bestMove[0]][bestMove[1]] = 'o'  # Make the best move
    print("Computer Move:")
    print_board(board)

# Game loop
def play_game():
  global currentPlayer  # Fix: Use global variable

  while True:
    if(currentPlayer == "Min"):
      min_move(board)
    else:
      max_move(board)

    result = check_winner(board)
    if(result == "Min"):
      print("Min Won !!!")
      print("Hurray! You won\n")
      break
    elif(result == "Max"):
      print("Max Won !!!")
      print("Oops! You lose\n")
      break
    elif(result == "Draw"):
      print("Draw !!!")
      print("Oops\n")
      break

    # Switch player turn
    currentPlayer = "Max" if currentPlayer == "Min" else "Min"

play_game()