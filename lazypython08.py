"""
if TRUE and TRUE
    command
"""
# and

age = 12
passport = "yes"

if age >= 16 and passport == "yes":
    print("Yes, you can travel abroad.")
else:
    print("Sorry! Not this time, see you:)")

# or
"""
if TRUE or TRUE
    command
if TRUE or FALSE
    command
if FALSE or TRUE
    command
"""

ticket = "no"
money = "no"
if ticket == "yes" or money == "yes":
    print("Yes, you may board the bus.")
if ticket == "no" and money == "no":
    print("Sorry! You should have a ticket or money.")

# not
money1 = 9
price = 10
condition = money1 >= price
if condition:
    print("You may board the bus.")
if not condition:
    print("Wait for the day of the hare.")





