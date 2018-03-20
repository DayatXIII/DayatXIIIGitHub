import turtle

#Looping using for loop

for rotate in range(3) :
    turtle.right(70)
    for steps in range(4) :
        turtle.right(90)
        turtle.forward(100)
        #for miniSteps in range(4) :
        #    turtle.right(90)
        #    turtle.forward(50)
        #    for miniMiniSteps in range(4) :
        #        turtle.right(90)
        #        turtle.forward(25)
        #        for miniMiniMiniSteps in range(4) :
        #            turtle.right(90)
        #            turtle.forward(10)


#Looping using while loop

turtle.right(70)

steps = 0;
while steps < 4 :
    turtle.right(90)
    turtle.forward(100)
    steps += 1

