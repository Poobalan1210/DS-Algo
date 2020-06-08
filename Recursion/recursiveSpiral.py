import turtle

def make_spiral(my_turtle,line_len):
	if line_len>0:
		my_turtle.forward(line_len)
		my_turtle.right(90)
		make_spiral(my_turtle,line_len-5)

if __name__=="__main__":
	my_turtle=turtle.Turtle()
	my_win=turtle.Screen()

	make_spiral(my_turtle,50)
	my_win.exitonclick()