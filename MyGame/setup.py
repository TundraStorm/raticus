import arcade
from Player import Player

def setup(self):
    """ Set up the game and initialize the variables. """

    # Sprite lists
    self.player_list = arcade.SpriteList()

    # Set up the player
    self.player_sprite = Player("assets/Raticus12.png", self.sprite_scalling,self.screen_width,self.screen_height)
    self.player_sprite.center_x = 50
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)