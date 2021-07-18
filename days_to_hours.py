from helper import validate_and_execute, user_input_message
# import all
# from helper import *

# Built in modules
#import os
#import logging
#print(os.name)

#logger = logging.getLogger("MAIN")
#logger.error("Error happened")


user_input = "placeholder"
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dictionary)


# user_input given as string type
# user_input converted to integer type
# The "f" for format is only valid syntax in >=v3.6
# using v3.8
