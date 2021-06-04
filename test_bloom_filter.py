from bloom_filter import BloomFilter
from partitioned_bloom_filter import PartitionedBloomFilter
from random import shuffle
import string
import random


def key_generator(size=6, chars=string.ascii_uppercase
                  + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def test_bloom_filter(bf, list_of_items):
    list_of_inserted_items = []

    for i in range(bf.num_of_items):
        bf.add(list_of_items[i])
        list_of_inserted_items.append(list_of_items[i])

    shuffle(list_of_items)

    False_Positive = 0
    True_Positive = 0
    for key in list_of_items[0:5000]:
        if bf.check(key):
            if key in list_of_inserted_items:
                True_Positive += 1
            else:
                False_Positive += 1

    return True_Positive, False_Positive


fp = 0.01

Bloom_f_1 = BloomFilter(false_positive_prob=fp, size=2 ** 10)

partitioned_Bloom_f_1 = PartitionedBloomFilter(
    false_positive_prob=fp, size=2 ** 10)

Bloom_f_2 = BloomFilter(false_positive_prob=fp, size=2 ** 12)

partitioned_Bloom_f_2 = PartitionedBloomFilter(
    false_positive_prob=fp, size=2 ** 12)

Bloom_f_3 = BloomFilter(false_positive_prob=fp, size=2 ** 16)

partitioned_Bloom_f_3 = PartitionedBloomFilter(
    false_positive_prob=fp, size=2 ** 16)


list_of_items = [key_generator() for _ in range(10000)]


True_Positive_1, False_Positive_1 = test_bloom_filter
(Bloom_f_1, list_of_items)Partitione_True_Positive_1, = test_bloom_filter(partitioned_Bloom_f_1, list_of_items)

True_Positive_2, False_Positive_2 = test_bloom_filter
(Bloom_f_2, list_of_items)Partitione_True_Positive_2,
Partitione_False_Positive_2 = test_bloom_filter(
    partitioned_Bloom_f_2, list_of_items)

True_Positive_3, False_Positive_3 = test_bloom_filter
(Bloom_f_3, list_of_items)Partitione_True_Positive_3,
Partitione_False_Positive_3 = test_bloom_filter(
    partitioned_Bloom_f_3, list_of_items)


print("Example of Original Bloom filter and Partitioned Bloom filter where m=2^10 ")

print("true positive lookups for Original Bloom Filter is {} %".format(True_Positive_1))
print("false positive lookups for Original Bloom filter is {} %".format(False_Positive_1))
print("Original Bloom filter false positive percentage: {}%".format(
    (False_Positive_1/97)*100))
print("true positive lookups for Partitioned Bloom filter is {} %".format(
    Partitione_True_Positive_1))
print("false positive lookups for Partitioned Bloom filter is {} %".format(
    Partitione_False_Positive_1))
print("Partitioned bloom filter false positive percentage: {}%".format(
    (Partitione_False_Positive_1/97)*100))

print("Example of Original Bloom filter and Partitioned Bloom filter where m=2^12")

print("true positive lookups for Original Bloom Filter is {} %".format(True_Positive_2))
print("false positive lookups for Original Bloom filter is {} %".format(False_Positive_2))
print("Original Bloom filter false positive percentage: {}%".format(
    (False_Positive_2/389)*100))
print("true positive lookups for Partitioned Bloom filter is {} %".format(
    Partitione_True_Positive_2))
print("false positive lookups for Partitioned Bloom filter is {} %".format(
    Partitione_False_Positive_2))
print("Partitioned bloom filter false positive percentage: {}%".format(
    (Partitione_False_Positive_2/389)*100))


print("Example of Original Bloom filter and Partitioned Bloom filter where m=2^16")

print("true positive lookups for Original Bloom Filter is {} %".format(True_Positive_3))
print("false positive lookups for Original Bloom filter is {} %".format(False_Positive_3))
print("Original Bloom filter false positive percentage: {}%".format(
    (False_Positive_3/6228)*100))
print("true positive lookups for Partitioned Bloom filter is {} %".format(
    Partitione_True_Positive_3))
print("false positive lookups for Partitioned Bloom filter is {} %".format(
    Partitione_False_Positive_3))
print("Partitioned bloom filter false positive percentage: {}%".format(
    (Partitione_False_Positive_3/6228)*100))
