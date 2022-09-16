#IMPORT CONSTANTS 
from math import pi
import math


# 


#CALCULATE AREA FOR SQUARE CIRCLE AND RECTANGLE

# SQUARE
# DEFINE FUNCTIONS THAT WILL BE CALLED LATER IN THE PROGRAM
def SQUARE(length):
    area_of_square = length * length
    # OUTPUT THE ANSWER 


    return float('%.2g' % area_of_square) # ROUND TO TWO SIGNIFICANT FIGURES


def RECTANGLE(length,width):
    area_of_rectangle = length * width


    #OUTPUT THE ANSWER
    return float('%.2g' % area_of_rectangle)

def CIRCLE(radius):
    area_of_circle = pi * (radius**2)

    return float('%.2g' % area_of_circle)


#CALCULATE VOLUME FOR CYLINDER CONE AND CUBOID/CUBE

def CYLINDER(r,h):
    volume_of_cylinder = pi * r * r * h

    #OUTPUT ANSWER
    return float('%.2g' % volume_of_cylinder)

def CONE(r,h):
    #V=1/3hπr².

    volume_of_cone = 1/3*h*pi*(r**2)

    return float('%.2g' % volume_of_cone)

def CUBOID(l,w,h):
    volume_of_cuboid = l * w * h

    return float('%.2g' % volume_of_cuboid)

def CUBE(l):
    #Use the length of one side to calculate
    volume_of_cube = (l**3)

    return float('%.2g' % volume_of_cube)


# PROGRAM THE USER INTERFACE

#OUTPUT WELCOME MESSAGE
print("""
================================
# WELCOME TO MY SHAPE CALCULATOR
================================
""")

