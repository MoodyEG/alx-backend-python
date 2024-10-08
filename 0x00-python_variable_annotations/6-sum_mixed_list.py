#!/usr/bin/env python3
""" Mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Mixed list """
    sum: float = 0.0
    for x in mxd_lst:
        sum += x
    return sum
