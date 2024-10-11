from datetime import date
from datetime import time
from datetime import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

my_dt = datetime.now()
print(my_dt)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

my_date = date.today()
my_string = my_date.strftime("%m/%d/%Y")
print(my_string)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

d1 = "06/28/1919"
d2 = "09/01/1939"
d1 = datetime.strptime(d1, "%m/%d/%Y")
d2 = datetime.strptime(d2, "%m/%d/%Y")
print(d1)
print(d2)
print(d2 - d1)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

