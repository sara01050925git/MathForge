# Handle invalid input after learning try/except.
# Change tolerance of righangle() function to relative tolerance
sep_sign= "="

""" Start the programm and Check wich option the user select , call functions based on selection &
 print the result"""
def main():
    option=start()
    if option==2:
        print("MathForge is closed")
    elif option==1:
        side1 , side2, side3 = triangle_side_input()
        if is_triangle(side1 , side2 , side3):
            print(" Result ".center(70,"="))
            print("Valid Triangle : Yes" )
            print(f"Type           : {triangle_type_detect(side1 , side2, side3)}")
            print(f"Right Triangle : {is_rightangle(side1, side2 , side3)}")
            print(70*sep_sign) 
        else :
            print("This is not a valid Triangle!")
        
    else:
        print("Please enter a valid number")

"""Start the programm and Get user selection"""
def start():
    print(70*sep_sign) 
    print("MathForge".center(70))
    print("v0.1".center(70))
    print(70*sep_sign)
    print("Choose a tool")
    print("1. Triangle Analyzer")
    print("2. Exit")
    option= input()
    return option 

# First option(Triangle analizer) functions
def triangle_side_input():
    side1= float(input("Enter the first sides length: "))
    side2= float(input("Enter the second sides length: "))
    side3= float(input("Enter the third sides length: "))
    return side1 , side2 , side3

def is_triangle(side1 , side2 , side3):
    sum12 = side1 + side2
    sum13 = side1 + side3
    sum23 = side2 + side3
    if sum12 > side3 and sum13 > side2 and sum23 > side1:
        return True 
    else:
        return False

def triangle_type_detect(side1, side2 , side3):
    if side1== side2 and side2==side3:
        return "Equilateral"
    elif side1==side2 or side2==side3 or side3==side1:
        return "Isosceles"
    else:
        return "scalene" 
    
def is_rightangle(side1, side2 , side3):
    import math
    magnitude=math.log(side1,10)
    sqr_side1=side1*side1
    sqr_side1_plus= sqr_side1 + magnitude/20
    sqr_side1_minus= sqr_side1 - magnitude/20
    sqr_side2=side2*side2
    sqr_side2_plus= sqr_side2 + magnitude/20
    sqr_side2_minus= sqr_side2 - magnitude/20
    sqr_side3=side3*side3
    sqr_side3_plus= sqr_side3 + magnitude/20
    sqr_side3_minus= sqr_side3 -magnitude/20
    if sqr_side2_minus + sqr_side3_minus <= sqr_side1 <= sqr_side2_plus + sqr_side3_plus or sqr_side1_minus + sqr_side3_minus <= sqr_side2 <= sqr_side1_plus + sqr_side3_plus or sqr_side2_minus + sqr_side1_minus <= sqr_side3 <= sqr_side2_plus + sqr_side1_plus :
        return "Yes"
    else: 
        return "No"
    
main()

