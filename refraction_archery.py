# ---------------------------------------------------
# Created By       : Yonas Asmelash
# Created Date     : 11/28/2022
# Version          : 1.0
# ---------------------------------------------------

# Imports the turtle and math packages
import turtle
import math


# Sets the background color to black
turtle.bgcolor("black")

# The two turtles the program uses
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# Sets the turtle colors to white
t1.pencolor("white")
t2.pencolor("white")

# Switches the turtles for arrows for aesthetic purposes
t1.shape("arrow")
t2.shape("arrow")

# Sets the speed of the turtles to 0
t1.speed(5)
t2.speed(5)

# Sets the pensize of each turtle to 5
t1.pensize(5)
t2.pensize(5)

t1.penup()
t1.goto(-300,20)
t1.pendown()
t1.write("n1", font=("Arial", 20, "bold"))

t1.penup()
t1.goto(-300,-40)
t1.pendown()
t1.write("n2", font=("Arial", 20, "bold"))


# PIcks up the pen, moves the turtle to (0,300), then draws a vertical line
t1.penup()
t1.goto(0,300)
t1.pendown()
t1.rt(90)
t1.fd(600)
t1.lt(90)

# PIcks up the pen, moves the turtle to (-300,0), then draws a horizontal line
t2.penup()
t2.goto(-300,0)
t2.pendown()
t2.fd(600)



# --------------------------------------------------------------------------------------------------

# Promts the user for the pen color
ray_color = turtle.textinput("What color do you want the ray to be?", "Ray Color: ")
t1.color(ray_color)
t2.color(ray_color)



# Prompts the user for the n1 and n2 values
n1 = turtle.numinput("What value value do you want the first index of refraction to have? ", "Enter n1 value: ")
n2 = turtle.numinput("What value value do you want the second index of refraction to have? )", "Enter n2 value: ")


# Promts the user for the angle of incidence
aoi = turtle.numinput("What angle do you want the angle of incidence to be?", "Enter the angle of incidence: ")


# Draws both the angle of incidence and reflected angle
t1.penup()
t1.goto(0,0)
t1.lt(90)
t1.lt(aoi)
t1.fd(250)
t1.rt(180)
t1.pendown()
t1.fd(250)
t1.rt(aoi+180)
t1.rt(aoi)
t1.fd(250)

aoref = aoi

t1.color("#89CFF0")
t1.penup()
t1.goto(-250,250)
t1.pendown
t1.write("Incident Ray", font=("Arial", 15, "bold"))

t1.penup()
t1.goto(-160, 30)
t1.pendown()
t1.write("θi=" + str(aoi), font=("Arial", 10, "bold"))


t1.penup()
t1.goto(230,250)
t1.pendown
t1.write("Reflected Ray", font=("Arial", 15, "bold"))

t1.penup()
t1.goto(70,30)
t1.pendown
t1.write("θr=" + str(aoref), font=("Arial", 10, "bold"))



t1.pencolor(ray_color)


# Creates variable repreesnting angle of indescendece in radians
aoi_in_radians = aoi*(math.pi/180)

# Calculates the angle of refraction utilizing Snell's Law in radians
aor_in_radians = ((n1*(math.sin(aoi_in_radians)))/n2)

# Converts angle of refraction into degrees
aor = aor_in_radians*(180/math.pi) 


# Calculates the critical angle
critical_angle = math.asin(n1/n2)

if aoi_in_radians > critical_angle:
    t2.penup()


else:
    # Picks up the pen and sets the turtle at (0,0)
    t2.penup()
    t2.right(90)
    t2.goto(0,0)
    t2.pendown()
    # Turns the neccessary number of degrees and moves forward 100 to draw the angle of refraction
    t2.left(aor)
    t2.fd(250)

    t1.color("#89CFF0")
    t1.penup()
    t1.goto(200,-250)
    t1.write("Refracted Ray", font=("Arial", 15, "bold"))

    t1.penup()
    t1.goto(10,-170)
    t1.pendown
    t1.write("θR=" + str(aoref), font=("Arial", 10, "bold"))



# Ends program and keeps screen on
turtle.done()