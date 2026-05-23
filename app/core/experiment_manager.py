# core/experiment_manager.py

from core.serializable import Serializable


class ExperimentManager(Serializable):
    """
    Manages simulation experiments lifecycle.
    """

    def __init__(self):
        self.experiments = []

    def create_experiment(self, config: dict):
        self.experiments.append(config)

    def list_experiments(self):
        return self.experiments

    # Serialization
    def to_dict(self):
        return {"experiments": self.experiments}

    def from_dict(self, data: dict):
        self.experiments = data.get("experiments", [])