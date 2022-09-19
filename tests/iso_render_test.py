import arcade

from arcade import Window

from time import time
from math import sin, cos, pi

from src.iso_function import screen_pos, set_tile_size


def _y_func(_in):
    return sin(_in * pi * 0.16)


def _x_func(_in):
    return cos(_in * pi * 0.2)


class _Engine(Window):

    def __init__(self, width, height, fullscreen):
        super().__init__(width, height, "Palette Knight", fullscreen=fullscreen, update_rate=1/120, draw_rate=1/120)

        self.cubes = arcade.SpriteList()
        self.start = 0

    def on_key_press(self, symbol: int, modifiers: int):
        self.close()

    def launch(self):
        _ = 32 * 5
        set_tile_size(_, _)
        # Do engine prep stuff

        cube_tex = arcade.load_texture(":data:/iso_cube.png")

        for x in range(40, 0, -1):
            for y in range(40, 0, -1):
                cube = arcade.Sprite()
                cube.position = screen_pos(x, y)
                cube.texture = cube_tex
                cube.center_x += self.width // 2
                cube.center_y -= self.height // 2 + 32*5
                cube.pos = (x, y)
                cube.true_y = cube.center_y
                cube.start_y = cube.center_y
                cube.scale = 5
                self.cubes.append(cube)

        self.start = time()
        self.run()

    def on_draw(self):
        self.clear()
        self.cubes.draw(pixelated=True)

    def on_update(self, delta_time: float):
        t = 2 * (time() - self.start)
        for cube in self.cubes:
            cube.true_y = cube.start_y + (_x_func(t + cube.pos[0]) + _y_func(-t + cube.pos[1])) * 15 * 5
            cube.center_y = int(cube.true_y)