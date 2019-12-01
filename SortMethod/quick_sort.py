data = [26, 3, 38, 1, 67, 8, 55, 14, 43, 18]

def quick_sort(d, size, lf, rg):		#lf, rg分别表示数组d的下标，只作为实参出现,lf作为默认的中间值下标，
										#找到第一个中间值下标以后，用rg_idx代替。if_idx和rg_idx分别从两个方向互相靠近，
	if lf < rg:							#当if_idx < rg_idx时，执行交换操作(要满足一定条件，这里不写了)。否则，将原来lf所在位置
		lf_idx = lf + 1					#与rg_idx所在位置交换，并且令lf = rg_idx,lf将原数组分成两部分，这两个部分在重复上述操作，
		while d[lf_idx] < d[lf]:		#直到从一开始的实参就显示lf >= rg为止。
			if lf_idx + 1 > size:
				break
			lf_idx += 1
		rg_idx = rg
		while d[rg_idx] > d[lf]:
			rg_idx -= 1
		while lf_idx < rg_idx:
			d[lf_idx], d[rg_idx] = d[rg_idx], d[lf_idx]
			lf_idx += 1
			while d[lf_idx] < d[lf]:
				lf_idx += 1
			rg_idx -= 1
			while d[rg_idx] > d[lf]:
				rg_idx -= 1
		d[lf], d[rg_idx] = d[rg_idx], d[lf]
	
		for i in range(size):
			print(d[i], end=" ")
		print()
	
		quick_sort(d, size, lf, rg_idx-1)	#以rg_idx为基准点分成左右两半，以递归方式分别为左右两半进行排序，直至完成排序
		quick_sort(d, size, rg_idx+1, rg)

quick_sort(data, 10, 0, 9)
