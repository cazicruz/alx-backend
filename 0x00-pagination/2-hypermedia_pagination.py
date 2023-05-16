#!/usr/bin/env python3
"""pagination from a .csv file"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The function should return a tuple of size two containing
    a start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination
    parameters."""
    end = page * page_size
    start = end - page_size
    return(start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ a method named get_page that takes two integer
        arguments page with default value 1 and page_size
        with default value 10"""
        assert (page > 0 and isinstance(page, int))
        assert (page_size > 0 and isinstance(page_size, int))

        dataset = self.dataset()
        try:
            indexes = index_range(page, page_size)
            return dataset[indexes[0]:indexes[1]]
        except IndexError:
            return []

     def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a page of the dataset.
        Args:
            page (int): The page number.
            page_size (int): The page size.
        Returns:
            dict : The page of the dataset.
        """
        total_pages = len(self.dataset()) // page_size 
        total_pages = math.ceil(total_pages)
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return info
