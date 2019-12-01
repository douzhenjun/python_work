#f=cos(x),delt(t)=1,N=100
import cmath as c
import numpy as np
p = 10
N = 2**p
dt = np.pi/4
fj = 0

x = np.arange(0, N, 1)

def A(k):
	return (f(k*dt)+f((k-N)*dt))*dt
	# return f(2*np.pi*k/N)


def f(x):
	# return np.cos(2*x)+np.sin(2*x)
	return 2*x**2-x-1


list_A = A(x)
print("list_A:\n", list_A)

def w(x):
	return c.exp(complex(0, (-2*np.pi*x)/N))


list_fj = np.array([0 for x in range(N)], dtype = complex)	
for j in range(0, N):
	list_w = np.array([(w(i))**j for i in range(0, N)], dtype = complex)
	print(list_w)
	fj = np.dot(list_A, list_w)
	list_fj[j] = fj
print("list_fj:\n", list_fj)
