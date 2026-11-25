# Minimax algorithm for Tic Tac Toe (AI plays O)
board = [" "] * 9
WIN = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),
       (2,5,8),(0,4,8),(2,4,6)]

def evaluate():
    for a,b,c in WIN:
        if board[a] == board[b] == board[c] != " ":
            return 1 if board[a] == "O" else -1
    return 0

def minimax(maximizing):
    score = evaluate()
    if score or " " not in board:
        return score
    if maximizing:
        best = -2
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    best = 2
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            best = min(best, minimax(True))
            board[i] = " "
    return best

def show():
    for i in range(0,9,3):
        print(" | ".join(board[i:i+3]))

while True:
    show()
    if evaluate() or " " not in board:
        break
    try:
        move = int(input("Your move (1-9): ")) - 1
        if move not in range(9) or board[move] != " ":
            print("Invalid move."); continue
    except ValueError:
        print("Enter a number."); continue
    board[move] = "X"
    if evaluate() or " " not in board:
        break
    best_score, best_move = -2, None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score, best_move = score, i
    board[best_move] = "O"

show()
result = evaluate()
print("Computer wins!" if result == 1 else "You win!" if result == -1 else "Draw!")
