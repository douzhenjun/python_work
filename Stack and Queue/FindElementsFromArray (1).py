#如何从数组中找出满足a+b=c+d的两个数对
#给定一个数组，找出数组中是否有两个数对(a,b),(c,d),使得a+b=c+d,其中a,b,c,d各不相同
#如果有更多答案，打印出其中一个就可以了。例如给定数组[3,4,7,10,20,9,8]，可以分别找到两个数对(3,8),(4,7)

def fastSortMethod(array, start, end):
	if start < end:
		temp = array[start]
		ptr = start
		qtr = end
		while ptr < qtr:
			while array[ptr] < temp or array[ptr] == temp:
				ptr += 1
				if ptr == end:
					break
			while array[qtr] > temp:
				qtr -= 1
			if ptr < qtr:
				array[ptr], array[qtr] = array[qtr], array[ptr]
		array[start], array[qtr] = array[qtr], array[start]
		print(array)
		fastSortMethod(array, start, qtr-1)
		fastSortMethod(array, qtr+1, end)
	return array


def FindElementsPairs(a, start, end, run):
	if start < end:
		p = start
		q = end
		targetValue = a[start] + a[end]
		p += 1
		q -= 1
		
		while a[p] == a[start]:
			p += 1
			if p == q:
				break

		while a[q] == a[end]:
			q -= 1
			if q == p:
				break

		while p < q:
			value = a[p] + a[q]
			if value > targetValue:
				q -= 1
			elif value < targetValue:
				p += 1
			else:
				elements = (a[start], a[end])
				print("We have found the corresponding pairwise elements, that is:({:d}, {:d}), ({:d}, {:d})"\
				.format(a[start],a[end],a[p],a[q])) 
				run.append(elements)
				return

		if len(run) == 0:
			FindElementsPairs(a, start+1, end, run)
			FindElementsPairs(a, start, end-1, run)


if __name__ == "__main__":
	array = [3, 4, 7, 10, 20, 9, 8]
	# array = [1, 2, 2, 2, 2, 6, 11]
	sorted_array = fastSortMethod(array, 0, 6)
	run = []									#设计了一个run数组，用于存放遍历到的匹配二元数组(a,b)，防止输出重复解，但又保证了输出所有结果
	FindElementsPairs(sorted_array, 0, 6, run)
	if len(run) == 0:
		print("There are not two pair of elements with the same sum.")
