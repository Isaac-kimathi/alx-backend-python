#!/usr/bin/env python3
"""module for type-annotated function"""
from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that takes in arguments of iterable sequence"""
    return [(item, len(item)) for item in lst]
