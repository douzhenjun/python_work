#KMP算法
#与朴素的字符串匹配算法不同,KMP算法在每一次匹配失败后追踪到匹配失败的那个点在模式串里的位置,并构造一个ListNext[]用于存储模式串在当前
#位置j与主串匹配失败后应当移到的位置.这避免了朴素匹配逐一排查的低效率,更快地得到匹配结果.
from BF_algorithm import StringList


M = StringList()
M.CreateStringByInput()
print("The main string is:",M.GetString())
T = StringList()
T.CreateStringByInput()
print("The target string is:",T.GetString())
pos = int(input("Please input the index of seats from where to seek first: "))
print("The result depends on the value of ListNext: ")
M.IndexKMP(pos, T, T.GetListNext())
print("The result depends on the value of ListNextValue: ")
M.IndexKMP(pos, T, T.GetListNextValue())




