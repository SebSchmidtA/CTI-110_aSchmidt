def main():
    
    import turtle
    turtle.shape("turtle")
    turtle.penup()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()
    
    for x in range(4):
        turtle.speed(10)
        turtle.forward(200)
        turtle.left(90)
    turtle.left(150)

    
    for y in range(2):
        turtle.forward(200)
        turtle.right(120)
    #i may have cheated a little by aligning it with the square lol
main()
