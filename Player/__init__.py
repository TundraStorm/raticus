import arcade
import glob
class Player(arcade.Sprite):
    from .update import update
    def __init__(self, image, scale,screen_height,screen_width):
        super().__init__()

        self.scale = scale
        self.textures = []
        self.screen_height = screen_height
        self.screen_width = screen_width
        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture(image)
        self.textures.append(texture)
        texture = arcade.load_texture(image,
                                      flipped_horizontally=True)
        self.textures.append(texture)
        texture = arcade.load_texture('assets/Raticus1.png')
        self.textures.append(texture)

        self.left_textures = [arcade.load_texture(file) for file in glob.glob('assets/character/idle/*.png', recursive=True)]
        self.right_textures =  [arcade.load_texture(file,flipped_horizontally=True) for file in glob.glob('assets/character/idle/*.png', recursive=True)]
        self.face_right = True
        # By default, face right.
        self.texture = texture
    
