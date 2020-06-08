'''This module contains the code to draw a Sierspinski Traingle of a certain degree'''

import turtle

def draw_triangle(points,color,turtle):
	
	#navigating to starting point and set fill color
	turtle.up()
	turtle.goto(points[0][0],points[0][1])
	turtle.down()
	turtle.fillcolor(color)
	
	#filling the color
	turtle.begin_fill()
	turtle.goto(points[1][0],points[1][1])
	turtle.goto(points[2][0],points[2][1])
	turtle.goto(points[0][0],points[0][1])
	turtle.end_fill()

def getMid(p1,p2):
	return ((p1[0]+p2[0])//2,(p1[1]+p2[1])//2)

def sierspinski(points,degree,my_turtle):
	colors=["blue","red","purple","orange","yellow","green","white","violet"]
	draw_triangle(points,colors[degree],my_turtle)
	
	if degree>0:
		points_arg=[points[0],getMid(points[0],points[1]),getMid(points[0],points[2])]
		sierspinski(points_arg,degree-1,my_turtle)
		
		points_arg=[points[1],getMid(points[1],points[0]),getMid(points[1],points[2])]
		sierspinski(points_arg,degree-1,my_turtle)
		
		points_arg=[points[2],getMid(points[2],points[0]),getMid(points[2],points[1])]
		sierspinski(points_arg,degree-1,my_turtle)

def main():
	my_turtle=turtle.Turtle()
	my_win=turtle.Screen()
	points=[[-300,-150],[0,300],[300,-150]]
	sierspinski(points,5,my_turtle)
	my_win.exitonclick()

if __name__=="__main__":
	main()