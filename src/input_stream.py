from arcade import Window


class InputSource:
    pass


class Command:
    pass


class InputTarget:
    pass


class InputStream:
    """
    This takes a FIFO queue of Input sources, and uses them to commands to InputTargets. Generally InputTargets are
    the player, but they can be anything. The Ai uses the same system with enemies, and in cutscenes the player, and
    engine can share control of the player character.

    [Keyboard, Mouse, Cutscene] -> Command Stream -> Player Character.
    """
    pass
