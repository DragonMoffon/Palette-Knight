from typing import Union, Set


class SettingsObserver:
    """
    When an object in the engine cares about a setting getting updated it wants to be alerted. It creates an observer
    object and registers every event it cares about. Observer half of Observer Pattern.
    """

    def on_setting_update(self,setting: str, value: Union[int, float, bool]):
        raise NotImplementedError()


class SettingSubject:
    """
    Every setting is a subject for the settings Observer Pattern. This means there needs to be a lightweight system to
    track every observer who cares about a particular subject. Subject half of Observer Pattern
    """
    def __init__(self):
        self._observers: Set[SettingsObserver] = set()

    def register_observer(self, observer: SettingsObserver):
        self._observers.add(observer)

    def deregister_observer(self, observer: SettingsObserver):
        self._observers.discard(observer)

    def p_update_setting(self, setting: str, value: Union[int, float, bool]):
        for observer in tuple(self._observers):
            observer.on_setting_update(setting, value)
