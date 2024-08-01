#!/usr/bin/env python3
""" Multiply """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multiply """
    return lambda x: x * multiplier
