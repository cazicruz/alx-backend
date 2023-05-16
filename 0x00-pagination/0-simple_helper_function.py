#!/usr/bin/env python3
""" pagination in python"""


def index_range(page: int, page_size: int) -> tuple(int, int):
    """The function should return a tuple of size two containing
    a start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination
    parameters."""
    end = page * page_size
    start = end - page_size
    return(start, end)
