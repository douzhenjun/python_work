#利用递归思想解决迷宫问题

class Maze():
	def __init__(self):
		self.maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,1,1,0,0,0,1,0,0,0,1],[1,0,1,0,0,0,0,1,0,1,0,1,0,1],
		[1,0,1,0,1,1,1,1,0,1,0,1,0,1],[1,0,1,0,0,0,0,0,0,1,1,1,0,1],
		[1,0,1,1,1,1,1,1,1,1,0,0,0,1],[1,0,1,0,0,0,0,0,0,0,0,1,0,1],
		[1,0,0,0,1,1,1,0,1,0,1,1,0,1],[1,0,1,0,1,0,1,0,1,0,1,0,0,1],
		[1,0,1,0,1,0,1,0,1,1,1,1,0,1],[1,0,1,0,0,0,1,0,0,1,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
		self.entrance = (1,1)                                           #the index of the entrance
		self.end = (10,12)                                              #the index of the exit
		self.directions = [(1,0),(0,1),(-1,0),(0,-1)]                   #the index set of four directions
		
	def Mark(self, position):
		self.maze[position[0]][position[1]] = 2
		
	def IsPassable(self, position):
		if self.maze[position[0]][position[1]] == 0:
			return True
		return False
	
	
	# def PrintRoute(self, position):	
		# print("The pass way from exit to entrance is:")
		# n = 0
		# while n % 10 == 0:
			# print(position, end='')
			# n = n + 1
		# print()
		
		
	def FindPass(self, position, end):
		if position == self.end:
			print("The route from end to entrance is:",position, end='')
			return True
		else:
			for i in range(4):
				self.Mark(position)
				next_position = (position[0] + self.directions[i][0],
				 position[1] + self.directions[i][1])
				if self.IsPassable(next_position):
					if self.FindPass(next_position, end):
						print(position, end='')
						end = position
						return True
					else:
						print("There is no route from the entrance to the end.")
						return False
		
			
l = Maze()
l.FindPass((1,1), (10,12))			
					
			
			
		
		
		
		
		
		
		
		
