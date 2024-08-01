#!/usr/bin/env python3
""" Annotate """
from typing import Any, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Annotate """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[Any, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
