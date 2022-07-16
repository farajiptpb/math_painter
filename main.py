import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, ypix, xpix, bgcolor):
        self.ypix = ypix
        self.xpix = xpix
        self.bgcolor = bgcolor

    def draw(self):

        z = np.zeros((self.ypix, self.xpix, 3), dtype=np.uint8)
        if self.bgcolor == 'white':
            z[:] = [500]
        else:
            pass

        for i in recs:
            z[i.origen_y:i.origen_y + i.height, i.origen_x:i.origen_x + i.width] = i.color

        for u in sqs:
            z[u.origen_y:u.origen_y + u.side, u.origen_x:u.origen_x + u.side] = u.color

        img = Image.fromarray(z, 'RGB')
        img.save('shapes.png')


class Rectangle:

    def __init__(self, upper_left, width, height, color):
        self.origen_y = upper_left[0]
        self.origen_x = upper_left[1]
        self.width = width
        self.height = height
        self.color = color


class Square:

    def __init__(self, upper_left, side, color):
        self.origen_y = upper_left[0]
        self.origen_x = upper_left[1]
        self.side = side
        self.color = color


ypix = int(input('Enter ypix: '))
xpix = int(input('Enter xpix: '))
bgcolor = input('background color: white or black : ')
recs = []
sqs = []


while True:
    rec_or_sq = input('what is the shape: rectangle or square:')

    if rec_or_sq.lower() == 'rectangle':
        rec = Rectangle(upper_left=(int(input('enter y of rec: ')), int(input('enter x of rec: ')))\
                        , width=int(input('enter width of rec: ')), height=int(input('enter height of rec: ')),\
                        color=(int(input('red color : ')), int(input('green color : ')), int(input('blue color : '))))
        recs.append(rec)
    else:
        sq = Square(upper_left=(int(input('enter y of square: ')), int(input('enter x of square: ')))\
                    , side=int(input('enter side of square: ')),\
                    color=(int(input('red color: ')), int(input('green color: ')), int(input('blue color: '))))
        sqs.append(sq)

    quit_ask = input('add shape or quit? : ')
    if quit_ask.lower() == 'quit':
        print(recs)
        print(sqs)
        break
    else:
        continue

canvas = Canvas(ypix=ypix, xpix=xpix, bgcolor=bgcolor)
canvas.draw()



