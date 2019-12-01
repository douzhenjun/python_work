#如何从数组中找出满足a+b=c+d的两个数对
#给定一个数组，找出数组中是否有两个数对(a,b),(c,d),使得a+b=c+d,其中a,b各不相同,c,d各不相同(a可能与c相同)
#如果有更多答案，打印出所有这样的结果(不允许a=b=c=d)。例如给定数组[3,4,7,10,20,9,8]，可以分别找到两个数对(3,8),(4,7)

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
				elements1 = (a[start], a[end])
				elements2 = (a[p], a[q])
				if elements2 not in run:				#如果待遍历的元素出现在run数组中，那么下一次再遇到时就忽视它，直接执行p+=1，q-=1
					print("We have found the corresponding pairwise elements, that is:({:d}, {:d}), ({:d}, {:d})"\
					.format(a[start],a[end],a[p],a[q])) #否则，则找到一组解，打印出来并把它以元组形式放到run数组中去，
					if elements1 not in run:			#注意，这里以待遍历元素(a[p],a[q])是否在run中作为条件判断而不是把待比较元素
						run.append(elements1)			#(a[start],a[end])是否在run中作为条件判断是因为如果那样做了，
														#就会导致遍历不到所有的结果，因为同一个和的解可能不止两对.而为了防止重复遍历
					run.append(elements2)				#才有了56行的if条件判断.
				p += 1
				q -= 1
		FindElementsPairs(a, start+1, end, run)
		FindElementsPairs(a, start, end-1, run)


if __name__ == "__main__":
	array = [3, 4, 7, 10, 20, 9, 8]
	array = [1, 6, 2, 5, 3, 9, 4]
	# array = [1, 2, 2, 2, 2, 6, 11]
	sorted_array = fastSortMethod(array, 0, 6)
	run = []									#设计了一个run数组，用于存放遍历到的匹配二元数组(a,b)，防止输出重复解，但又保证了输出所有结果
	FindElementsPairs(sorted_array, 0, 6, run)
	if len(run) == 0:
		print("There are not two pair of elements with the same sum.")
