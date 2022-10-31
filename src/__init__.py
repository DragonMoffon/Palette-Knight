from arcade.resources import add_resource_handle

from src.window import _EngineWindow

Engine = None


def run():
    global Engine
    add_resource_handle("asset", "assets")
    add_resource_handle("data", "data")
    Engine = _EngineWindow(800, 600, True)
    Engine.launch()
