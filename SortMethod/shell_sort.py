import insert_sort as uu
SIZE = 8
def shell(data):
	jmp = SIZE // 2
	while jmp != 0:
		tmp = [[] for x in range(jmp)]
		for i in range(jmp):
			tmp[i].append(data[i])
			l = i + jmp
			while l < SIZE:
				tmp[i].append(data[l])
				l += jmp
			uu.insert(tmp[i])
		print(tmp)
		k = 0
		while k < SIZE:
			for j in range(len(tmp)):
				if len(tmp[j]) == 0:
					continue
				data[k] = tmp[j][0]
				tmp[j].remove(tmp[j][0])
				print(tmp)
				k += 1
		jmp = jmp // 2
	return data

if __name__ == "__main__":
	data = [63, 92, 27, 36, 45, 71, 58, 7]
	print("The original data is:\n", data)
	shell(data)
	print("The present data is:\n", data)

					
					
			
		
			
	
