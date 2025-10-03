import keyboard
import os
import threading

connectFourBoard = [[0 for _ in range(7)] for _ in range (6)]

for row in connectFourBoard:
    print(row)

def esc_listener():
    keyboard.wait('esc')
    print("ESC pressed! Exiting...")
    os._exit(0)

print("Welcome to the game of Connect 4")
print("Player 1 is represented by 1s and Player 2 is represented by 2s")
current_player = 1
isGameOver = False
isTie = False
while not isGameOver:
    threading.Thread(target=esc_listener, daemon=True).start()
    try:
        column = int(input((f"Player {current_player} please select column between 1 and 7: "))) - 1
    except ValueError:
            print("Invalid input, please enter a number between 1 and 7")
            continue
    if column < 0 or column > 6:
        print("Invalid column, please select between 1 and 7")
        continue
    if connectFourBoard[0][column] != 0:
        print("Column is full, please select another column")
        continue
    for i in range(6):
	    if connectFourBoard[5 - i][column] == 0:
                connectFourBoard[5 - i][column] = current_player
                break
    for row in connectFourBoard:
        print(row)

# checking for a win condition
#check vertical
    for c in range(3):
        for r in range(7):
            if connectFourBoard[c][r] == connectFourBoard[c + 1][r] == connectFourBoard[c + 2][r] == connectFourBoard[c + 3][r] != 0:
                isGameOver = True
                break


#check horizontal
    for c in range(6):
        for r in range(4):
            if connectFourBoard[c][r] == connectFourBoard[c][r + 1] == connectFourBoard[c][r + 2] == connectFourBoard[c][r + 3] != 0:
                isGameOver = True
                break

#check diagonal - down right
    for c in range(3):
        for r in range(4):
            if connectFourBoard[c][r] == connectFourBoard[c + 1][r + 1] == connectFourBoard[c + 2][r + 2] == connectFourBoard[c + 3][r + 3] != 0:
                isGameOver = True
                break

#check diagonal - up right
    for c in range(3, 6):
        for r in range(4):
            if connectFourBoard[c][r] == connectFourBoard[c - 1][r + 1] == connectFourBoard[c - 2][r + 2] == connectFourBoard[c - 3][r + 3] != 0:
                isGameOver = True
                break

#check for tie
    for c in range(7):
        if connectFourBoard[0][c] == 0:
            isTie = False
            break
        else:
            isTie = True

    if isGameOver:
        print(f"Player {current_player} wins!")
        break
    if isTie:
        print("It's a tie!")
        break


    if current_player == 1:
        current_player = 2
    else:
        current_player = 1