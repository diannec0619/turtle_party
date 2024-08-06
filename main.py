# Turtle party project
# Dianne Cooper
# 8/6/24

import turtle

turtle.color("green")

def helper(back):
  turtle.penup()
  turtle.back(back)
  turtle.pendown()

def triangle(size):
  angle = 120
  for i in range(3):
    turtle.forward(size)
    turtle.left(angle)

for i in range(3, 0, -1):
  triangle(i * 25)
  helper(i * 25 )
