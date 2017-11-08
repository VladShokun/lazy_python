# String indexing
# 0, 1, 2, 3, 4, 5, 6, 7...
a = "Hello!"
print(a[0])
print(a[1])
b = a[2]
print(b)

# Backward indexing
# -1, -2, -3, -4...
print(a[-3])
print(a[-2])

# Slicing
a = 'Hello world!'
b = a[0:6]
print(b)
c = a[0:-3]
print(c)

# experimrnt
p = "По небу звездочка летит и красоту Рисует таинство несбыточных мгновений...Во тьме предутренней усталый, на ходу, Предвосхищаю неземное вдохновенье!"
print(p)
print(len(p))
print(p[126:135]+p[12:23])
# Slicing 2
a ="Эта та самая строка, над которой мы шаманим"
b =a[4:12]
print(b)

#  Methods
# .capitalize()
a = 'kick the ball before the ball kicks you!'
b = a.capitalize()
print(b)
# .upper()
a = 'kick the ball before the ball kicks you!'
b = a.upper()
print(b)
# .lower()
a = 'KICK THE BALL BEFORE THE BALL KICKS YOU!'
b = a.lower()
print(b)
# .title()
a = 'kick the ball before the ball kicks you!'
print(a.title())
b = a.title()
print(b)
# swapcase()
a = 'Kick The Ball Before The Ball Kicks You!'
print(a.swapcase())
b = a.swapcase()
print(b)












