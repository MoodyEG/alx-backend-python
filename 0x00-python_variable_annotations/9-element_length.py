#!/usr/bin/env python3
""" Annotate """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Annotate """
    return [(i, len(i)) for i in lst]
