import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_anti_clockwise():
    tim.setheading(tim.heading() - 10)


def turn_clockwise():
    tim.setheading(tim.heading() + 10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_anti_clockwise, "a")
screen.onkey(turn_clockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
