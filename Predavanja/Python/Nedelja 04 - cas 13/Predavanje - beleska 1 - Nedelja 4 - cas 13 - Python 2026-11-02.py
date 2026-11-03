# This is a comment
# This is one cell
print('Hello World!')
# String
user_name = 'Pera'
# Da nemesemo navodnike, profa koristi jednostruke '
team_name = "Northport United"

name = 'Matteo O\'Brien'    # Escape \' -> '
name = "Matteo O'Brien"     # Ovde name Escape, ali ako nam trebaju dvostruki navodnici onda mozemo da koristimo isti escape za "

# Numbers: Integer, Float
attendance = 52000
hourly_wage = 25.47

# Boolean (True / False)
has_roof = True
is_caregiver = False

# None
testing = None  # None u Pthonu je u stvari NULL

print(user_name, team_name, attendance, hourly_wage, has_roof, is_caregiver)
print(type(user_name), type(team_name), type(attendance), type(hourly_wage), type(has_roof), type(is_caregiver), type(testing))
# Operators
x = 2
y = 3

# Arithmetic
print(x + y)
print(x - y)
print(x * y)
print(x ** y)   # x na y (x na kvadrat i tako to, ako treba na treci onda x***y)
print(x / y)

print(x // y)   # Kos crta predstavlja celobrojno deljenje
print( x % y)   # za ostatak

# String "arithmetic"
x = 2
s1 = "Text 1"
s2 = "Something else"
s3 = "3"

print(s1 + " " + s2)
print(s1 + s3)
# print(s3 + x)     # TypeError: can only concatenate str (not "int") to str
# print(x + s3)       # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(s3 + str(x))
print(x + int(s3))

# print(x + int(s1))  # ValueError: invalid literal for int() with base 10: 'Text 1'
# WHERE column IN ("A", "B", "C")

# List
weather_condtions = ["fog", "clear", "snow", "rain"]

print(type(weather_condtions))

print(weather_condtions)
print(len(weather_condtions))
attendance = [32454, 23456, 32981, 21345, 29945]

print("First element of list: ", attendance[0])
print("Second element of list: ", attendance[1])
print("Last element of list: ", attendance[4])

# print("Last element of list: ", attendance[len(attendance)])    # IndexError: list index out of range, jer nam je zadnji index len -1
print("Last element of list: ", attendance[len(attendance) - 1]) 
print("Last element of list: ", attendance[-1])     # Ovo je zadnji index, broj u nazad paython, moze i -2, -3 ....

# print("Last element of list: ", attendance[77])     # IndexError: list index out of range