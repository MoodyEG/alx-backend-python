#!/usr/bin/env python3
""" Tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
	""" Tuple """
	return (k, v**2)
