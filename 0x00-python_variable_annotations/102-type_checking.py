#!/usr/bin/env python3
"""Type Checking"""


from typing import Tuple, List


def zoom_array(lst: Tuple[Any], factor: int = 2) -> Tuple[Any]:
    """Represents class zoom array"""
    zoomed_in: Tuple[Any] = tuple([
        item for item in lst
        for _ in range(factor)
    ])
    return zoomed_in


array = (13, 69, 90)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
