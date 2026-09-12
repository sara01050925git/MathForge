# Change tolerance of righangle() function to relative tolerance
import math
sep_sign= "="
#Triangle analyzer
def triangle_analyzer():
    while True:
        side1,side2,side3=get_sides()
        
        if is_triangle(side1 , side2 , side3):
            break
        else:
            print("oops,It's Not A triangle!")
    print(" Result ".center(70,"="))
    print("Valid Triangle  : Yes" )
    print(f"Type           : {triangle_type_detect(side1 , side2, side3)}")
    print(f"Right Triangle : {is_rightangle(side1, side2 , side3)}")
    print(70*sep_sign) 
            

def get_sides():
    i=0
    sides=[1 ,1 ,1 ]
    for side in sides:
        i=i+1
        while True:
            try:
                sides[i-1]=float(input(f"Enter the length of side{i}: "))
                if sides[i-1]<=0:
                    raise ValueError
                break
            except ValueError:
                print("⚠  Enter a posetive NUMBER as sidelength")
    return sides

def is_triangle(side1,side2,side3):
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