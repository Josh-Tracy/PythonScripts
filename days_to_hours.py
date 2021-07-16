
# Variables
#calculation_to_units = 24
#name_of_units = "hours"


# functions - Parameters passed from user input after being converted to an integer
# unit gathered during input and assigned to unit key in dictionary
# only hours and minutes are valid
def days_to_units(num_of_days, conversion_unit):
        if conversion_unit == "hours":
            return f"{num_of_days} days are {num_of_days * 24} hours"
        elif conversion_unit == "minutes":
            return f"{num_of_days} days are {num_of_days * 24 * 60}  minutes"
        else:
            return "unsupported unit"

def validate_and_execute():
    try:
        # User input number for key days is converted into an integer
        #
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid number")
        else:
            print("You entered a negative number, please enter a valid number")

    except ValueError:
        print("You input is not a valid number")

# Continue to run unless uncaught exception is  given or exit is typed
# set function filters duplicate values from the list
#user_input = "placeholder"
#while user_input != "exit":
#    user_input = input("Enter the number of days to convert to hours:\n- Seperate a list using commas\n")
#    for number_of_days_element in set(user_input.split(", ")):
#        validate_and_execute()

user_input = "placeholder"
while user_input != "exit":
    user_input = input("Enter the number of days and conversion unit colon seperated. Exmaple: 2:minutes\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()

my_list = [20, 30]
print(my_list[1])

# user_input given as string type
# user_input converted to integer type
# The "f" for format is only valid syntax in >=v3.6
# using v3.8