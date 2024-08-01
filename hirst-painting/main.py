# import colorgram
import turtle as t
import random

# colors = colorgram.extract('image.jpg', 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(245, 243, 239), (247, 242, 244), (203, 165, 107), (239, 246, 241), (151, 73, 47), (235, 238, 244), (172, 154, 39), (52, 93, 125), (223, 202, 134), (137, 32, 20), (132, 162, 185), (202, 90, 69), (48, 122, 88), (67, 48, 41), (13,
                                                                                                                                                                                                                                               100, 73), (146, 178, 146), (164, 142, 156), (111, 73, 77), (236, 175, 164), (152, 19, 23), (19, 84, 89), (183, 205, 171), (56, 45, 48), (40, 61, 74), (48, 65, 81), (80, 147, 127), (189, 83, 86), (175, 192, 211), (14, 74, 66), (224, 176, 182)]
number_of_dots = 100
tim.shape("turtle")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
