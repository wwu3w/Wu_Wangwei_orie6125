
from hw2problem2 import max_subarray
import numpy as np


alist = ['a','a','z','z','a']
assert np.all(max_subarray(alist) == [[0,3],[1,4]])

print('This test is completed')