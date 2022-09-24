from turtle import *
import random

tracer(0, 0); goto(5000, 0); goto(-5000, 0); goto(0,0); tracer(1, 1)

t = 0
y = 0
incr = 0.25


pitch = 7 #pitch (not in degrees)
gravity = .5 #strength of gravity (1 is normal, .5 is half, 2 is double etc)
velocity = 20 #velocity

while True:
    t = t+incr
    x = t*pitch
    velocity = velocity+(-gravity*incr)
    y = y+velocity*incr
    goto(x,y)
    if ycor() <= 0: break

crash = (x, 0)
goto(crash)
tracer(0, 0)
for i in range(30):
    goto(crash[0]+random.randint(-50, 50), crash[1]+random.randint(-50, 50))
    pencolor(random.choice(['red', 'orange', 'yellow']))
    goto(crash)
pencolor('black')
write('BOOM!')
