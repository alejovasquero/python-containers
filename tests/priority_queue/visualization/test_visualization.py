import unittest
from random import randint

from src.priority_queue.operations.comparison import less
from src.priority_queue.priority_heap import Heap, QueueElement
from src.priority_queue.visual.graph_visualization import draw_heap


class HeapTest(unittest.TestCase):

    def test_priority_queue_push(self):
        heap = Heap()

        for i in range(0, 25):
            value = randint(0, 1000)
            element = QueueElement(value, value)
            heap.push_element(element)

        draw_heap(heap)
