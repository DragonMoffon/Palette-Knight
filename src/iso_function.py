tile_width = 0
tile_height = 0


def set_tile_size(width, height):
    global tile_width
    global tile_height

    tile_width = width
    tile_height = height


def screen_pos(tile_x, tile_y):
    """
    To convert from tile co-ordinates we can use a simple matrix to convert the input values.

    The operation begins by rotating the sprite by 45 degrees and shrinking by half. If we did this operation on
    a unit vector i we would see that i is equal to moving across on the X axis by 1 and down on the Y axis by 0.5.
    It is mirrored for the unit vector j. Giving the matrix [1, 0.5][-1, 0.5].

    We then multiply by the tile size to expand the co-ordinate system. This leaves an artifact however as a rotated
    tile covers 4 unit tiles. So halving the size gives the correct and final matrix [0.5w, -0.5w][0.25h, 0.25h]

    reference https://www.youtube.com/watch?v=04oQ2jOUjkU&ab_channel=JordanWest.

    *note, by using tiles that are divisible by 2 and 4 we can ensure the returned screen space is always an integer
    value. This is particularly valuable with low resolution assets.

    **note 2, we also shift the final result on the x-axis which aligns 0,0 with the center of the tile.

    :param tile_x: x co-ordinate in tile space
    :param tile_y: y co-ordinate in tile space
    :return: vector co-ordinate in screen space.
    """

    screen_x = int(0.5*tile_width*tile_x - 0.5*tile_height*tile_y)
    screen_y = int(0.25*tile_height*tile_x + 0.25*tile_width*tile_y)

    return screen_x, screen_y


def tile_pos(screen_x, screen_y):
    """
    Because the transformation from tile to screen co-ordinates is a matrix we can easily reverse the transformation
    by using the inverted matrix. Using some major simplification we end up with the matrix [1/2w, 1/h][-1/2w, 1/h]

    reference https://www.youtube.com/watch?v=04oQ2jOUjkU&ab_channel=JordanWest.

    *note, the simplification was done by myself, and is not mentioned in the video

    **note 2, we do have to shift the tile by half width first.

    :param screen_x:
    :param screen_y:
    :return:
    """

    tile_x = int(screen_x/tile_width + screen_y/(0.5*tile_height))
    tile_y = int(screen_y/(0.5*tile_height) - screen_x/tile_width)

    return tile_x, tile_y


