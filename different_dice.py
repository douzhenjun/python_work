from die import Die

import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
hist = pygal.Bar()

hist.title = "Results of rolling at a D6 and a D10 50,000 times"
x_labels = []
for i in range(2,max_result+1):
	x_labels.append(i)	
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')
