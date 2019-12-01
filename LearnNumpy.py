#This file is to learn numpy module
import numpy as np

print("In: a = arange(9).reshape(3,3)")
print("In: a")
a = np.arange(9).reshape(3, 3)
print(a)

print("In: b")
b = 2 * a
print(b)

print("In: hstack(a, b)")
c = np.hstack((a, b))
print("In: c")
print(c)

c = np.vstack((a,b))
print("In: c = np.vstack((a,b))")
print("In: c")
print(c)
c = np.concatenate((a,b), axis=0)
print(c)

print("In: c = dstack((a,b))")
print("In: c")
c = np.dstack((a,b))
print(c)

print("In: c = column_stack()")
print("In: c")
c = np.column_stack((a,b))
print(c)

b = np.arange(24).reshape(2, 12)
print("In: b")
print(b)

print("In: b.ndim")
print(b.size)

print("In: b.nbytes")
print(b.nbytes)
print("In: b.size * b.itemsize")
print(b.size * b.itemsize)

print("In: b = array([1.j + 1, 2.j + 3])")
b = np.array([1.j + 1, 2.j + 3])
print(b)
print("In: b.dtype")
print(b.dtype)
print("b = arange(4).reshape(2,2))")
print("In: b")
b = np.arange(4).reshape(2,2)
print(b)
f = b.flat
print("In: f")
print(f)
for item in f:
	print(item)
