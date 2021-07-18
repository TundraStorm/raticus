import arcade


SPRITE_SCALING = 0.25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5
TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1

from MyGame import MyGame


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT,SPRITE_SCALING,MOVEMENT_SPEED, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()