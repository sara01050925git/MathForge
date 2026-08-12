# Handle invalid input after learning try/except.
# Change tolerance of righangle() function to relative tolerance
# Optimize number_divisors()
# Improve the construction of back button
sep_sign= "="
import math

""" Start the programm and Check wich option the user select , call functions based on selection &
 print the result"""
def main():
    option=start()
    if option==3:
        print("MathForge is closed")
    elif option==1:
        geometry_lab()
    elif option==2:
        number_theory_lab()
    else:
        print("Please enter a valid number")

"""Start the programm and Get user selection"""
def start():
    print(70*sep_sign) 
    print("MathForge".center(70))
    print("v0.1".center(70))
    print(70*sep_sign)
    print("Choose a tool")
    print("1. Geometry lab")
    print("2. Numbertheory lab")
    print("3. Exit")
    option= int(input())
    return option 


# Functions related to geometry lab 
def geometry_lab():
    print("Choose a tool")
    print("1. Triangle Analyzer")
    print("2. Back")
    option= int(input())
    if option==2:
        main()
    elif option==1:
        triangle_analyzer()
    else:
        print("Please enter a valid number")
    
def triangle_analyzer():
    side1 , side2, side3 = triangle_side_input()
    if is_triangle(side1 , side2 , side3):
        print(" Result ".center(70,"="))
        print("Valid Triangle  : Yes" )
        print(f"Type           : {triangle_type_detect(side1 , side2, side3)}")
        print(f"Right Triangle : {is_rightangle(side1, side2 , side3)}")
        print(70*sep_sign) 
    else :
        print("This is not a valid Triangle!")
        
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



#Functions related to number_theory_lab
def number_theory_lab():
    print("Choose a tool")
    print("1. Analize number")
    print("2. Back")
    option= int(input())
    if option==2:
        main()
    elif option==1:
        analyze_number()
    else:
        print("Please enter a valid number")

def analyze_number():
    number = int(input("Please enter an Integer: "))
    divisors=number_divisors(number)
    print(" Result ".center(70,"="))
    print(f"Prime Number:   {prime_number(number)}")
    print(f"Perfect Number: {perfect_number(number,divisors)}\n")
   
    print(f"Divisors:       {divisors}")
    print(f"Total divisors: {total_divisors(divisors)}")

def prime_number(number):
    divisor = 2
    if number <= 1:
        return "No"
    else:
        root=int(math.sqrt(number))
        while True:
            if divisor <= root :
                if number%divisor == 0:
                    break
                else:
                    divisor +=1
            else:
                return "Yes"
        return "No"


def perfect_number(number, divisors):
    divisors_sum =0 
    if number == 0 :
        return "No"
    else:
        for divisor in divisors:
            divisors_sum = divisors_sum + divisor
        if number== divisors_sum/2 and divisors_sum%2==0:
            return "Yes" 
        else:
            return "No"



def number_divisors(number):
    divisor = 1
    divisors=[]
    if number ==0:
        return "Every Number"
    elif number > 0:
        for divisor in range(number):
            if number%(divisor+1) == 0:
                divisors.append(divisor+1)
        return divisors
    elif number < 0 :
        for divisor in range(-number):
            if number%(divisor+1) == 0:
                divisors.append(divisor+1)
        return divisors


def total_divisors(divisors):
    if divisors == "Every Number":
        return "Infinity"
    else:
        i=0
        for divisor in divisors:
            i +=1
        return i 





main()



