import unittest
import time
from main import _min, _max, _sum, _mult
sample = [-3, 6, 32, 8592, -2384, 50, 294, 7583, -999]


class MyTestCase(unittest.TestCase):

    def test_min(self):
        start = time.time()
        assert _min(sample) == -2384
        print('Время работы функции _min -', time.time() - start)

    def test_max(self):
        start = time.time()
        assert _max(sample) == 8592
        print('Время работы функции _max -', time.time() - start)

    def test_sum(self):
        start = time.time()
        assert _sum(sample) == 13171
        print('Время работы функции _sum -', time.time() - start)

    def test_mult(self):
        start = time.time()
        assert _mult(sample) == -1313853316918448947200
        print('Время работы функции _mult -', time.time() - start)

    def mytest(self):
        assert_sum(sample) < _mult(sample)

    array = [i for i in range(500)]
    start = time.time()
    sum_def = array[0]
    for i in range(1, len(array)):
        sum_def += array[i]
    print(time.time() - start)




if __name__ == '__main__':
    unittest.main()
