"""
if condition:
    command
elif conditiontwo:
    command
elif conditionthree:
    command
elif conditionfour:
    command
else:
    command

and
or
not
"""

marsians = 100
cyborgs = 0
print("Hello Earth! This is the report on Mars occupation.")

if(cyborgs >= 51):
    print("Mission accomplished! Cyborgs have occupied Mars!")
elif cyborgs > 41 and cyborgs < 51:
    print("Missions is nearly accomplished. We are close to completion.")
elif cyborgs > 26 and cyborgs <= 41:
    print("Mission in progress, we are in the second half.")
elif cyborgs > 10 and cyborgs <= 26:
    print("Mission in progress, we are still in the first half.")
elif cyborgs >= 1 and cyborgs <= 10:
    print("Mission in still on the early stage")
else:
    print("Sorry! Cyborgs died :(")

print("End of report. Your cyborgs.")
