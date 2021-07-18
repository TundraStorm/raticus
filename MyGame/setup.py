import arcade
from Player import Player

def setup(self):
    """ Set up the game and initialize the variables. """

    # Sprite lists
    self.player_list = arcade.SpriteList()

    # Set up the player
    self.player_sprite = Player("assets\character\idle\idle001.png", self.sprite_scalling,self.screen_width,self.screen_height)
    self.player_sprite.center_x = 50
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)
    #     # --- Load in a map from the tiled editor ---

    # CHARACTER_SCALING = 1
    # TILE_SCALING = 0.5
    # COIN_SCALING = 0.5
    # SPRITE_PIXEL_SIZE = 128
    # GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)
    # # Movement speed of player, in pixels per frame
    # PLAYER_MOVEMENT_SPEED = 10
    # GRAVITY = 1
    # PLAYER_JUMP_SPEED = 20

    # # Name of map file to load
    # map_name = ":resources:tmx_maps/test_map_1.tmx"
    # # Name of the layer in the file that has our platforms/walls
    # platforms_layer_name = 'Platforms'
    # # Name of the layer that has items for pick-up
    # coins_layer_name = 'Coins'

    # # Read in the tiled map
    # my_map = arcade.tilemap.read_tmx(map_name)

    # # -- Platforms
    # self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
    #                                                 layer_name=platforms_layer_name,
    #                                                 scaling=TILE_SCALING,
    #                                                 use_spatial_hash=True)

    # # -- Coins
    # self.coin_list = arcade.tilemap.process_layer(my_map, coins_layer_name, TILE_SCALING)

    # # --- Other stuff
    # # Set the background color
    # if my_map.background_color:
    #     arcade.set_background_color(my_map.background_color)

    # # Create the 'physics engine'
    # self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
    #                                                         self.wall_list,
    #                                                         GRAVITY)
                                                            

