This code was created by Usman 2152992

//Start of program

import turtle
    
      
t = turtle.Turtle()
  
# radius of the circle
r = 10
  
# Loop for printing concentric circles
for i in range(50):
    t.circle(r * i)
    t.up()
    t.sety((r * i)*(-1))
    t.down()

//End of program
