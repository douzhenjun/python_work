'''将一个p进制数转化为q进制数。首先把p进制数P转化成10进制数R，再把十进制数R转化成
q进制数Q.第一个只要不断对10先求余，再除以10，直到商为1为止。将每次求余得到的
数乘以p^(n)再相加，n从0到位数减1.第二个将R不断对q先求商再求余，直到商为0为止。
再将每次求得的余数倒序打印出来就可以了(或者每次乘以10的n次方再相加)。
'''
p = int(input("Please input the p:"))
q = int(input("Please input the q:"))
n = int(input("Please input the %d system number:" %p))
print("The original ",p," system number is:",n)
sum = 0
num = 0
product = 1
while n > 0:
	sum += n % 10 * product
	n = n // 10
	product = product * p

product = 1
while sum > 0:
	num += sum % 2 * product
	sum = sum // 2
	product = product * 10 
print("The present",q,"system number is:",num)	
