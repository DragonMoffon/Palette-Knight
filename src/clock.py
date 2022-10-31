class Clock:

    def __init__(self):
        self._time: float = 0
        self._const_time: float = 0
        self._frame_time: int = 0

        self._tick_speed: float = 1
        self._delta_time: float = 0

        self._ticking: bool = True

    def tick(self, delta_time):
        self._delta_time = delta_time
        self._frame_time += 1

        self._const_time += delta_time
        self._time += delta_time * self._tick_speed * self._ticking

    def length(self, time):
        return self._time - time

    def const_length(self, const_time):
        return self._const_time - const_time

    def set_tick_speed(self, speed):
        self._tick_speed = speed

    def pause_clock(self):
        self._ticking = False

    def resume_clock(self):
        self._ticking = True

    @property
    def time(self):
        return self._time

    @property
    def const_time(self):
        return self._const_time

    @property
    def frame(self):
        return self._frame_time

    @property
    def delta_time(self):
        return self._delta_time * self._tick_speed * self._ticking

    @property
    def delta_const_time(self):
        return self._delta_time

    @property
    def tick_speed(self):
        return self._tick_speed

    @property
    def paused(self):
        return not self._ticking

