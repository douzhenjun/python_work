#建立一个关于考场学生的信息，对学生按照分数进行排名，输出学生姓名，考场号及其分数
data = []
fp = open("student_data.txt", "r")
student_data = fp.readlines()
fp.close()
for line in student_data:
	data.append(line.strip())

students = {}
score_id = []
score = 0
for i in range(1, len(data)-3, 5):
	score += int(data[i])
	score += int(data[i+1])
	score += int(data[i+2])
	score_id.append(score)
	score_id.append(data[i+3])
	students[data[i-1]] = score_id
	score = 0
	score_id = []

print("The original students data is: \n", students)

list_values = list(students.values())
for i in range(len(list_values)-1):
	for j in range(i+1, 0, -1):
		if list_values[j][0] > list_values[j-1][0]:
			list_values[j], list_values[j-1] = list_values[j-1], list_values[j]
		elif list_values[j][0] == list_values[j-1][0]:
			if list_values[j][1] < list_values[j-1][1]:
				list_values[j], list_values[j-1] = list_values[j-1], list_values[j]
		else:
			break

sorted_students = []
for j in list_values:
	for k in list(students.keys()):
		if students[k] == j:
			items = (k, j)
			sorted_students.append(items)
print("The sorted students data is: \n", sorted_students)
		
