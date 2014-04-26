# author: Nathangabc
import turtle
t= turtle.Turtle()
length = 1
angle = 1
numbers = [ 1, 2, 3, 4, 5 ]
count = 0
while count < 360:
	t.forward(length)
	t.left(angle)
	count = count + 1