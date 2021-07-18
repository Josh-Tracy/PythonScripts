# Import modules
import datetime

# Gather input
user_input = input("Enter your goal with a deadline separated by a colon\n Example:Learn Python:10.02.2021 (D-M-Y)\n")
input_list = user_input.split(":")

# From the list of inputs, take index 0 as a string for the goal and index 1 as the date
goal = input_list[0]
deadline = input_list[1]

# Use the datetime def to turn the date taken from list,index1 into a datetime data type for use in calculations
deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

# Calculate how many days from now until deadline specified
todays_date = datetime.datetime.today()
time_till = deadline_date - todays_date
hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"The time remaining to complete your goal: {goal} is {hours_till} hours")