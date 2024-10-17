#!/usr/bin/env python3
"""module of type-annotated function make_multiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
