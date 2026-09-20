sep_sign= "-"
version = "v1.0.0"
import geometry
import number_theory

""" Start the programm and Check wich option the user select , call functions based on selection &
 print the result"""
def main():
    while True:
        option=start()
        if option==3:
            print("MathForge is closed")
            quit()
        elif option==1:
            print("Choose a tool")
            print("1. Triangle Analyzer")
            print("2. Back")
            option= get_option()
            if option==2:
                pass
            elif option==1:
                geometry.triangle_analyzer()
            else:
                    print("Please enter a valid number")
        elif option==2:
            print("Choose a tool")
            print("1. Analize number")
            print("2. Back")
            option=get_option()
            if option==2:
                pass
            elif option==1:
                number_theory.analyze_number()
            else:
                    print("Please enter a valid number")
        else:
            print("Please enter a valid number")

"""Start the programm and Get user selection"""
def start():
    print(70*sep_sign) 
    print("MathForge".center(70))
    print(version.center(70))
    print(70*sep_sign)
    print("Choose a tool")
    print("1. Geometry lab")
    print("2. Numbertheory lab")
    print("3. Exit")
    option=get_option()
    return option

def get_option():
    while True:
        try:
            option= int(input())
            return option
        except ValueError:
            print("Please enter a valid number")

main()