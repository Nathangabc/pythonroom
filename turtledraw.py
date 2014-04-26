# author: Nathangabc
import turtle
t= turtle.Turtle()
sides = 50
length = 3
angle = 180 - 180 * (sides - 2) / sides
numbers = range(0, sides)
#colors = ["yellow", "blue", "green", "red", "magenta", "orange" ]
for number in numbers:
	#t.color(color)
	t.forward(length)
	t.left(angle)
	
	
	
	
