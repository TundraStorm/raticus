import arcade
from Player import Player



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height,sprite_scalling,movement_speed, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)
        
        # Variables that will hold sprite lists
        self.player_list = None
        self.movement_speed = movement_speed
        self.sprite_scalling = sprite_scalling
        self.screen_height = height
        self.screen_width = width
        # Set up the player info
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)
    
    from .on_draw import on_draw
    from .on_key_press import on_key_press
    from .on_key_release import on_key_release
    from .on_update import on_update
    from .setup import setup