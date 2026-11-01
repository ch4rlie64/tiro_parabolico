from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 500) / 25
        speed.y = (y + 500) / 25
        #Se aumenta el valor inicial de la velocidad de 200 a 500

def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5
        if not inside(target):
            target.x = 200
            target.y = randrange(-150, 150)
        target.x -= 2
        #Se aumentó la velocidad horizontal de los proyectiles de 0.5 a 2
    if inside(ball):
        speed.y -= 1
        #Para balancear el aumento de velocidad inicial de el proyectil
        #se aumentó la gravedad de 0.35 a 1       
        ball.move(speed)

    dups = targets.copy()
    targets.clear()

    for target in dups:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
