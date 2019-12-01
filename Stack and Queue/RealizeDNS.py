#如何实现反向DNS查找缓存
#反向DNS查找指的是使用Internet IP 地址查找域名。例如，如果你在浏览器中输入74.125.200.106,它会自动重定向到google.com
#如何实现反向DNS查找缓存？

#分析与解答：要想实现反向DNS查找缓存，主要需要完成如下的功能:
#			(1)将IP地址添加到缓存中的URL映射
#			(2)根据给定IP地址查找对应的URL

class TrieNode:
	def __init__(self):
		CHAR_COUNT = 11
		self.isLeaf = False
		self.url = None
		self.child = [None] * CHAR_COUNT
		i = 0
		while i < CHAR_COUNT:
			self.child[i] = None
			i += 1
			
def getIndexFromChar(c):
	return 10 if c == "." else (ord(c) - ord("0"))

def getCharFromIndex(i):
	return "." if i == 10 else ("0" + str(i))
	
class DNSCache:
	def __init__(self):
		self.CHAR_COUNT = 11
		self.root = TrieNode()
		
	def insert(self, ip, url):
		lens = len(ip)
		pCrawl = self.root
		level = 0
		while level < lens:
			index = getIndexFromChar(ip[level])
			if pCrawl.child[index] == None:
				pCrawl.child[index] = TrieNode()
			pCrawl = pCrawl.child[index]
			pCrawl.isLeaf = True
			pCrawl.url = url
			level += 1
			
	def searchDNSCache(self, ip):
		pCrawl = self.root
		lens = len(ip)
		level = 0
		while level < lens:
			index = getIndexFromChar(ip[level])
			if pCrawl.child[index] == None:
				return None
			pCrawl = pCrawl.child[index]
			level += 1
		if pCrawl != None and pCrawl.isLeaf:
			return pCrawl.url
		return None
		
if __name__ == "__main__":
	ipAdds = ["10.57.11.127", "121.57.61.129", "66.125.100.103"]
	url = ["www.samsung.com", "www.samsung.net", "www.google.in"]
	n = len(ipAdds)
	cache = DNSCache()
	for i in range(n):
		cache.insert(ipAdds[i], url[i])
		i += 1
	ip = "121.57.61.129"
	res_url = cache.searchDNSCache(ip) 
	if res_url != None:
		print("找到了IP对应的URL:\n"+ip+"--->"+res_url)
	else:
		print("没有找到对应的URL\n")
	
	
		
		
		
		
		
		
		
		
		
