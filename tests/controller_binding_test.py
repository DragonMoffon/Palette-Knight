import arcade
import pyglet


class App(arcade.Window):

    def __init__(self):
        super().__init__()
        pyglet.input.controller.add_mappings_from_file(r"C:\Users\Playtech\Desktop\Code\Python\Palette-Knight\resources\game_controller_bindings.txt")

        self.controller = pyglet.input.get_controllers()[0]
        print(self.controller.name, self.controller.guid)

        mapping = pyglet.input.controller.get_mapping(self.controller.guid)
        print(mapping)

    def on_draw(self):
        self.clear()

    def on_update(self, delta_time: float):
        print(self.controller.rightx)


if __name__ == '__main__':
    App().run()