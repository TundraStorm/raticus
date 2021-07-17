import arcade
def on_draw(self):
    """
    Render the screen.
    """
    # This command has to happen before we start drawing
    arcade.start_render()

    # Draw all the sprites.
    self.player_list.draw()