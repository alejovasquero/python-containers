import unittest

from src.hash_table.hash_table import HashTable


class HashTableTest(unittest.TestCase):

    def test_should_store_elements(self):
        size = 20
        elements_to_push = 200

        table: HashTable = HashTable(size)
        for i in range(0, elements_to_push):
            table["item" + str(i)] = "value" + str(i)

            self.assertEqual(table[f"item{i}"], f"value{i}")

        self.assertEqual(elements_to_push, table.capacity)

    def test_should_delete_elements(self):
        size = 20
        elements_to_push = 1000

        table: HashTable = HashTable(size)
        for i in range(0, elements_to_push):
            table["item" + str(i)] = "value" + str(i)

        capacity = elements_to_push
        for i in range(elements_to_push - 3, -1, -1):
            del table["item" + str(i)]
            capacity -= 1
            self.assertEqual(None, table["item" + str(i)])
            self.assertEqual(capacity, table.capacity)

        self.assertIsNotNone(table[f"item{elements_to_push-1}"])
        self.assertIsNotNone(table[f"item{elements_to_push-2}"])