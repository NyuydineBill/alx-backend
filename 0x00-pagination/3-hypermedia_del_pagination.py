#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {}
            for i, row in enumerate(dataset):
                self.__indexed_dataset[i] = row
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a page of data from the dataset
        with hypermedia pagination information,
        resilient to deletions in the dataset.

        :param index: The start index of the return page
        :param page_size: The number of items per page
        :return: A dictionary containing pagination information
        """
        assert isinstance(index, int) and index >= 0, "Index
        must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "Page
        size must be an integer greater than 0"

        indexed_data = self.indexed_dataset()
        total_items = len(indexed_data)
        assert index < total_items, "Index out of range"

        data = []
        current_index = index
        count = 0

        while count < page_size and current_index < total_items:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                count += 1
            current_index += 1

        next_index = current_index if current_index < total_items else None

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index,
        }
