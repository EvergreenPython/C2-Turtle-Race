import turtle 
import random

cameraMan = turtle.Turtle() 
cameraMan.shape("triangle")

cameraMan.penup() 
cameraMan.goto(-175, 140)
cameraMan.speed(0)

for i in range(16): 
  cameraMan.write(i)
  cameraMan.right(90)
  cameraMan.forward(20)
  cameraMan.pendown() 
  cameraMan.forward(200)
  cameraMan.left(180)
  cameraMan.penup()
  cameraMan.forward(220)
  cameraMan.right(90)
  cameraMan.forward(20)
cameraMan.hideturtle() 

celine = turtle.Turtle() 
celine.shape("turtle")
celine.penup() 
celine.goto(-200, 100)
celine.color("gold") 

trevor = turtle.Turtle() 
trevor.shape("turtle")
trevor.penup() 
trevor.goto(-200, 60)
trevor.color("red") 

aaron = turtle.Turtle() 
aaron.shape("turtle")
aaron.penup() 
aaron.goto(-200, 20)
aaron.color("blue") 

emma = turtle.Turtle() 
emma.shape("turtle")
emma.penup() 
emma.goto(-200, -20)
emma.color("yellow") 

arnav = turtle.Turtle() 
arnav.shape("turtle")
arnav.penup() 
arnav.goto(-200, -60)
arnav.color("silver") 

# Create 4 more turtles, with different colors
# Set their locations 

celine.pendown() 
trevor.pendown()
aaron.pendown() 
emma.pendown() 
arnav.pendown() 

for i in range(40): 
  celine.forward(random.randint(1,15))
  trevor.forward(random.randint(1,15))
  aaron.forward(random.randint(1,15))
  emma.forward(random.randint(1,15))
  arnav.forward(random.randint(1,15))