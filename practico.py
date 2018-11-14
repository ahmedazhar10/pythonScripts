import turtle

#Create window
window = turtle.Screen()

#Created turtle named squirt
squirt = turtle.Turtle()

#set speed
value = 100
squirt.speed(value)

#set initial position (turtle always faces left at first)

#face up
#squirt.left(90)

#face down
#squirt.right(90)

#face right
#squirt.left(180)

#face left
#already left

print("This is")

for i in range(4):
    print("LIT!!!")

#DEFINE FUNCTIONS
def square(x):
    for i in range(4):
        squirt.forward(x)
        squirt.left(90)

def trippySquare():
    for i in range(100):
        square(100)
        squirt.left(13)
        

def fourBoxes(x):
    for i in range(4):
        square(x)
        squirt.up()
        squirt.forward(x+10)
        squirt.down()


def triangle(length):
    for i in range(3):
        squirt.forward(length)
        squirt.left(120)

def trippyTriangle():
    for i in range(20):
        squirt.forward(i * 10)
        squirt.left(120)

def mountains(x):
    for i in range(5):
        triangle(x)
        squirt.up()
        squirt.forward(x+5)
        squirt.down()  

def star(length):
    for i in range(5):
        squirt.forward(length)
        squirt.right(144)

def trippyStar():
    for i in range(20):
        squirt.forward(i * 10)
        squirt.right(144)



#CALLING FUNCTIONS

square(100)
#triangle(100)

#star(100)
#fourBoxes(100)
#mountains(50)
#trippySquare()
#trippyStar()
#trippyTriangle()

#Program is now paused
window.exitonclick()
