import turtle
l=["red","yellow","green","pink"]
for i in range (10):
    turtle.pensize(3)
    turtle.fillcolor (l[i])
    turtle.begin_fill()
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90) #90 degree left
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.end_fill()
    turtle.write("ajay", font =("arial",20,"bold"))
    
    
