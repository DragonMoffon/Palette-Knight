from arcade import Window


class _EngineWindow(Window):

    def __init__(self, width, height, fullscreen):
        super().__init__(width, height, "Palette Knight", fullscreen=fullscreen, update_rate=1/120, draw_rate=1/120)

    def on_key_press(self, symbol: int, modifiers: int):
        self.close()

    def on_draw(self):
        self.clear()

    def launch(self):
        self.run()
