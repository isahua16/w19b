def init():
    while(True):
        try:
            print("Welcome to the simple calculator!\nPlease select one of the following options:\nAddition: 1\nSubtraction: 2\nMultiplication: 3\nDivision: 4\nYour Choice:")
            choice = input()
            choice = int(choice)
            if(choice == 1 or choice == 2 or choice == 3 or choice == 4):
                user_num_one, user_num_two = get_numbers()
                calculate(choice, user_num_one, user_num_two)
                if(not restart()):
                    return
            else:
                print("Your entry is not valid. ")
        except ValueError:
            print("Your entry is not a valid number between 1, 2, 3 or 4")
        except:
            print("Your entry is invalid.")

def restart():
    while(True):
        try:
            print("Would you like to do another calculation?\n 1: Yes\n 2: No\nYour Choice: ")
            user_input = int(input())
            if(user_input == 1):
                return True
            elif(user_input == 2):
                print("Goodbye")
                return False
        except ValueError:
            print("Enter 1 or 2")
        except:
            print("Something is wrong")
    

def get_number():
    while(True):
        try:
            num = float(input())
            return num
        except ValueError:
            print("Please enter a valid number. Enter a another number: ")
        except:
            print("Something went wrong, try again")

def get_numbers():
    print("Enter a first number: ")
    user_num_one = get_number()
    print("Enter a second number: ")
    user_num_two = get_number()
    return user_num_one, user_num_two

def calculate(choice, num_one, num_two):
    try:
        if(choice == 1):
            print("Your result:", num_one + num_two)
        elif(choice == 2):
            print("Your result:", num_one - num_two)
        elif(choice == 3):
            print("Your result:", num_one * num_two)
        elif(choice == 4):
            print("Your result:", num_one / num_two)
    except ZeroDivisionError:
        print("Cannot divide a number by 0")

init()










