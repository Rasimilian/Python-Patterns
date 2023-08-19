from typing import Dict, Any


class Borg:
    _shared_state: Dict[str, Any] = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state


class SubBorg(Borg):
    def __init__(self, state: str = None) -> None:
        super().__init__()
        if state:
            self.state = state
        else:
            if not hasattr(self, "state"):
                self.state = "First init"


class AnotherBorg(Borg):
    """Subclass with the overriden _shared_state."""
    _shared_state: Dict[str, Any] = {}

    def __init__(self, state: str = None) -> None:
        super().__init__()
        if state:
            self.state = state
        else:
            if not hasattr(self, "state"):
                self.state = "First init"
