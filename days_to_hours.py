# Variables
calculation_to_units = 24
name_of_units = "hours"


# functions - Parameters passed from user input after being converted to an integer
def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"

def validate_and_execute():
    try:
        user_input_number = int(number_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid number")
        else:
            print("You entered a negative number, please enter a valid number")

    except ValueError:
        print("You input is not a valid number")

# Continue to run unless uncaught exception is  given or exit is typed
# set function filters duplicate values from the list
user_input = "placeholder"
while user_input != "exit":
    user_input = input("Enter the number of days to convert to hours:\n- Seperate a list using commas\n")
    for number_of_days_element in set(user_input.split(", ")):
        validate_and_execute()

# user_input given as string type
# user_input converted to integer type
# The "f" for format is only valid syntax in >=v3.6
# using v3.8
