# У наредним задацима функције су задате у следећем формату:
# - func_name(var1: type, var2: type) -> type
# - func_name означава тражено име функције
# - var1: type и var2: type означавају параметре функције и њихове типове
# - -> type означава тип повратне вредности функције
# 1. Написати функцију list_sum(values: list) -> int која враћа збир елемената листе list_sum([5, 10, -2]) враћа 13
def list_sum(lista: list):
    sum = 0
    for i in lista:
        sum += i
    
    return int(sum)

print(list_sum([5, 10, -2]))
# 2. Написати функцију list_avg(values: list) -> float која враћа просек елемената листе list_avg([5, 10, 9]) враћа 8.0
def list_avg(lista: list):
    prosek = 0.0
    for i in lista:
        prosek += i

    return float(prosek / len(lista))

print(list_avg([5, 10, 9]))
# 3. Написати функцију min_of_two(x: int, y: int) -> int која враћа мањи од два броја min_of_two(19, 27) враћа 19
def min_of_two(x: int, y: int):
    if x > y:
        return int(y)
    else:
        return int(x)
print(min_of_two(19, 27))
# 4. Написати функцију min_of_three(x: int, y: int, z: int) -> int која враћа најмањи од три броја min_of_three(19, 13, 42) враћа 13
# Користите функцију min_of_two приликом имплементације
def min_of_three(x: int, y: int, z: int):
    najmanji_broj = min_of_two(x, y)
    if najmanji_broj > z:
        return int(z)
    else: 
        return int(najmanji_broj)

print(min_of_three(19,13,42))
# 5. Написати функцију max_of_two(x: int, y: int) -> int која враћа већи од два броја max_of_two(19, 27) враћа 27
def max_of_two(x: int, y: int):
    if x > y:
        return int(x)
    else:
        return int(y)
    
print(min_of_two(19, 27))
# 6. Написати функцију max_of_three(x: int, y: int, z: int) -> int која враћа највећи од три броја max_of_three(19, 13, 42) враћа 42
# Користите функцију max_of_two приликом имплементације
def max_of_three(x: int, y: int, z: int):
    najveci_broj = max_of_two(x, y)
    if najveci_broj > z:
        return int(najveci_broj)
    else: 
        return int(z)
    
print(max_of_three(19,13,42))
# 7. Користећи функцију crowd_category (из претходне вежба), написати функцију:
# is_large(attendance: int) -> bool која проверава да ли је прослеђена посета велика
# is_large(35000) враћа True
# is_large(15000) враћа False
# is_large(None) враћа False

def crowd_category(attendance):
    if attendance is None:
        return "Unknown"
    elif attendance < 15000:
        return "Small"
    elif attendance < 30000:
        return "Medium"
    else:
        return "Large"
    
def is_large(attendance: int):
    return crowd_category(attendance) == "Large"

is_large(35000)
is_large(15000)
is_large(None)
# 8. Написати функцију count_vowels(text: str) -> int која враћа број самогласника у тексту (a, e, i, o, u)
# count_vowels('programming in python') враћа 5


def count_vowels(text: str):
    vowels_list = ["a", "e", "i", "o", "u"]
    count = 0
    for t in text:
        if t in vowels_list:
            count += 1

    return count

count_vowels('programming in python')
# 9. Написати функцију min_and_max(values: list) -> tuple која враћа најмањи и највећи елемент листе
# min_and_max([5, 10, 9, 42, 40]) враћа (5, 42)

def min_and_max(values: list):
    minimum = min(values)
    maximum = max(values)
    return (minimum, maximum)

min_and_max([5, 10, 9, 42, 40])
# 10. Написати функцију get_larger_than(values, target) која враћа листу елемената већих од прослеђеног елемента
# Повратна вредност функције треба бити листа (тј. list)
# get_larger_than([5, 10, 9], 7) враћа [10, 9]
# get_larger_than([5, 10, 9, 42, 40], 9) враћа [10, 42, 40]

def get_larger_than(values, target):
    
    result = [v for v in values if v > target]

    return result

print(get_larger_than([5, 10, 9], 7))
print(get_larger_than([5, 10, 9, 42, 40], 9))
# 11. *Написати функцију fizz_buzz(n) која исписује бројеве од 1 до n са промењеним вредностима:
# Ако је број дељив са 3, исписати Fizz
# Ако је број дељив са 5, исписати Buzz
# Ако је број дељив и са 3 и са 5, исписати FizzBuzz
# Шта ако желимо да додамо и услов за дељивост са бројем 7?
# Ако је број дељив са 7, исписујемо Zazz
# Нпр. уместо 21 исписујемо FizzZazz
# Нпр. уместо 105 исписујемо FizzBuzzZazz

def fizz_buzz(n):
    
    count = 1
    while count < n:
        result = ""
        if count % 3 == 0:
            result += "Fizz"
        if count % 5 == 0:
            result += "Buzz"
        if count % 7 == 0:
            result += "Zazz"
        if result == "":
            result = str(count)

        
        print(result)
        count +=1

fizz_buzz(106)