import logging


class Logger:
    """
    Central logging system for simulation framework.
    """
#logger says what/when happened and if its an error or not
    def __init__(self, name: str = "BrainSignal"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO) #says INFO/WARNING/ERROR

        if not self.logger.handlers: # if there is still no output
            handler = logging.StreamHandler() # then write the logs in the console
            formatter = logging.Formatter(
                "[%(asctime)s] %(levelname)s - %(message)s"
            )
            # [2026-07-04 12:00:00] INFO - Simulation started
            handler.setFormatter(formatter) # use this format
            self.logger.addHandler(handler) # add it to the logger

    def info(self, msg: str):
        self.logger.info(msg)

    def warning(self, msg: str):
        self.logger.warning(msg)

    def error(self, msg: str):
        self.logger.error(msg)