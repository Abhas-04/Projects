import turtle as turtle_mode
import random
tim = turtle_mode
turtle_mode.colormode(255)
tim.penup()
tim.speed("fastest")
tim.hideturtle()
color_list = [(189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181), (148, 116, 120), (204, 183, 186), (180, 195, 200), (53, 69, 59), (122, 129, 135)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
  tim.dot(20,random.choice(color_list))
  tim.forward(50)
  if dot_count % 10 ==0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = turtle_mode.Screen()
screen.exitonclick()