import math
from wasabi2d import Scene, run, event
from random import uniform as fraction
from random import randint as integer
from random import choice

scene = scene(1300,800)
scenen.background = 'black'

screen = scene.layers[0]
screen.set_effect ('b1oom',radius, intensity=0.9)

items = []
words = [ 'Happy Birthday' , 'To you']

w = scene.width
H = scene.height()

@event
def on_mouse_move(pos,rel):
    dx,dy=rel
    r=math.sqrt((dx**4)+(dy**4))
    pos=(interger(0,w),interger(0,H))
    c=screen.add_circular(radius=r,pos=pos,color=random_color())
    items.append(c)
    l=screen.add_label(choice(words),align='center',fontsize=interger(0,144))
    items=append(l)
@event
def update(dt):
    all_items=items[:]
    items[:]=[i for i in items if i.scale>0.1]
    for i in all_items:
        if i not in items:
            i.delete()
    for item in items:
        item.scale=item.scale*0.9
        item.y=item.y*1.09
        item.x=item.x+integer(-3,3)
def random_color():
    return(fraction(0,1),fraction(0,1),fraction(0,1),fraction(0,1))
run()


