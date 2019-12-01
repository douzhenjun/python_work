#如何实现LRU缓存方案

from collections import deque

class LRU:
	def __init__(self, cacheSize):
		self.cacheSize = cacheSize
		self.queue = deque()
		self.hashSet = set()
		
	def isQueueFull(self):		#判断缓存是否已满
		return len(self.queue) == self.cacheSize
		
	def enqueue(self, pageNum):
		if self.isQueueFull():
			self.hashSet.remove(self.queue[-1])
			self.queue.pop()
			
		self.queue.appendleft(pageNum)
		self.hashSet.add(pageNum)
		
	#当访问某一个page的时候会调用这个函数，对于访问的page有两种情况，
	#	1.如果page在缓存队列中，直接把这个结点移动到队首；
	#	2.如果page不在缓存队列中，把这个page缓存到队首。
	
	def accessPage(self, pageNum):
		#page不在缓存队列中，把它缓存到队首
		if pageNum not in self.hashSet:
			self.enqueue(pageNum)
		#page已经在缓存队列中了，移动到队首
		elif pageNum != self.queue[0]:
			self.queue.remove(pageNum)
			self.queue.appendleft(pageNum)
		
	def printQueue(self):
		while len(self.queue) > 0:
			print(self.queue.popleft())
			
if __name__ == "__main__":
	#假设缓存大小为3
	lru = LRU(3)
	lru.accessPage(1)
	lru.accessPage(2)
	lru.accessPage(5)
	lru.accessPage(6)
	lru.accessPage(7)
	#通过上面的访问序列后，缓存的信息为
	lru.printQueue()
