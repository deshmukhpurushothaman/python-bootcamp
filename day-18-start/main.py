import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

num_sides = 5

# colors = ["medium aquamarine", "cyan", "forest green", "crimson",
#           "purple", "orange", "yellow", "blue", "red", "black", "pink"]
directions = [0, 90, 180, 360]

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for num_sides in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(num_sides)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# tim.pensize(15)
tim.speed("fastest")


def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap_size)


draw_spirograph(5)
# for _ in range(200):
#     tim.color(randomColor())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
