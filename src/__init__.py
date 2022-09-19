from arcade.resources import add_resource_handle

from src.engine import _Engine

Engine = None


def run():
    global Engine
    add_resource_handle("data", "resources")
    Engine = _Engine(800, 600, True)
    Engine.launch()
