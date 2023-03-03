import unittest

from src.custom_deque.custom_deque import CustomDeque


class DequeTest(unittest.TestCase):

    def test_should_add_elements_front(self):
        deque = CustomDeque()

        elements_to_push = 1000

        for i in range(elements_to_push):
            deque.append_left(i)

        self.assertEqual(elements_to_push, len(deque))

    def test_should_remove_elements_front(self):
        deque = CustomDeque()

        elements_to_push = 1000

        for i in range(elements_to_push):
            deque.append_left(i)

        for i in range(elements_to_push):
            self.assertEqual(i, deque.remove_rear())

        self.assertEqual(0, len(deque))

    def test_should_remove_elements_rear(self):
        deque = CustomDeque()

        elements_to_push = 1000

        for i in range(elements_to_push):
            deque.append_right(i)

        print(deque)

        for i in range(elements_to_push):
            self.assertEqual(i, deque.remove_front())

        self.assertEqual(0, len(deque))

    def test_should_add_elements_rear(self):
        deque = CustomDeque()

        elements_to_push = 1000

        for i in range(elements_to_push):
            deque.append_right(i)

        self.assertEqual(elements_to_push, len(deque))

    def test_unique(self):
        deque = CustomDeque()

        deque.append_right(1)

        self.assertEqual(1, len(deque))
        self.assertEqual(1, deque.remove_front())
        self.assertEqual(0, len(deque))

        deque.append_left(1)
        self.assertEqual(1, len(deque))
        self.assertEqual(1, deque.remove_rear())
        self.assertEqual(0, len(deque))


if __name__ == "__main__":
    unittest.TextTestRunner.run(unittest.TestLoader.loadTestsFromTestCase(DequeTest))
