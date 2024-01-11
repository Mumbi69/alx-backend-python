#!/usr/bin/env python3
"""Complex types - functions"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Represents the class make multiplier"""
    def multiplier_function(x: float) -> float:
        """Represents the class multiplier function"""
        return x * multiplier

    return multiplier_function
