
############## Shahd Ahmed 221011110 ##############

def check(board, row, col):
    # Check column 
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal 
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal 
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i][j] == 1:
            return False
    
    # Check lower-left diagonal 
    for i, j in zip(range(row + 1, len(board)), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower-right diagonal 
    for i, j in zip(range(row + 1, len(board)), range(col + 1, len(board))):
        if board[i][j] == 1:
            return False

    return True


def placing_queens(board,row,goal):
    if row >= len(board):
        for i in range(len(board)):
            for j in range(len(board)):
                goal[i][j] = board[i][j]
        return True

    for col in range(len(board)):
        if check(board, row, col):
            board[row][col] = 1  
            print_board(board)
            print()

            if placing_queens(board, row + 1,  goal):
                return True

            #backtrack
            board[row][col] = 0  
    return False


def print_board(board):
    for row in board:
        row_str = ""
        for cell in row:
            row_str += str(cell) + " "  
        print(row_str)  


def main():
    N = 4  
    board = [[0 for _ in range(N)] for _ in range(N)]  
    print("Initial Board:") 
    print_board(board) 
    print() 

    
    goal = [[0 for _ in range(N)] for _ in range(N)]

    if not placing_queens(board, 0, goal):
        print("No Solution")
        return False

    print("The Goal:")
    print_board(goal)

    return True


if __name__ == "__main__":
    main()
