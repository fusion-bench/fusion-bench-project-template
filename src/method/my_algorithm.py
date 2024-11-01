from fusion_bench import BaseAlgorithm, BaseModelPool
from torch import nn


class MyAlgorithm(BaseAlgorithm):
    def run(self, modelpool: BaseModelPool):
        """
        This method returns the pretrained model from the model pool.
        If the pretrained model is not available, it returns the first model from the model pool.

        Args:
            modelpool (BaseModelPool): The pool of models to fuse.

        Raises:
            AssertionError: If the model is not found in the model pool.
        """
        if isinstance(modelpool, nn.Module):
            return modelpool
        elif not isinstance(modelpool, BaseModelPool):
            modelpool = BaseModelPool(modelpool)

        model = modelpool.load_pretrained_or_first_model()

        assert model is not None, "Model is not found in the model pool."
        return model
