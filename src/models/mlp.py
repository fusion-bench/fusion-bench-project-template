import torch
from torch import nn


def create_mlp(input_dim: int, output_dim: int):
    """
    Create a simple MLP model.

    Args:
        input_dim (int): the input dimension
        output_dim (int): the output dimension

    Returns:
        nn.Module: the MLP model
    """
    model = nn.Sequential(
        nn.Linear(input_dim, 128),
        nn.ReLU(),
        nn.Linear(128, 64),
        nn.ReLU(),
        nn.Linear(64, output_dim),
    )
    return model