# CREATE AN INFINITE WHILE LOOP TO CONTINUE RUNNING PROGRAM UNTIL USER ENDS IT
while True:
    print("""
    ------------------
    CHOOSE NUMBER FROM 1-7
    ------------------
    1) SQUARE (area)
    2) RECTANGLE (area)
    3) CIRCLE (area)
    4) CYLINDER (volume)
    5) CONE (volume)
    6) CUBOID (volume)
    7) CUBE (volume)
    """)
    #USER ENTERS SHAPE CHOICE
    shape_choice = input("PLEASE CHOOSE A SHAPE NUMBER: ")
    # Select the process based on the number inputed by the user
    if shape_choice == "1" or shape_choice == "square":
        # ASK FOR USER INPUT FOR ARGUMENTS AND PARAMETERS FOR THE SPECIFIC FUNCTION CHOSEN
        length = input("PLEASE ENTER LENGTH OF YOUR SQUARE: ")
        # Check if user entered an actual number to prevent calculation and conversion errors
        if length.isdigit():
            # Output the ANSWER
            print("AREA OF YOUR SQUARE IS: ", SQUARE(float(length)),'cm') # ADD UNIT TO FINAL ANSWER
            #CHECK IF USER WANTS TO CALCULATE ANOTHER SHAPE AND IF NOT EXIT THE PROGRAM
            PROGRAM_STATUS = input("WILL YOU LIKE TO CALCULATE ANOTHER SHAPE?(yes/no): ")
            PROGRAM_STATUS = PROGRAM_STATUS.lower()
            if PROGRAM_STATUS == "yes" :
                continue
            else:
                # ELSE BREAK WHILE LOOP AND EXIT THE PROGRAM
                break
        else:
            print("PLEASE ENTER A VALID NUMBER!")

        #The same logic flows through the rest of the program

    elif shape_choice == "2" or shape_choice == "rectangle":
        length = input("PLEASE ENTER LENGTH OF YOUR RECTANGLE: ")
        width = input("PLEASE ENTER WIDTH OF YOUR RECTANGLE: ")
        if length.isdigit() and width.isdigit():
            print("THIS IS THE AREA OF YOUR RECTANGLE: ", RECTANGLE(float(length),float(width)),'cm')
            PROGRAM_STATUS = input("WILL YOU LIKE TO CALCULATE ANOTHER SHAPE?(yes/no): ")
            PROGRAM_STATUS = PROGRAM_STATUS.lower()
            if PROGRAM_STATUS == "yes" :
                continue
            else:
                break

        else:
            print("PLEASE ENTER VALID NUMBERS!")
        

    elif shape_choice == "3" or shape_choice == "circle":
        radius = input("PLEASE ENTER RADIUS OF YOUR CIRCLE: ")
        if radius.isdigit():
            print("THIS IS THE AREA OF YOUR CIRCLE: ", CIRCLE(float(radius)),'cm')
            PROGRAM_STATUS = input("WILL YOU LIKE TO CALCULATE ANOTHER SHAPE?(yes/no): ")
            PROGRAM_STATUS = PROGRAM_STATUS.lower()
            if PROGRAM_STATUS == "yes" :
                continue
            else:
                break
        else:
            print("PLEASE ENTER A VALID NUMBER!")
        
    
    elif shape_choice == "4" or shape_choice == "cylinder":
        radius = input("PLEASE ENTER RADIUS OF YOUR CYLINDER: ")
        height = input("PLEASE ENTER HEIGHT OF YOUR CYLINDER: ")
        if height.isdigit() and radius.isdigit():
            print("THIS IS THE VOLUME OF YOUR CYLINDER: ", CYLINDER(float(radius),float(height)),'cm3')
            PROGRAM_STATUS = input("WILL YOU LIKE TO CALCULATE ANOTHER SHAPE?(yes/no): ")
            PROGRAM_STATUS = PROGRAM_STATUS.lower()
            if PROGRAM_STATUS == "yes" :
                continue
            else:
                break
        else:
            print("PLEASE ENTER VALID NUMBERS!")
        

    elif shape_choice == "5" or shape_choice == "cone":
        radius = input("PLEASE ENTER RADIUS OF YOUR CONE: ")
        height = input("PLEASE ENTER HEIGHT OF YOUR CONE: ")
        if height.isdigit() and radius.isdigit():
            print("THIS IS THE VOLUME OF YOUR CONE: ", CONE(float(radius),float(height)),'cm3')
            PROGRAM_STATUS = input("WILL YOU LIKE TO CALCULATE ANOTHER SHAPE?(yes/no): ")
            PROGRAM_STATUS = PROGRAM_STATUS.lower()
            if PROGRAM_STATUS == "yes" :
                continue
            else:
                break
        else:
            print("PLEASE ENTER VALID NUMBERS!")
        


    elif shape_choice == "6" or shape_choice == "cuboid":
        width = input("PLEASE ENTER WIDTH OF YOUR CUBOID: ")
        length = input("PLEASE ENTER LENGTH OF YOUR CUBOID: ")
        height = input("PLEASE ENTER HEIGHT OF YOUR CUBOID: ")
        conditions = [ length.isdigit(),height.isdigit(),width.isdigit()]
        if all(conditions):
            print("THIS IS THE VOLUME OF YOUR CUBOID: ", CUBOID(float(length),float(width),float(height)),'cm3')
            PROGRAM_STATUS = input("WILL YOU LIKE TO CALCULATE ANOTHER SHAPE?(yes/no): ")
            PROGRAM_STATUS = PROGRAM_STATUS.lower()
            if PROGRAM_STATUS == "yes":
              continue
            else:
                break
        else:
            print("PLEASE ENTER VALID NUMBERS!")

    elif shape_choice == "7" or shape_choice == "cube":
        length = input("PLEASE ENTER LENGTH OF YOUR CUBE: ")
        if length.isdigit():
            print("THIS IS THE VOLUME OF YOUR CUBE: ", CUBE(float(length)),'cm3')
            PROGRAM_STATUS = input("WILL YOU LIKE TO CALCULATE ANOTHER SHAPE?(yes/no): ")
            PROGRAM_STATUS = PROGRAM_STATUS.lower()
            if PROGRAM_STATUS == "yes" :
                continue
            else:
                break
        else:
            print("PLEASE ENTER A VALID NUMBER!")
    else:
        print("PLEASE CHOOSE FROM LIST!")


