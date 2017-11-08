"""
String methods
.find()
.rfind()
.index()
.rindex()
.replace('x', 'X')
"""
# .find(), .rfind()
a = "Hit the ball before it hits you!"
b = a.find('it')
с = a.rfind('it')
print(b)
print(с)
# .index()
a = "Hit the ball before it hits you!"
f = a.index('h')
g = a.rindex('h')
print(f,g)
# .replace('x', 'X')
a = "Hit the ball before it hits you!"
t = a.replace("it", "at")
print(t)

# .split()
a = "Let there be light! ~ Because we want to fight! ~ All right!"
b = a.split('~')
print(b)

# .join(list)
list = ['Let', 'there', 'be', 'light']
variable = ";".join(list)
print(variable)

string = "4"
list1 = ["a", "b", "c"]
print(string.join(list1))










