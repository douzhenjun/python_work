import scipy.misc
import matplotlib.pyplot as plt
import numpy as np

b = np.array([1,2,3])
print(b)

def get_indices(size):
	arr = np.arange(size)
	arr2 = []
	for i in arr:
		if i % 4 == 0:
			arr2.append(i)
	arr = np.array(arr2)
	return arr
			
