from collections import deque

from src.hash_table.hash_table import HashTable
from tests.hash_table.visualization.data.hashes import salt_hash, sha_hash_salt, normal_hash


def get_data_of_hash_with_samples(hash_func, samples: [()]):
    collisions = []

    for sample in samples:
        size = sample[0]
        elements_to_push = sample[1]
        table: HashTable = HashTable(size=size, hash_func=hash_func)

        for i in range(elements_to_push):
            table[f"key{i}"] = f"value{i}"

        collisions.append(table.collisions)

    return collisions


def get_data_of_hash_with_func(samples: [()], hash_funcs: []):
    data = []

    for func in hash_funcs:
        data.append(get_data_of_hash_with_samples(func, samples))

    return data


def get_all_data(min_hash_table_size, max_hash_table_size, elements):
    samples = deque()

    for size in range(min_hash_table_size, max_hash_table_size + 1):
        samples.append((size, elements))

    return get_data_of_hash_with_func(samples, [normal_hash, salt_hash, sha_hash_salt])
