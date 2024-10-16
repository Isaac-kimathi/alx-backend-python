#!/usr/bin/env python3
"""module for type-annotated function sum_mixed_list"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function to compute the sum of a list of integers and floating-point numbers."""
    return float(sum(mxd_lst))
