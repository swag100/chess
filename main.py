import pygame as pg

# CONSTANTS
BOARD_SIZE = (8, 8)

GRID_COLORS = ((234,236,209), (120,149,88))
GRID_SIZE = 64

WINDOW_SIZE = (GRID_SIZE*BOARD_SIZE[0], GRID_SIZE*BOARD_SIZE[1])\

# CLASSES
class Piece(pg.sprite.Sprite):
    def __init__(self, x, y):
        self._x, self._y = (x * GRID_SIZE, y * GRID_SIZE)
        print(self._x,self._y)

class Game(object):
    def __init__(self):
        self._over = False
        self._pieces = pg.sprite.Group()

        Piece(1,1)

    def handle_events(self):
        for event in pg.event.get(): 
            if event.type == pg.QUIT: self._over = True
    def update(self):
        pass
    def draw(self, screen):
        self._pieces.draw(screen)

def draw_board(screen):
    x, y = (0, 0)
    grid = ((False,True)*int(BOARD_SIZE[0]/2), (True,False)*int(BOARD_SIZE[0]/2)) * int(BOARD_SIZE[1]/2)
    for row in grid:
        for column in row:
            pg.draw.rect(screen, GRID_COLORS[int(column)], pg.Rect(x, y, GRID_SIZE, GRID_SIZE))
            if x < WINDOW_SIZE[0]-GRID_SIZE: x += GRID_SIZE
            else: x = 0
        y += GRID_SIZE

def main():
    pg.init()

    screen = pg.display.set_mode(WINDOW_SIZE) 
    pg.display.set_caption("Chess")

    clock = pg.time.Clock()
    game = Game()

    draw_board(screen)

    while not game._over:
        game.handle_events()
        game.update()
        game.draw(screen)
 
        # Pause for the next frame
        clock.tick(60)
        # Update the display.
        pg.display.flip()

main()