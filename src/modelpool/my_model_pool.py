from fusion_bench import BaseModelPool


class MLPModelPool(BaseModelPool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
