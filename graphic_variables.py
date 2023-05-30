import pygame

piece_surfaces_128 = [pygame.image.load('piece_textures/res_128/white_king_128.png'),  # 0
                      pygame.image.load('piece_textures/res_128/white_queen_128.png'),  # 1
                      pygame.image.load('piece_textures/res_128/white_rook_128.png'),  # 2
                      pygame.image.load('piece_textures/res_128/white_bishop_128.png'),  # 3
                      pygame.image.load('piece_textures/res_128/white_knight_128.png'),  # 4
                      pygame.image.load('piece_textures/res_128/white_pawn_128.png'),  # 5
                      pygame.image.load('piece_textures/res_128/black_king_128.png'),  # 6
                      pygame.image.load('piece_textures/res_128/black_queen_128.png'),  # 7
                      pygame.image.load('piece_textures/res_128/black_rook_128.png'),  # 8
                      pygame.image.load('piece_textures/res_128/black_bishop_128.png'),  # 9
                      pygame.image.load('piece_textures/res_128/black_knight_128.png'),  # 10
                      pygame.image.load('piece_textures/res_128/black_pawn_128.png')]  # 11

screen_resolution = 500

for i in range(0, 12):
    piece_surfaces_128[i] = pygame.transform.smoothscale(piece_surfaces_128[i],
                                                         (screen_resolution / 8, screen_resolution / 8))

screen = pygame.display.set_mode((screen_resolution * 1.1, screen_resolution))
white_on_bottom = True
show_coordinates = True
text_color = (0, 0, 0)
board_colors = [200, 200, 200], [60, 70, 140]

board_to_display = [[8, 10, 9, 7, 6, 9, 10, 8],
                    [11, 11, 11, 11, 11, 11, 11, 11],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [5, 5, 5, 5, 5, 5, 5, 5],
                    [2, 4, 3, 1, 0, 3, 4, 2]]

buffered_piece = -1
