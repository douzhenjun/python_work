#coding:utf-8
class GameStats():
	'''statistical information of game tracing'''
	def __init__(self, ai_settings):
		'''initial the information'''
		self.ai_settings = ai_settings
		#flag is true when game is active
		self.game_active = False
		self.high_score = 0
		
		self.reset_stats()
		
		
	def reset_stats(self):
		'''initial the information which probably change during running the game'''
		self.ships_remain = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1

