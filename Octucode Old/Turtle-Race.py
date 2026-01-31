import os
from turtle import Turtle, Screen

tur = Turtle()
scr = Screen()


while True:

  name = scr.textinput("لحظة من فضلك!!", "Enter what you want to draw:")
  
  if name == "square" or name == "مربع":
    tur.goto(0, 0)
    tur.color("red")
    tur.pensize(10)
    tur.shape("turtle")
    for _ in range(4):
      tur.forward(100)
      tur.left(90)

  elif name == "circle" or name == "دائرة":
    tur.goto(0, 0)
    tur.color("black")
    tur.pensize(5)
    tur.shape("square")
    tur.speed(0)
    step_size = 5
    for _ in range(360 // step_size):
      tur.forward(step_size)
      tur.left(step_size)

  elif name == "triangle" or name == "مثلث":
    tur.goto(0, 0)
    tur.color("purple")
    tur.pensize(3)
    tur.shape("circle")
    for _ in range(3):
      tur.forward(100)
      tur.left(120)

  elif name == "exit" or name == "خروج":
    scr.clear()           # Clears the screen before displaying the message
    scr.bgcolor("light blue")
    tur.pensize(5)
    tur.color("black")
    tur.penup()                # Lift the pen to prevent drawing lines
    tur.goto(50, 50)
    tur.hideturtle()
    tur.write("Press any key to exit", align="center", font=("Arial", 16, "normal"))
    tur.pensize(3)
    tur.color("gray")
    tur.goto(25, 25)
    tur.write("اضغط على اي زر للخروج", align="center", font=("Arial", 16, "normal"))
    scr.exitonclick()          # Waits for a click to exit

  else:
    continue
