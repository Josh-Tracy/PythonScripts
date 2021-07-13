# Variables
calculation_to_units = 24
name_of_units = "hours"


# functions - Parameters passed from user input after being converted to an integer
def days_to_units(num_of_days):
    # validation
    print(num_of_days > 0)
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"
    else:
        return "Invalid value: Negative integer given"

# user_input given as string type
user_input = input("Enter the number of days to convert to hours:\n")
# user_input converted to integer type
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)
# The "f" for format is only valid syntax in >=v3.6
# using v3.8
