class ExperimentManager:
    """
    Stores, runs, and compares simulation experiments.
    """

    def __init__(self):
        self.experiments = {}

    def create_experiment(self, name: str, config: dict):
        self.experiments[name] = {
            "config": config,
            "results": None
        }

    def save_results(self, name: str, results):
        if name in self.experiments:
            self.experiments[name]["results"] = results

    def get_experiment(self, name: str):
        return self.experiments.get(name)

    def list_experiments(self):
        return list(self.experiments.keys())