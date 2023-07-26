from turtle import *

pensize(2)
speed('fastest')
for i in range(6):
    lt(60)
    fd(100)
    for i in range(4):
        lt(90)
        fd(50)
        for i in range(6):
            lt(60)
            fd(25)
            

hideturtle()
mainloop()