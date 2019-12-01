from button import Button 
import pygame.font

class ButtonB(Button):
	def __init__(self, ai_settings, screen, msg):
		'''initial the attribute of button'''
		super().__init__(ai_settings, screen, msg)
	
	def prep_msg(self, msg):
		'''let msg be a image and in the center of the button'''
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
