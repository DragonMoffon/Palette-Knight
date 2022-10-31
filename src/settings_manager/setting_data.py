# Each settings tab has a group of variables that need to be saved between launches.
# Graphics, Controls, Audio, Accessibility. These settings influence a huge array of engine systems.
# These settings must be read only for everything except a settings manager. The Settings manager does not care
# what these settings do or what they mean. All they know is that there are rules on what they can and cannot be.
from typing import Tuple

from src.settings_manager.settings_observer import SettingSubject


class SettingsData:

    def __init__(self):
        self._setting_subject = SettingSubject()

    @property
    def settings_broadcast(self):
        return self._setting_subject


class GraphicsData(SettingsData):

    def __init__(self):
        super().__init__()
        self._resolution: int = 0
        self._window_mode: int = 0
        self._fps_cap: int = 0
        self._vsync: bool = False
        self._anti_aliasing: bool = False

    def set_resolution(self, resolution: int):
        self._resolution = resolution
        self._setting_subject.p_update_setting("resolution", resolution)

    def set_window_mode(self, window_mode: int):
        self._window_mode = window_mode
        self._setting_subject.p_update_setting("window_mode", window_mode)

    def set_fps_cap(self, fps_cap: int):
        self._fps_cap = fps_cap
        self._setting_subject.p_update_setting("fps_cap", fps_cap)

    def set_vsync(self, vsync: bool):
        self._vsync = vsync
        self._setting_subject.p_update_setting("vsync", vsync)

    def set_anti_aliasing(self, anti_aliasing):
        self._anti_aliasing = anti_aliasing
        self._setting_subject.p_update_setting("anti_aliasing", anti_aliasing)

    @property
    def resolution(self):
        return self._resolution

    @property
    def window_mode(self):
        return self._window_mode

    @property
    def fps_cap(self):
        return self._fps_cap

    @property
    def vsync(self):
        return self._vsync

    @property
    def anti_aliasing(self):
        return self._anti_aliasing
