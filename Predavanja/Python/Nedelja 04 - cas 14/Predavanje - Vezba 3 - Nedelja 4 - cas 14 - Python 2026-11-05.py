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