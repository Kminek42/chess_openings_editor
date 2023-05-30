import pygame
import graphic_variables


def draw_buttons():
    tile_size = graphic_variables.screen_resolution / 8
    pygame.draw.rect(graphic_variables.screen, (200, 50, 50),
                     [8 * tile_size, 0 * tile_size, tile_size + 1, tile_size + 1])


def draw_coordinates():
    tile_size = graphic_variables.screen_resolution / 8
    font = pygame.font.SysFont(None, int(graphic_variables.screen_resolution / 40))
    for y in range(0, 8):
        for x in range(0, 8):
            text = chr(x + 97) + chr(7 - y + 49)
            img = font.render(text, True, graphic_variables.text_color)
            img.set_alpha(150)
            if graphic_variables.white_on_bottom:
                graphic_variables.screen.blit(img, (x * tile_size, y * tile_size))
            else:
                graphic_variables.screen.blit(img, ((7 - x) * tile_size, (7 - y) * tile_size))


def draw_pieces():
    tile_size = graphic_variables.screen_resolution / 8
    for y in range(0, 8):
        for x in range(0, 8):
            if graphic_variables.white_on_bottom:
                if graphic_variables.board_to_display[y][x] != -1:
                    graphic_variables.screen.blit(
                        graphic_variables.piece_surfaces_128[graphic_variables.board_to_display[y][x]],
                        (x * tile_size, y * tile_size))
            else:
                if graphic_variables.board_to_display[y][x] != -1:
                    graphic_variables.screen.blit(
                        graphic_variables.piece_surfaces_128[graphic_variables.board_to_display[y][x]],
                        ((7 - x) * tile_size, (7 - y) * tile_size))

    if graphic_variables.buffered_piece != -1:
        graphic_variables.screen.blit(graphic_variables.piece_surfaces_128[graphic_variables.buffered_piece],
                                      (pygame.mouse.get_pos()[0] - tile_size / 2, pygame.mouse.get_pos()[1] - tile_size / 2))


def draw_board():
    tile_size = graphic_variables.screen_resolution / 8
    for y in range(0, 8):
        for x in range(0, 8):
            pygame.draw.rect(graphic_variables.screen, graphic_variables.board_colors[(y + x) % 2],
                             [x * tile_size, y * tile_size, tile_size + 1, tile_size + 1])


def draw():
    draw_board()
    draw_pieces()
    draw_coordinates()
    draw_buttons()
    pygame.display.flip()


def draw_gui():
    print("null")
