import math
import mmh3
from bitarray import bitarray


class PartitionedBloomFilter():
    def __init__(self, num_of_items=None, false_positive_prob=None, size=None):
        self.num_of_hash_fun = 4
        self.false_positive_prob = false_positive_prob
        if num_of_items is None:
            self.num_of_items = self.get_number_of_inserts_for_given_fp_rate(size, false_positive_prob, self.num_of_hash_fun)
            self.size = size
        elif size is None:
            self.size = self.get_size(num_of_items, false_positive_prob)
            self.num_of_items = num_of_items

        self.partition_size = int(self.size / self.num_of_hash_fun)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.num_of_hash_fun):
            digest = mmh3.hash(item, i) % self.partition_size
            self.bit_array[i * self.partition_size + digest] = True

    def check(self, item):
        for i in range(self.num_of_hash_fun):
            digest = mmh3.hash(item, i) % self.partition_size
            if not self.bit_array[i * self.partition_size + digest]:
                return False
        return True

    @classmethod
    def get_number_of_inserts_for_given_fp_rate(cls, m, fp, k):
        n = (m / (-k / math.log(1 - math.exp(math.log(fp) / k))))
        return int(n)

    @classmethod
    def get_size(cls, n, fp):
        size = -(n * math.log(fp)) / (math.log(2) ** 2)
        return int(size)

    @classmethod
    def get_num_of_hash_fun(cls, m, n):
        k = (m / n) * math.log(2)
        return int(k)