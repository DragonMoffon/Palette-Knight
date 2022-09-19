from src.iso_function import screen_pos, tile_pos, set_tile_size


def _test_screen_pos(tile_x, tile_y):
    print(screen_pos(tile_x, tile_y))


def _test_tile_pos(screen_x, screen_y):
    print(tile_pos(screen_x, screen_y))


def _test_reversal_screen_pos(tile_x, tile_y):
    _r_screen = screen_pos(tile_x, tile_y)
    _r_tile = tile_pos(*_r_screen)
    print((tile_x, tile_y), "->", _r_screen, "->", _r_tile)


def _test_reversal_tile_pos(screen_x, screen_y):
    _r_tile = tile_pos(screen_x, screen_y)
    _r_screen = screen_pos(*_r_tile)
    print((screen_x, screen_y), "->", _r_tile, "->", _r_screen)


if __name__ == '__main__':
    set_tile_size(32, 32)
    _test_screen_pos(3, 1)
    _test_tile_pos(96, 32)
    _test_reversal_screen_pos(10, 5)
    _test_reversal_tile_pos(256, 96)