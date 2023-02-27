import unittest
from collections import deque
from queue import PriorityQueue
from random import randint, sample

from src.queue.operations.comparison import greater, less
from src.queue.priority_heap import QueueElement, Heap


class PriorityTest(unittest.TestCase):

    def test_should_create_min_priority(self):
        test_size = 1000

        p_queue: PriorityQueue = PriorityQueue(test_size)
        p_heap: Heap = Heap(less)

        priority = sample([int(i) for i in range(10000)], 1000)
        for i in range(test_size):
            element: QueueElement = QueueElement(randint(0, 1000), priority[i])

            p_heap.push_element(element)
            p_queue.put((element.priority, element.element))

        for i in range(50):
            p_queue_element = p_queue.get()
            p_heap_element: QueueElement = p_heap.pop()
            self.assertEqual(p_heap_element.element, p_queue_element[1])
            self.assertEqual(p_heap_element.priority, p_queue_element[0])

    def test_should_create_max_priority(self):
        test_size = 1000

        p_queue: PriorityQueue = PriorityQueue(test_size)
        p_heap: Heap = Heap(greater)

        priority = sample([int(i) for i in range(10000)], 1000)
        for i in range(test_size):
            element: QueueElement = QueueElement(randint(0, 1000), priority[i])

            p_heap.push_element(element)
            p_queue.put((element.priority * -1, element.element))

        for i in range(50):
            p_queue_element = p_queue.get()
            p_heap_element: QueueElement = p_heap.pop()
            self.assertEqual(p_heap_element.element, p_queue_element[1])
            self.assertEqual(p_heap_element.priority * -1, p_queue_element[0])

    def test_should_create_min_priority_order_agnostic(self):
        test_size = 1000

        p_queue: PriorityQueue = PriorityQueue(test_size)
        values = deque()

        priority = sample([int(i) for i in range(10000)], test_size)
        for i in range(test_size):
            element: QueueElement = QueueElement(randint(0, 1000), priority[i])
            values.append(element)
            p_queue.put((element.priority, element.element))

        p_heap: Heap = Heap(less)
        new_sample = sample(values, len(values))
        self.assertEqual(len(p_queue.queue), len(new_sample))

        for i in new_sample:
            p_heap.push_element(i)

        print(new_sample)
        self.assertEqual(len(p_queue.queue), len(p_heap))

        for i in range(test_size):
            self.assertEqual(len(p_heap), len(p_queue.queue))
            p_queue_element = p_queue.get()
            p_heap_element: QueueElement = p_heap.pop()
            self.assertEqual(p_heap_element.element, p_queue_element[1])
            self.assertEqual(p_heap_element.priority, p_queue_element[0])


if __name__ == "__main__":
    unittest.TextTestRunner.run(unittest.TestLoader.loadTestsFromTestCase(PriorityTest))
