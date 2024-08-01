#!/usr/bin/env python3
""" Sum list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sum list """
    sum: float = 0.0
    for x in input_list:
        sum += x
    return sum
