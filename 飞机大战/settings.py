#coding:utf_8
class Settings():
#存储《外星人入侵》的所有设置的类

	def __init__(self):
		#初始化游戏的设置
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		#飞船的设置
		self.ship_speed_factor = 5
		self.ship_limit = 5
		
		#子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 50
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 10
		
		#外星人设置
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#self.fleet_direction为1表示向右，为-1表示向左
		self.fleet_direction = 1
		self.alien_points = 50
		
		#speed up the game
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		'''when restart the game, initialize the speed of above objects'''
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		#fleet_direction be 1 means rightward,-1 means leftward
		self.fleet_direction = 1
			
			
	def increase_speed(self):
		'''this function aims to increase speed by multiple the speedup_scale'''
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
			
			
			
			
			
		
		
		
		
		
		
		
		
		
