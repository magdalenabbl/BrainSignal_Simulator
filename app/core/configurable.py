# core/configurable.py


class Configurable:
    """
    Base class for runtime configuration injection.
    """

    def load_config(self, config: dict):
        """
        Load configuration parameters dynamically.
        """
        for key, value in config.items():
            setattr(self, key, value)