import requests
sep_sign= "="

def main():
    while True:
        opration=input("Enter your operation: ")
        pay_load={"expr": opration}
        try: 
            response=requests.get(f"http://api.mathjs.org/v4/",params=pay_load)
            response.raise_for_status()
        except  requests.HTTPError:
            status=response.status_code
            if (status//100) ==4:
                print("Please check your input and try again.")
            elif (status//100) ==5:
                print("There is a problem with the server, Please try again later.")
            else:
                print("An error occured, try again")
        except requests.ConnectionError:
            print("Please check your connection and try again.")
        except requests.Timeout:
            print("Timed-out!!!")
        else:
            result(response,opration)
            break

def result(response,opration):
    print(" Result ".center(70,"="))
    print(f"{opration} = {response.text}")





