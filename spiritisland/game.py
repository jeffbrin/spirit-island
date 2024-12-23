from board import Board

board = Board.choose_board('A')

for id, land in board.lands.items():
    print(id, [n.id for n in land.neighbours])

land = board.lands[1]
print(land.id)

targets = land.available_target_lands(2)
print([t.id for t in targets])