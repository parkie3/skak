# skak spil der er bedre end patricks
import pygame as pg
from math import sqrt
s = 400
screen = pg.display.set_mode((s, s))
offset = s/64
Size = s/8

def distance(p1, p2):
    return sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)


def is_over(thing, pos):
    return True if thing.collidepoint(pos) else False

def is_over_circle(circle, pos):
    return True if circle.radius > distance(pos, circle.pos) else False

def grid_snap(pos):
    x = Size*round((pos[0]+Size/2)/Size)-Size/2
    y = Size*round((pos[1]+Size/2)/Size)-Size/2
    return x, y

# mouse class
class Mouse:

    def __init__(self, pos, l, r, hold):
        self.pos = pos
        self.l_click = l
        self.r_click = r
        self.holding = hold

    def update(self):
        if self.holding is not None:
            self.holding.pos = self.pos
            self.holding.selected = True

        if not self.l_click and self.holding is not None:
            self.holding.selected = False
            self.holding = None


class Piece:

    def __init__(self,pos,col,type,relpos):
        self.pos = pos
        self.size = Size
        self.radius = Size
        self.col = col
        self.type = type
        self.rect = pg.Rect(pos[0], pos[1], Size, Size)
        self.relpos = relpos
        self.selected = False


    #tegn stykker
    def drawp(self):
        #tegn cirkel ved position
        pg.draw.circle(screen, self.col,self.pos, s/20)
        #hvis sort, skal teksten være hvid og omvendt.
        if self.col == (255,255,255):
            img = font.render(self.type, True, (0, 0, 0))
        else:
            img = font.render(self.type, True, (255, 255, 255))
        #tegn tekst
        screen.blit(img, (self.pos[0]-offset, self.pos[1]-offset))

    def update(self):
        # grid snap
        if not self.selected:
            self.pos = grid_snap(self.pos)
            self.OGpos = self.pos


class Tile:

    def __init__(self, pos, size, color, name):
        self.pos = pos
        self.size = size
        self.color = color
        self.name = name
        self.rect = pg.Rect(pos[0], pos[1], size, size)

    def draw(self):
        pg.draw.rect(screen, self.color, self.rect)

#setup board
colors = [(196, 164, 132), (64, 47, 29)]

alf = ["a", "b", "c", "d", "e", "f", "g", "h"]
tiles = []

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
mouse = Mouse((0, 0), False, False, None)

running = True
pg.font.init()
#run window
while running:

    Mouse = pg.mouse.get_pos()
    font = pg.font.SysFont(None, 24)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse.l_click = True
            if event.button == 3:
                mouse.r_click = True
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                mouse.l_click = False

    screen.fill(255)

    mouse.pos = pg.mouse.get_pos()
    mouse.update()
    for piece in pieces:
        piece.update()
    if mouse.l_click:
        for piece in pieces:
            if is_over_circle(piece, mouse.pos):
                if mouse.holding != piece:
                    mouse.holding = piece
    # draw tiles
    for tile in tiles:
        tile.draw()

    for piece in pieces:
        piece.drawp()
    pt = ""
    #mouse over tiles
    for tile in tiles:
        if is_over(tile.rect, Mouse):
            for piece in pieces:
                if tile.pos == piece.relpos:
                    pt = piece.type
            text = str(pt) + tile.name
            print(text)
            img = font.render(text, True, (255, 50, 50))
            screen.blit(img, (Mouse[0]+15,Mouse[1]+10))



    pg.display.flip()

pg.display.quit()
pg.quit()
