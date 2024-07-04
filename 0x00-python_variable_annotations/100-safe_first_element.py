#!/usr/bin/env python3
'''100-safe_first_element.py'''

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element of a sequence safely.

    Args:
      lst (Sequence[Any]): An input sequence of any type.

    Returns:
      Union[Any, None]: The first element of the sequence if it exists, otherwise None.
    """
    if lst:
      return lst[0]
    else:
      return None
