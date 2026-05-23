# core/logger.py


class Logger:
    """
    Simple logging system for simulation debugging.
    """

    def log(self, message: str):
        print(f"[LOG] {message}")