#!/usr/bin/env python3
""" Sum list """


def sum_list(input_list: list[float]) -> float:
    """ Sum list """
    sum:float = 0
    for x in input_list:
        sum += x
    return sum
