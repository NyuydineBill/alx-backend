#!/usr/bin/env python3
"""
This module provides a Server class to
paginate a database of popular baby names.
"""

import csv
from typing import List
from 0-simple_helper_function import index_range


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
        """
        Retrieves a page of data from the dataset.

        :param page: The current page number (1-indexed)
        :param page_size: The number of items per page
        :return: A list of rows corresponding to the specified page
        """
        assert isinstance(page, int) and page > 0, "Page must be
        an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "Page size must
        be an integer greater than 0"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
