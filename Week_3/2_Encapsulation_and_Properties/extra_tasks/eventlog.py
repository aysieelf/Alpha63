class EventLog:
    def __init__(self):
        self._event_log_list = []

    @property
    def get_log(self):
        return tuple(self._event_log_list)

    def add_event(self, event: str):
        self._event_log_list.append(event)
