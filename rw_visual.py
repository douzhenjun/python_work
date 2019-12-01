#coding:utf-8

import matplotlib.pyplot as plt
from random_walk import RandomWalk

#build up a example of RandomWalk, and plot all its points
while True:
	#simulate random walking constantly unless the program is active
	rw = RandomWalk(500)
	rw.fill_walk()
	print("The coordinate of these points are:" + "\n")
	for i in range(0,rw.num_points):
		print("({},{})".format(rw.x_values[i],rw.y_values[i]), end = ',')
		if i % 5 == 0:
			print("\n")
			
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolor='none', s=15)
	#to stress the start_point and latest_point
	plt.scatter(0, 0, c='green', edgecolors='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
	
	plt.show()
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
