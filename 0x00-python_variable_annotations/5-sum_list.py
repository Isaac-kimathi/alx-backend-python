#!/usr/bin/env python3
"""module for type-annotated function sum_list"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """function that computes the sum of a list of floating-point numbers"""
    return float(sum(input_list))
