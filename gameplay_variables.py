move_number = 0  # index of the move in the current line
matching_lines = []  # list of matching lines index
line = ''  # current line
move = 'null'  # current move
filename = 'lines_black_french_defense.txt'
lines = open(filename).readlines()  # lines in the database
run = True
