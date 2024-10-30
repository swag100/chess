import pygame as pg

# CONSTANTS
WINDOW_SIZE = (512, 512)
GRID_COLORS = ((234,236,209), (120,149,88))
PATTERN = ((False,True)*4, (True,False)*4) *4

# CLASSES
class Game(object):
    def __init__(self):
        self.over = False
        self.sprites_list = pg.sprite.Group()


    def handle_events(self):
        for event in pg.event.get(): 
            if event.type == pg.QUIT: self.over = True
    def update(self):
        pass
    def draw(self, screen):
        screen.fill(GRID_COLORS[0]) 
        pg.display.flip()

def main():
    pg.init()

    screen = pg.display.set_mode(WINDOW_SIZE) 
    pg.display.set_caption("Chess")

    clock = pg.time.Clock()
    game = Game()

    while not game.over: 
        game.handle_events()
        game.update()
        game.draw(screen)
 
        # Pause for the next frame
        clock.tick(60)

main()