import arcade

def on_key_press(self, key, modifiers):
    """Called whenever a key is pressed. """

    # If the player presses a key, update the speed
    if key == arcade.key.UP:
        self.player_sprite.change_y = 7
        #self.player_sprite.change_y = -MOVEMENT_SPEED*0.5
    elif key == arcade.key.DOWN:
        self.player_sprite.change_y = 0#-MOVEMENT_SPEED
    elif key == arcade.key.LEFT:
        self.player_sprite.change_x = - self.movement_speed
    elif key == arcade.key.RIGHT:
        self.player_sprite.change_x = self.movement_speed
