from abc import ABC


class Configurable(ABC):
    """
    Mixin for components that can be configured via dict/JSON.
    """

    def load_config(self, config: dict):
        self.config = config

    def save_config(self) -> dict:
        return getattr(self, "config", {}) # if there is self.config->returns it; if there is not-> returns {}