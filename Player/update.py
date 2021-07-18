from random import randrange

def update(self):
    self.center_x += self.change_x
    self.center_y += self.change_y
    
    # Figure out if we should face left or right
    if self.change_x < 0:
        self.texture = self.left_textures[0]
        self.face_right = False
    elif self.change_x > 0:
        self.texture = self.right_textures[0]
        self.face_right = True
    else:
        if self.face_right:
            self.texture = self.right_textures[randrange(1, 15)]
        else:
            self.texture = self.left_textures[randrange(1, 15)]

    # if self.change_x + self.change_y == 0:
    #    self.texture = self.textures[(randrange(2))] 
    # Check for out-of-bounds
    if self.left < 0:
        self.left = 0
    elif self.right > self.screen_width - 1:
        self.right = self.screen_width - 1

    if self.bottom < 0:
        self.bottom = 0
    elif self.top > self.screen_height - 1:
        self.top = self.screen_height - 1
