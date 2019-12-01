#贪心算法
#假设有三种月饼，库存量分别为18，15，10万吨，总售价分别为75，72，45亿元，市场最大需求是20万吨，那么最大收益策略应该如何确定？

def sort_method(moonlist):
	if len(moonlist) == 0:
		return
	for i in range(len(moonlist)-1):
		for j in range(i+1, 0, -1):
			moonlist[j].price = moonlist[j][1]/moonlist[j][0]
			if moonlist[j].price > moonlist[j-1].price:
				moonlist[j-1],moonlist[j] = moonlist[j],moonlist[j-1]

moonlist = []
while True:
	co = input("Do any another mooncakes remain?(Yes/Enter, No/n)")
	if co == "n":
		break
	store = float(input("Please input the store of this cake:(units:ten thousand tons)"))
	sell = float(input("Please input the total sell price of this cake:(units:ten thousand RMB)"))
	cake = (store, sell)
	moonlist.append(cake)
sort_method(moonlist)
md = float(input("Please input the total market demand for the number of cakes:(units: tenthousand tons)"))
profit = 0
while md > 0:
	for i in range(len(moonlist)-1):
		if md >= moonlist[i][0]:
			profit += moonlist[i][1]
			md -= moonlist[i][0]
		else:
			profit += (moonlist[i].sell/moonlist[i].store)*md
			md = 0
print("The largest profit is:", profit, "(ten thousand RMB).")
		
	


		
		
	
