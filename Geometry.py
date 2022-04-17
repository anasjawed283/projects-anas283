import turtle
print("(1 for square) (2 for rectangle) (3 for square) (1 for circle) (4 for spiral) (5 for triangle) (6 for star) (7 for ellipse) ")
shape=int(input("enter number of shape:"))

if (shape==1):
    #for square
    t = turtle.Turtle()
    s = int(input("Enter the length of the side of square: "))
    for _ in range(4):
        t.forward(s)
        t.left(90)
    window = turtle.Screen()
    geoff = turtle.Turtle()
    window.exitonclick()
    
elif (shape==2):
    #for rectangle
    t = turtle.Turtle()
    l = int(input("Enter the length of the Rectangle: "))
    w = int(input("Enter the width of the Rectangle: "))
    t.forward(l) 
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(l)
    t.left(90)
    t.forward(w)
    t.left(90)
    window = turtle.Screen()
    geoff = turtle.Turtle()
    window.exitonclick()
    
elif(shape==3):
    #for circle
    rad=int(input("Enter the radius of circle:"))
    t = turtle.Turtle()
    t.circle(rad)
    window = turtle.Screen()
    geoff = turtle.Turtle()
    window.exitonclick()

elif (shape==4):
    #for spiral
    rad_out=int(input("Enter the outer radius of spiral:"))
    t = turtle.Turtle()
    for i in range(100):
        t.circle(rad_out + i, 45)
    window = turtle.Screen()
    geoff = turtle.Turtle()
    window.exitonclick()
        
elif (shape==5):
    #for triangle
    a= int(input("Enter the side of the eqilatral triangle:"))
    board = turtle.Turtle()
    board.forward(a)
    board.left(120)
    board.forward(a)
    board.left(120)
    board.forward(a)
    turtle.done()
    window = turtle.Screen()
    geoff = turtle.Turtle()
    window.exitonclick()

elif (shape==6):
    #star shape(forn 100)
    # # first triangle for star
    ant= int(input("Enter the side of the star:"))
    board = turtle.Turtle()
    board.forward(ant) # draw base
    board.left(120)
    board.forward(ant)
    board.left(120)
    board.forward(ant)
    board.penup()
    board.right(ant+(ant/2))
    board.forward(ant/2)
    # second triangle for star
    board.pendown()
    board.right(90)
    board.forward(ant)
    board.right(120)
    board.forward(ant)
    board.right(120)
    board.forward(ant)
    turtle.done()
    window = turtle.Screen()
    geoff = turtle.Turtle()
    window.exitonclick()

elif (shape==7):
    screen = turtle.Screen()
    screen.title("Project @Anas Jawed :Now drawing Ellipse")
    screen.setup(500,500)
    turtle.up()
    turtle.goto(-140,-75)
    turtle.down()
    turtle.seth(-45)
    turtle.circle(200,90)
    turtle.circle(100,90)
    turtle.circle(200,90)
    turtle.circle(100,90)
    window = turtle.Screen()
    geoff = turtle.Turtle()
    window.exitonclick()

else:
    print("Invalid drawing number")
    