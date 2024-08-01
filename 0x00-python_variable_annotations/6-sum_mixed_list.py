#!/usr/bin/env python3
""" Mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ Mixed list """
    sum:float = 0
    for x in mxd_lst:
        sum += float(x)
    return sum
