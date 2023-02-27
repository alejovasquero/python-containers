import datetime
from collections import deque
from queue import PriorityQueue
from random import randint
import pandas as pd
from numpy import greater

from src.queue.priority_heap import QueueElement, Heap


def take_algorithm_time(array, func):
    """
    Calculates the time taken for the algorithm to sort the array. The result is in microseconds

    Parameters
    ----------
        array : list
            The array for sorting
        sorting_algorithm : function
            Sorting algorithm to test
    Returns
    ----------
        list : int
            The median taken for the algorithm to sort the array (microseconds)
    """

    start_time = datetime.datetime.now()
    func()
    finish_time = datetime.datetime.now()
    full_time = finish_time - start_time
    return full_time.microseconds


def take_median_time_for_queue(queue_data):
    """
    Returns the median time for the sorting algorithm given

    Parameters
    ----------
        queue_data : list[list]
            The arrays for sorting
    Returns
    ----------
        list : int
            The median taken for the algorithm to sort the samples set
    """

    times = deque()

    for item in queue_data:
        full_push_time = deque()

        def push():
            queue: PriorityQueue = PriorityQueue()
            for value_to_push in item:
                queue.put(value_to_push)

        full_push_time.append(take_algorithm_time(item, push))
        times.append(full_push_time)

    df = pd.DataFrame(times)
    return df.median()


def take_median_time_for_heap(heap_data):
    """
    Returns the median time for the sorting algorithm given

    Parameters
    ----------
        heap_data : list[list]
            The arrays for sorting
    Returns
    ----------
        list : int
            The median taken for the algorithm to sort the samples set
    """

    times = deque()

    for item in heap_data:
        full_push_time = deque()

        def push():
            heap: Heap = Heap(greater)
            for value_to_push in item:
                heap.push_element(value_to_push)

        full_push_time.append(take_algorithm_time(item, push))
        times.append(full_push_time)

    df = pd.DataFrame(times)
    return df.median()


def get_push_data(queue_data, heap_data):
    """
    Returns the sorting time for a sample of arrays

    Parameters
    ----------
        samples : list[list]
            The array for sorting
    Returns
    ----------
        list : list
            A list with the time taken for heap_sort, shell_sort, radix_sort and the python sorted_sort
    """

    return [
        take_median_time_for_queue(queue_data),
        take_median_time_for_heap(heap_data)
    ]


def get_queue_push_time(samples, length, max_value=10000000):
    """
    Returns the time median time for the sorting algorithms with the defined parameters

    Parameters
    ----------
        samples : int
            The length of every array on the sample
        length : int
            The length of every array on the sample
        max_value : bool
            The maximum value for sorting
    Returns
    ----------
        list : list
            A list with the time taken for heap_sort, shell_sort, radix_sort and the python sorted_sort
    """

    samples_data_queue = deque()
    samples_data_heap = deque()
    for i in range(samples):
        queue_data, heap_data = get_random_list(length, max_value)
        samples_data_queue.append(queue_data)
        samples_data_heap.append(heap_data)
    return get_push_data(samples_data_queue, samples_data_heap)


def get_random_list(size, limit=10000000):
    """
    Returns a random list of values

    Parameters
    ----------
        size : int
            Size of the array
        limit : int
            Maximum value to be returned
    Returns
    ----------
        value : list
            List of random number, with size given
    """

    heap = deque()
    queue = deque()

    for i in range(size):
        value = randint(0, limit)
        queue.append((value, value))
        heap.append(QueueElement(value, value))
    return queue, heap
