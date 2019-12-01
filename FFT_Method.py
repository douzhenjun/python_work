#FFT_method
import numpy as np
import cmath as c

p = 10
N = 2**p			
q = 1
dt = np.pi/4
A1_N = np.array([0 for x in range(N)], dtype = complex)		#用于存储初始Ak值，以及用于迭代生成A2_N
A2_N = np.array([0 for x in range(N)], dtype = complex)		#用于迭代生成A1_N，以及存储最终关于Ak的傅里叶变换fj

def f(x):
	# return np.cos(2*x)+np.sin(2*x)
	return 2*x**2-x-1


def A(k):
	return (f(k*dt)+f((k-N)*dt))*dt

A1_N = np.array([A(i) for i in range(N)], dtype = complex)
print("A1_N:\n", A1_N)


def W(x):
	return c.exp(complex(0, (-2*np.pi*x)/N))

list_W = np.array([W(i) for i in range(0, N)], dtype = complex)		#用于存储旋转因子W(下标为N，自变量为m，m从1到(N/2)-1),因为W^(N/2)=-1,所以
print("list_W:\n", list_W)											#W^x=-W^(x+N/2),所以它可以消除一半的乘法运算

q= 1

while q < p:
	if q % 2 == 1:
		for k in range(0, pow(2,p-q)):
			for j in range(0, pow(2,q-1)):
				A2_N[k*pow(2,q)+j] = A1_N[k*pow(2,q-1)+j] + A1_N[k*pow(2,q-1)+j+pow(2,p-1)]
				A2_N[k*pow(2,q)+j+pow(2,q-1)] = (A1_N[k*pow(2,q-1)+j]-A1_N[k*pow(2,q-1)+j+pow(2,p-1)])*W(k*pow(2,q-1))
		print("A2_N:\n", A2_N)
		q += 1  
	if q % 2 == 0:
		for k in range(0, pow(2,p-q)):
			for j in range(0, pow(2,q-1)):
				A1_N[k*pow(2,q)+j] = A2_N[k*pow(2,q-1)+j] + A2_N[k*pow(2,q-1)+j+pow(2,p-1)]
				A1_N[k*pow(2,q)+j+pow(2,q-1)] = (A2_N[k*pow(2,q-1)+j]-A2_N[k*pow(2,q-1)+j+pow(2,p-1)])*W(k*pow(2,q-1))
		print("A1_N:\n", A1_N)
		q += 1
		
if p % 2 == 0:
	A2_N = np.array([A1_N[i] for i in range(N)], dtype = complex)

print("A2_N:\n", A2_N)
