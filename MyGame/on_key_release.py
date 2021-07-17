import arcade

def on_key_release(self, key, modifiers):
    """Called when the user releases a key. """

    # If a player releases a key, zero out the speed.
    # This doesn't work well if multiple keys are pressed.
    # Use 'better move by keyboard' example if you need to
    # handle this.
    
    if key == arcade.key.UP or key == arcade.key.DOWN:
        self.player_sprite.change_y = -2.5
    elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
        self.player_sprite.change_x = 0