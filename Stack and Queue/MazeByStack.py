#采用回溯法求解迷宫问题
from SequenceStack import SequenceStack

class Maze():
	def __init__(self):
		# self.maze = [[1,1,1,1,1,1,0,1,1,1],[1,0,0,0,0,1,0,1,1,1],
					# [1,0,1,1,0,1,0,0,0,1],[1,0,1,1,0,1,1,1,0,1],
					# [1,0,1,1,0,0,0,0,0,1],[1,0,1,1,0,1,1,1,1,1],
					# [1,0,1,1,0,0,0,0,0,1],[1,0,1,1,1,1,1,1,1,1],
					# [1,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]]	
		# self.entrance = (0,6)                                           #the index of the entrance
		# self.exit = (8,9)                                               #the index of the exit
		# self.directions = [(1,0),(0,1),(-1,0),(0,-1)]                   #the index set of four directions
		
		self.maze = [[1,1,1,1,1,0,0,0,1],[1,1,1,1,0,1,1,0,1],
					[1,1,0,0,0,0,0,0,1],[1,0,0,1,0,0,0,0,1],
					[1,0,1,0,0,0,1,0,1],[1,1,1,1,0,1,0,0,1]]
		self.entrance = (0,5)
		self.exit = (5,7)
		self.directions = [(1,0),(0,1),(-1,0),(0,-1)]
		# self.maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		# [1,0,0,0,1,1,0,0,0,1,0,0,0,1],[1,0,1,0,0,0,0,1,0,1,0,1,0,1],
		# [1,0,1,0,1,1,1,1,0,1,0,1,0,1],[1,0,1,0,0,0,0,0,0,1,1,1,0,1],
		# [1,0,1,1,1,1,1,1,1,1,0,0,0,1],[1,0,1,0,0,0,0,0,0,0,0,1,0,1],
		# [1,0,0,0,1,1,1,0,1,0,1,1,0,1],[1,0,1,0,1,0,1,0,1,0,1,0,0,1],
		# [1,0,1,0,1,0,1,0,1,1,1,1,0,1],[1,0,1,0,0,0,1,0,0,1,0,0,0,1],
		# [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
		# self.entrance = (1,1)                                           #the index of the entrance
		# self.exit = (10,12)                                             #the index of the exit
		# self.directions = [(1,0),(0,1),(-1,0),(0,-1)]                   #the index set of four directions
	
	#注意这是倒序打印	
	def PrintRoute(self, st):
		print("The route from exit to entrance is: ")
		i = 0
		while st.IsEmptyStack() != True:
			print(st.PopStack(), end=' ')
			i = i + 1
			if i % 10 == 0:
				print()
	
	#将已走过的位置的元素标记为非零
	def Mark(self, position):
		self.maze[position[0]][position[1]] = 2
		
		
	def IsPassable(self, position):
		if self.maze[position[0]][position[1]] == 0:
			return True
		return False
		
		
	def FindPass(self):
		ss = SequenceStack()
		position = self.entrance
		ss.PushStack(position)
		while True:
			if position == self.exit:
				self.PrintRoute(ss)
				return
			else:
				if self.IsPassable(position):
					tag = False
				self.Mark(position)
				n = 1
				for i in range(4):
					next_position = (position[0] + self.directions[i][0],
					position[1] + self.directions[i][1])
					if self.IsPassable(next_position):
						ss.PushStack(next_position)
						if tag == True:
							ss.PopStack()
							ss.PushStack(position)
							ss.PushStack(next_position)
						position = next_position
						break
					else:
						n = n + 1
				if n == 5:
					if ss.IsEmptyStack():
						break
					else:
						position = ss.PopStack()
						tag = True
		print("There is no pass way in the maze!")
					
					
			
l = Maze()
l.FindPass()								
					
					
					
					
					
		
		
		
		
		
		
		
		
		
		
		
		
