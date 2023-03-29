import turtle


def visible(turtle_name):


    return 0


def demo():
    tom = turtle.Turtle()
    print(type(tom))
    tom.speed(1)
    for x in range(5):
        tom.forward(50)
        tom.left(90)
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()
    tom.forward(100)
    tom.pendown()
    tom.pencolor("red")
    tom.right(90)
    tom.forward(120)
    tom.right(-90)
    tom.forward(120)
    tom.home()
    turtle.done()


demo()
