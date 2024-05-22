import turtle

turtle.bgcolor ( "purple" )
p = turtle.Pen ( )
p.pencolor ( "yellow" )
p.shape ( "turtle" )
p.width ( 2 )



l = 30
h = 15
for no_side in range ( 3 , 100 ):
    p.left ( 90 + 180 / no_side)
    
    for j in range (no_side):
        p.forward ( l )
        p.left ( 360 / no_side )
    p.right ( 90 + 180 / no_side )
    p.penup ( )
    p.forward ( h )
    p.pendown ( )

    l+=15
    h+=5
   

turtle.done