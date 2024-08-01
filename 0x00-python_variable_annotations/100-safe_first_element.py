#!/usr/bin/env python3
""" Annotate """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Annotate """
    if lst:
        return lst[0]
    else:
        return None
