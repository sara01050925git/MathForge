# Optimize number_divisors()
import math
sep_sign= "="

def analyze_number():
    while True:
        try:
            number = int(input("Please enter an Integer: "))
            if number < 0:
                 print("Please enter a postive integer.")
            else :
                break
        except ValueError:
            print("Please enter an integer: ")


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

