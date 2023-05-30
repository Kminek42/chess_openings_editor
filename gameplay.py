import gameplay_variables
import graphic_variables
import gameplay_variables


def reset_editor():
    file = open(gameplay_variables.filename, 'a')
    file.write('\n')
    file.write(gameplay_variables.line)
    gameplay_variables.run = False


def compare_lines():
    gameplay_variables.move_number += 4
    gameplay_variables.matching_lines = []
    for line in gameplay_variables.lines:
        matching = True
        for i in range(0, len(gameplay_variables.line)):
            if i < len(line):
                if gameplay_variables.line[i] != line[i]:
                    matching = False
        if matching:
            gameplay_variables.matching_lines.append(line)

    print('Matching lines:')
    print(' ', gameplay_variables.matching_lines)
    print('Next moves in database:')
    next_moves = []
    available_moves = []
    moves_count = []
    for line in gameplay_variables.matching_lines:
        if len(line) >= gameplay_variables.move_number + 4:
            temp = ''
            temp += str(line[gameplay_variables.move_number])
            temp += str(line[gameplay_variables.move_number + 1])
            temp += str(line[gameplay_variables.move_number + 2])
            temp += str(line[gameplay_variables.move_number + 3])
        next_moves.append(temp)

    move_index = -1
    for i in next_moves:
        if i not in available_moves:  # add new move
            available_moves.append(i)
            moves_count.append(1)
        else:
            for n in range(0, len(available_moves)):  # update move count
                if available_moves[n] == i:
                    move_index = n
            moves_count[move_index] += 1

    for i in range(0, len(available_moves)):
        print(available_moves[i], moves_count[i])


def update_line():
    gameplay_variables.line += gameplay_variables.move
    print('''
-----------------------------------
current line:''', gameplay_variables.line)
    compare_lines()


def make_move(position_x, position_y):
    if graphic_variables.buffered_piece == -1:  # if first click
        # show board
        graphic_variables.buffered_piece = graphic_variables.board_to_display[position_y][position_x]
        graphic_variables.board_to_display[position_y][position_x] = -1
        # store move
        gameplay_variables.move = chr(position_x + ord('a')) + str(8 - position_y)
    else:  # if second click
        # show board
        if position_x != ord(gameplay_variables.move[0]) - ord('a') or position_y != 56 - ord(gameplay_variables.move[1]):
            graphic_variables.board_to_display[position_y][position_x] = graphic_variables.buffered_piece
            graphic_variables.buffered_piece = -1
            # store move
            gameplay_variables.move += chr(position_x + ord('a')) + str(8 - position_y)
            if gameplay_variables.move == 'e1g1':
                graphic_variables.board_to_display[7][4] = -1
                graphic_variables.board_to_display[7][5] = 2
                graphic_variables.board_to_display[7][6] = 0
                graphic_variables.board_to_display[7][7] = -1

            if gameplay_variables.move == 'e1c1':
                graphic_variables.board_to_display[7][0] = -1
                graphic_variables.board_to_display[7][1] = -1
                graphic_variables.board_to_display[7][2] = 0
                graphic_variables.board_to_display[7][3] = 2
                graphic_variables.board_to_display[7][4] = -1

            if gameplay_variables.move == 'e8g8':
                graphic_variables.board_to_display[0][4] = -1
                graphic_variables.board_to_display[0][5] = 8
                graphic_variables.board_to_display[0][6] = 6
                graphic_variables.board_to_display[0][7] = -1

            if gameplay_variables.move == 'e8c8':
                graphic_variables.board_to_display[0][0] = -1
                graphic_variables.board_to_display[0][1] = -1
                graphic_variables.board_to_display[0][2] = 6
                graphic_variables.board_to_display[0][3] = 8
                graphic_variables.board_to_display[0][4] = -1

            print(gameplay_variables.move)
            update_line()
        else:
            graphic_variables.board_to_display[position_y][position_x] = graphic_variables.buffered_piece
            graphic_variables.buffered_piece = -1


def click_on_board(position_x, position_y):
    position_x = int(position_x / graphic_variables.screen_resolution * 8)
    position_y = int(position_y / graphic_variables.screen_resolution * 8)

    if not graphic_variables.white_on_bottom:
        position_x = 7 - position_x
        position_y = 7 - position_y

    make_move(position_x, position_y)


def click_on_gui(position_y):
    position_y = int(position_y / graphic_variables.screen_resolution * 8)
    if position_y == 0:
        reset_editor()


def mouse_click(position_x, position_y):
    if position_x < graphic_variables.screen_resolution:
        click_on_board(position_x, position_y)
    else:
        click_on_gui(position_y)
