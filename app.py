def init():
    while(True):
        try:
            print("Welcome to the simple calculator!\nPlease select one of the following options:\nAddition: 1\nSubtraction: 2\nMultiplication: 3\nDivision: 4\nYour Choice:")
            choice = int(input())
            # Get the user's choice and convert it to a number
            if(choice == 1 or choice == 2 or choice == 3 or choice == 4):
                # Get the user's two numbers they wish to do arithmetic on
                user_num_one, user_num_two = get_numbers()
                calculate(choice, user_num_one, user_num_two)
                # If the user answers no to restart, get out of the loop and end program.
                if(restart() == False):
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
            print("Would you like to do another calculation?\nYes: 1\nNo: 2\nYour Choice: ")
            # Ask for user input and convert it to a number
            user_input = int(input())
            if(user_input == 1):
                # Will loop the init function
                return True
            elif(user_input == 2):
                print("Goodbye")
                # Will break the init function loop
                return False
        except ValueError:
            print("Enter 1 or 2")
        except:
            print("Something went wrong")
    
def get_number():
    while(True):
        # Will keep asking for a valid number until the user enters a valid number
        try:
            num = float(input())
            # Return a valid number
            return num
        except ValueError:
            print("Please enter a valid number. Enter a another number: ")
        except:
            print("Something went wrong.")

def get_numbers():
    print("Enter a first number: ")
    # Store the first number into a variable
    user_num_one = get_number()
    print("Enter a second number: ")
    # Store the second number into another variable
    user_num_two = get_number()
    # Return those two numbers
    return user_num_one, user_num_two

def calculate(choice, num_one, num_two):
    # Pass the choice and the two numbers into this function
    try:
        # Return the result based on the user's choice
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
    except:
        print("Something went wrong.")

# Call the program
init()










