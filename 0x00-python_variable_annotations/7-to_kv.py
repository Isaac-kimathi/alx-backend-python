#!/usr/bin/env python3
"""module of type-annotated function"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """"function to Converts a key and its value to a tuple of the key and
        the square of its value"""
    return (k, float(v**2))

