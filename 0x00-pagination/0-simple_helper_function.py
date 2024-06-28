#!/usr/bin/env python3
"""Time to do some pagination with this helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of start and end index for pagination.

    Args:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start and end index for the given page.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
