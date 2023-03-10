# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['foo', 'bar', 'HelloSayer', 'preprocess']

# %% ../nbs/00_core.ipynb 2
import torch
from typing import Dict, List

# %% ../nbs/00_core.ipynb 4
def foo(): pass

# %% ../nbs/00_core.ipynb 5
def bar(name: str, country:str) -> str:
    r"""
    Represents a textual description of the bar.
    
    Parameters
    ----------
    name
        the name of the bar
    country
        the name of the country
        
    Returns
    -------
    The description
    """
    
    return f"{name}'s bar"

# %% ../nbs/00_core.ipynb 7
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): self.to = to
        
    def say(self):
        "Do the saying"
        return say_hello(self.to)

# %% ../nbs/00_core.ipynb 9
def preprocess(self, batch_data: List[Dict[str, bytearray]]) -> torch.Tensor:
    r"""
    Transform raw input into model input data zzz.

    Parameters
    ----------
    batch_data (`List[Dict[str, bytearray]]`)
        The batched list of raw input images.

    Returns
    -------
    The preprocessed inout images as `torch.Tensor` 
    """
    ...
