import turtle

squirt = turtle.Turtle()

value = 100 
squirt.speed(value)

#---------------DEFINE FUNCTIONS----------#

def colourThingy():

    squirt.pencolor("blue")

    for i in range(50):
        squirt.forward(50)
        squirt.left(123) # Let's go counterclockwise this time

    squirt.pencolor("red")
    for i in range(50):
        squirt.forward(100)
        squirt.left(123)

def polygon(num_sides):

    side_length = 70
    angle = 360.0 / num_sides
    for i in range(num_sides):
        squirt.forward(side_length)
        squirt.right(angle)

def dots():
    dot_distance = 25
    width = 5
    height = 7
    squirt.penup()
    for y in range(height):
        for i in range(width):
            squirt.dot()
            squirt.forward(dot_distance)
        squirt.backward(dot_distance * width)
        squirt.right(90)
        squirt.forward(dot_distance)
        squirt.left(90)

def ninja():
    squirt.speed(2000)
    for i in range(180):
        squirt.forward(100)
        squirt.right(30)
        squirt.forward(20)
        squirt.left(60)
        squirt.forward(50)
        squirt.right(30)
        squirt.penup()
        squirt.setposition(0, 0)
        squirt.pendown()
        squirt.right(2)



#---------------CALL FUNCTIONS----------#

colourThingy()
#polygon(6)
#dots()
#ninja()
