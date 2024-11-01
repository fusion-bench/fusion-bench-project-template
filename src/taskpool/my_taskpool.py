from fusion_bench import BaseTaskPool
from fusion_bench.taskpool.dummy import get_model_summary


class MyTaskPool(BaseTaskPool):
    def __init__(self, print_model_info: bool = True, **kwargs):
        self.print_model_info = print_model_info

    def evaluate(self, model) -> dict:
        if self.print_model_info:
            report = get_model_summary(model)
        else:
            report = {}
        return report
