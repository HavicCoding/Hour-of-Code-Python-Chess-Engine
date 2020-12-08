from stockfish import Stockfish
from chess import Board

fishy = Stockfish('stockfish.exe')
board = Board()

position = []

isWhite = input("Do you want to be white or black?\n> ").lower()

while isWhite not in ['black','white']:
    isWhite = input('Please input "white" if you want to be white, "black" if you want to be black\n> ').lower()

if 'white' == isWhite:
    isWhite = 1 # Fishy is black

else:
    isWhite = 0 # Fishy is white

def play(counter):
    global position
    global fishy
    if counter % 2 == isWhite:
        move = fishy.get_best_move()
        print(move)
    elif counter % 2 != isWhite:
        move = input("Input your move in UCI format (Ex: e2e4 moves the piece at e2 to the e4 square)\n> ").lower()
        while True:
            if fishy.is_move_correct(move) == False:
                print("%s is not a valid move." %move)
                move = input("Input your move in UCI format (Ex: e2e4 moves the piece at e2 to the e4 square)\n> ").lower()
            elif fishy.is_move_correct(move):
                break
    position += [move]
    board.push_uci(move)
    fishy.set_position(position)
    print(fishy.get_board_visual())

def main():
    counter = 0
    while not board.is_game_over():
        play(counter)
        counter += 1
        if board.is_check():
            print("CHECK!")

    if board.is_checkmate():
        if len(position) % 2 != isWhite:
            print("Fishy won!")
        elif len(position) %2 == isWhite:
            print("You won!")
    else:
        print("There was a stalemate. Nobody won.")

main()
