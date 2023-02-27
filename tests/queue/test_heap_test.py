import unittest
from collections import deque
from random import randint

from src.queue.operations.comparison import less, greater
from src.queue.priority_heap import Heap, QueueElement


class HeapTest(unittest.TestCase):

    def test_priority_queue_push(self):
        heap = Heap(greater)

        for i in range(0, 25):
            value = randint(0, 1000)
            element = QueueElement(value, value)
            heap.push_element(element)

        self.assert_max_heap_invariant_with_priority(heap, less)

    def assert_max_heap_invariant_with_priority(self, heap: Heap, comparator_func):
        heap_list = heap.list_data
        for j in range(1, len(heap_list)):
            left, right = j * 2, j * 2 + 1
            i = j - 1
            left -= 1
            right -= 1
            if heap_list[j] is not None:
                if left < len(heap_list) and heap_list[left] is not None:
                    self.assertTrue(comparator_func(heap_list[i], heap_list[left]) <= 0)
                if right < len(heap_list) and heap_list[right] is not None:
                    self.assertTrue(comparator_func(heap_list[i], heap_list[right]) <= 0)

    def test_should_create_heap_with_size(self):
        heap = Heap(14)
        self.assertEqual(0, len(heap.list_data))

        heap = Heap(10)
        self.assertEqual(0, len(heap.list_data))

        heap = Heap(25)
        self.assertEqual(0, len(heap.list_data))

        heap = Heap(1000)
        self.assertEqual(0, len(heap.list_data))

    def test_maintain_min_heap_invariant(self):
        heap = Heap(less)
        for i in range(0, 25):
            heap.push_element(randint(0, 1000))
        self.assert_min_heap_invariant(heap)

        heap = Heap(less)
        heap.push_element(1000)
        heap.push_element(1)
        self.assert_min_heap_invariant(heap)

        heap = Heap(less)
        for i in range(0, 1000):
            heap.push_element(randint(0, 1000))

        self.assert_min_heap_invariant(heap)

    def test_maintain_max_heap_invariant(self):
        heap = Heap(greater)
        for i in range(25):
            heap.push_element(randint(0, 1000))
        self.assert_max_heap_invariant(heap)

        heap = Heap(greater)
        heap.push_element(1000)
        heap.push_element(1)
        self.assert_max_heap_invariant(heap)

        heap = Heap(greater)
        for i in range(0, 1000):
            heap.push_element(randint(0, 1000))
        self.assert_max_heap_invariant(heap)

    def assert_min_heap_invariant(self, heap: Heap):
        for i in range(1, len(heap) + 1):
            if heap[i - 1] is not None:
                if 2 * i <= len(heap) and heap[2 * i - 1] is not None:
                    self.assertLessEqual(heap[i - 1], heap[2 * i - 1])
                if 2 * i + 1 <= len(heap) and heap[2 * i] is not None:
                    self.assertLessEqual(heap[i - 1], heap[2 * i])

    def assert_max_heap_invariant(self, heap: Heap):
        for i in range(1, len(heap) + 1):
            if heap[i - 1] is not None:
                if 2 * i <= len(heap) and heap[2 * i - 1] is not None:
                    self.assertGreaterEqual(heap[i - 1], heap[2 * i - 1])
                if 2 * i + 1 <= len(heap) and heap[2 * i] is not None:
                    self.assertGreaterEqual(heap[i - 1], heap[2 * i])

    def test_should_normalize_list_max(self):
        list = deque()
        for i in range(500):
            list.append(randint(0, 1000))

        for i in range(len(list) // 2, 0, -1):
            Heap.heapify(list, i, greater)

        self.assert_max_heap_invariant(list)

    def test_should_normalize_list_min(self):
        list = deque()
        for i in range(500):
            list.append(randint(0, 1000))

        for i in range(len(list) // 2, 0, -1):
            Heap.heapify(list, i, less)

        self.assert_min_heap_invariant(list)

    def test_should_pop_min(self):
        heap = Heap(less)
        initial_size = 500
        for i in range(initial_size):
            value = randint(0, 1000)
            heap.push_element(QueueElement(value, 500000 - value))

        for i in range(50):
            value = heap.pop()
            self.assert_min_heap_invariant(heap)
            initial_size -= 1
            self.assertEqual(initial_size, heap.current_size)
            for j in heap.list_data:
                self.assertLessEqual(value, j)

    def test_should_pop_max(self):
        heap = Heap(greater)
        initial_size = 500
        for i in range(initial_size):
            value = randint(0, 1000)
            heap.push_element(QueueElement(value, 500000 - value))

        for i in range(50):
            value = heap.pop()
            self.assert_max_heap_invariant(heap)
            initial_size -= 1
            self.assertEqual(initial_size, heap.current_size)
            for j in heap.list_data:
                self.assertGreaterEqual(value, j)


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(HeapTest))
