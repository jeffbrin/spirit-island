from board import Board

board = Board.choose_board('A')

for id, land in board.lands.items():
    print(id, [n.id for n in land.neighbours])
