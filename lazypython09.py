"""
Метод срок
string.isalpha() - все символы алфавитные
string.isalnum() - и алфавитные и цефровые символы
string.isdigit() - все символы в строке евляються цифрами
string.islower() - все символы из нижнего регистра
string.isupper() - все символы из верхнего регистра
string.istitle() - проверка на то что каждое слово начинается с буквы верхнего регистра
string.isspace() - проверка на наличие пробела
"""

string = "AAaa"
print(string.isalpha())

string = "AAaa001"
print(string.isalnum())

string = "02354"
print(string.isdigit())

string = "oerirnvpwin2"
print(string.islower())

string = "NEIFNIEVNEWS11"
print(string.isupper())

string = "A Table Is Round"
print(string.istitle())

string = "   "
print(string.isspace())

name = input("Hello this is a string validator. What is your name?: ")
a = input(name + ", type some symbols and hit Enter please: ")
if a.isdigit():
    print("You enter only digits.")
else:
    print("You entered one or more non-digits or not only digits.")