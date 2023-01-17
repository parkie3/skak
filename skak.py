# skak spil der er bedre end patricks
import pygame as pg
import random as rn
s = 400
screen = pg.display.set_mode((s, s))



def is_over(thing, pos):
    return True if thing.collidepoint(pos) else False

class Piece:

    def __init__(self,pos,col,type,relpos):
        self.pos = pos
        self.col = col
        self.type = type
        self.relpos = relpos
    offset = 15
    def drawp(self):
        pg.draw.circle(screen, self.col,self.pos, s/16)
        if self.col == (255,255,255):
            img = font.render(self.type, True, (0, 0, 0))
        else:
            img = font.render(self.type, True, (255, 255, 255))
        print(self.pos)
        print(type(self.pos))
        screen.blit(img, self.pos)

class Tile:

    def __init__(self, pos, size, color, name):
        self.pos = pos
        self.size = size
        self.color = color
        self.name = name
        self.rect = pg.Rect(pos[0], pos[1], size, size)

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect)


colors = [(196, 164, 132), (64, 47, 29)]

alf = ["a", "b", "c", "d", "e", "f", "g", "h"]
tiles = []
Size = s/8

for i in range(8):
    for j in range(8):
        col = colors[(j+i)%2]
        n = f"{alf[i]}{8-j}"
        tiles.append(Tile((i*Size, j*Size), Size, col, n))

pieces = []
piecesdata = "RNBQKBNRPPPPPPPP                                PPPPPPPPRNBQKBNR"
count = 0
for i in range(8):
    for j in range(8):
        if 0<=i<=2:
            col = (0, 0, 0)
        else:
            col = (255, 255, 255)
        type_ = piecesdata[count]
        count +=1
        if type_ ==" ":
            pass
        else:
            pieces.append(Piece((j*Size+Size/2,i*Size+Size/2),col, type_,(j*Size, i*Size)))

print(pieces[0].pos and tiles[0].pos)
running = True
pg.font.init()
while running:
    font = pg.font.SysFont(None, 24)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    screen.fill(255)

    mouse = pg.mouse.get_pos()
    # draw tiles
    for tile in tiles:
        tile.draw()

    for piece in pieces:
        piece.drawp()
    pt = ""
    #mouse over tiles
    for tile in tiles:
        if is_over(tile.rect, mouse):
            for piece in pieces:
                if tile.pos == piece.relpos:
                    pt = piece.type
            text = str(pt) + tile.name
            print(text)
            img = font.render(text, True, (255, 50, 50))
            screen.blit(img, (mouse[0]+15,mouse[1]+10))



    pg.display.flip()

pg.display.quit()
pg.quit()
