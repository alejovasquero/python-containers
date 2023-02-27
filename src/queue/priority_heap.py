from __future__ import annotations

from collections import deque

from src.queue.operations.comparison import less


class QueueElement:
    priority: int

    def __init__(self, element, priority=1):
        self.priority = priority
        self.element = element

    def __str__(self):
        return "(" + str(self.element) + ", " + str(self.priority) + ")"

    def __lt__(self, other: QueueElement):
        return self.priority < other.priority

    def __gt__(self, other: QueueElement):
        return self.priority > other.priority

    def __le__(self, other: QueueElement):
        return self.priority <= other.priority

    def __ge__(self, other: QueueElement):
        return self.priority >= other.priority

    def __eq__(self, other: QueueElement):
        return self.priority == other.priority


class Heap:
    list_data: deque
    current_size: int
    comparator_func = None

    def __init__(self, comparator_func=None):
        self.list_data = deque()
        self.current_size = 0

        if comparator_func is None:
            self.comparator_func = less
        else:
            self.comparator_func = comparator_func

    def push_element(self, element: int):
        self.current_size += 1
        self.list_data.append(element)
        current_pointer = self.current_size

        movement_flag = current_pointer + 1
        while movement_flag != current_pointer and current_pointer != 1:
            movement_flag = current_pointer
            parent = int(current_pointer / 2)
            adjusted_parent = parent - 1
            adjusted_current = current_pointer - 1
            if self.comparator_func(self.list_data[adjusted_current], self.list_data[adjusted_parent]) == 1:
                self.swap(current_pointer, parent)
                current_pointer = parent

    @staticmethod
    def heapify(data_list: list, index, comparator_func):
        if index < len(data_list):
            right = index * 2 + 1
            left = index * 2
            swap_element = index

            if right <= len(data_list) and comparator_func(data_list[swap_element - 1], data_list[right - 1]) < 1:
                swap_element = right
            if left <= len(data_list) and comparator_func(data_list[swap_element - 1], data_list[left - 1]) < 1:
                swap_element = left

            if swap_element != index:
                data_list[swap_element - 1], data_list[index - 1] = data_list[index - 1], data_list[swap_element - 1]
                Heap.heapify(data_list, swap_element, comparator_func)

    def swap(self, a, b):
        temp = self.list_data[a - 1]
        self.list_data[a - 1] = self.list_data[b - 1]
        self.list_data[b - 1] = temp

    def __str__(self):
        string = "["
        for i in self.list_data:
            string += str(i) + ", "
        string += "]"
        return string

    def __len__(self):
        return self.current_size

    def __getitem__(self, key):
        return self.list_data[key]

    def pop(self) -> QueueElement:
        if self.current_size == 0:
            return None
        else:
            element = self.list_data[0]
            self.list_data[0] = self.list_data[self.current_size - 1]
            self.current_size -= 1
            self.heapify(self.list_data, 1, self.comparator_func)
            self.list_data.pop()
            return element
