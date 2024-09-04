#from game import Game1

#g = Game() # this obje

#the things below are temporary, and they work for now

from board import Board

#mapping
let_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

t = Board()

while True:
    print(t)
    from_pos = input("From (format e.g. a2 or h3  etc.): ")
    to_pos = input("To: ")
    col_from, row_from = let_num[from_pos[0]], int(from_pos[1])
    col_to, row_to = let_num[to_pos[0]], int(to_pos[1])

    t.move_piece_if_to_is_valid(row_from, col_from, row_to, col_to)