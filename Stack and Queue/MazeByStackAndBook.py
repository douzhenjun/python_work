
from ex030102 import SequenceStack

class Maze():
	def __init__(self):
		self.directions = [(1,0),(0,1),(-1,0),(0,-1)]                   #the index set of four directions
		
		
	def PrintRoute(self, Exit, st):
		print("The route from entrance to exit is: ")
		print(Exit, end=' ')
		i = 1
		while st.IsEmptyStack() != True:
			print(st.PopStack(), end=' ')
			i = i + 1
			if i % 10 == 0:
				print()

	def PassedMark(self, mazeroute, position):
		mazeroute[position[0]][position[1]] = 2
		
		
	def IsPossiblePass(self, mazeroute, position):
		if mazeroute[position[0]][position[1]] == 0:
			return True
		return False
		
		
	def FindMazeRoute(self, mazeroute, Enter, Exit):
		st = SequenceStack()
		position = Enter
		nxt = 0
		while True:
			if position == Exit:
				self.PrintRoute(Exit, st)
				return 
			else:
				self.PassedMark(mazeroute, position)
				for i in range(nxt, 4):
					nextposition = (position[0]+self.directions[i][0],
					position[1]+self.directions[i][1])
					if self.IsPossiblePass(mazeroute, nextposition):
						st.PushStack((position, i+1))
						position = nextposition
						nxt = 0
						break
					else:
						while st.IsEmptyStack() and mazeroute[st.PopStack()[0][0]][st.PopStack()[0][1]] != 0:
							st.PopStack()
						if st.IsEmptyStack():
							break
						else:
							(position,nxt) = st.PopStack()
		print("There is no pass way in the maze!")
						
						
																
							
l = Maze()
mazeroute = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,1,1,0,0,0,1,0,0,0,1],[1,0,1,0,0,0,0,1,0,1,0,1,0,1],
		[1,0,1,0,1,1,1,1,0,1,0,1,0,1],[1,0,1,0,0,0,0,0,0,1,1,1,0,1],
		[1,0,1,1,1,1,1,1,1,1,0,0,0,1],[1,0,1,0,0,0,0,0,0,0,0,1,0,1],
		[1,0,0,0,1,1,1,0,1,0,1,1,0,1],[1,0,1,0,1,0,1,0,1,0,1,0,0,1],
		[1,0,1,0,1,0,1,0,1,1,1,1,0,1],[1,0,1,0,0,0,1,0,0,1,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
l.FindMazeRoute(mazeroute, (1,1), (10,12))								
