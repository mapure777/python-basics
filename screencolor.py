import turtle
import random
screen = turtle.Screen()
colors = ["blue","red","green","pink","orange","white","yellow","purple"]
def screencolor(x,y):
    c = random.choice(colors)
    screen.bgcolor(c)

# calling the function
screen.onclick(screencolor)
turtle.done()
