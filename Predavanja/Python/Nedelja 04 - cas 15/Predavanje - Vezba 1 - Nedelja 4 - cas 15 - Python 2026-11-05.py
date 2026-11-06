# У наредним задацима функције су задате у формату: func_name(var1: type, var2: type) -> type
# func_name означава тражено име функције
# var1: type и var2: type означавају параметре функције и њихове типове
# -> type означава тип повратне вредности функције
# На пример get_endpoints(data: tuple) -> tuple
# Функција мора да се зове get_endpoints, да прима један параметар типа tuple и да сама враћа tuple
# 1. Написати функцију get_endpoints(data: tuple) -> tuple која враћа први и последњи елемент 
# get_endpoints((10, 20, 30, 40)) враћа (10, 40)
test1 = ((10, 20, 30, 40))

def get_endpoints(tuplee):    
    return (tuplee[0], tuplee[-1])

print(get_endpoints(test1))
# 2. Написати функцију get_unique_items(items: tuple) -> tuple која враћа торку без дупликата
# get_unique_items((1, 2, 2, 3, 1, 4)) враћа (1, 2, 3, 4)
test2 = ((1, 2, 2, 3, 1, 4))

def get_unique_items(tuplee):
    return tuple(set(tuplee))

print(get_unique_items(test2))
# 3. Написати функцију safe_lookup(data: dict, key: str) -> str која безбедно дохвата из речника
# Ако је кључ пронађен у речнику, вратити вредност за тај кључ
# safe_lookup({'name': 'Alice'}, 'name') враћа 'Alice'
# Ако кључ није пронађен у речнику, вратити 'Not Found'
# safe_lookup({'name': 'Alice'}, 'age') враћа 'Not Found'

def safe_lookup(dict, str):
    return dict.get(str, "Not Found")

print(safe_lookup({'name': 'Alice'}, 'name'))

print(safe_lookup({'name': 'Alice'}, 'age'))
# 4.  Написати функцију find_difference(set1: set, set2: set) -> set која враћа разлику два скупа
# find_difference({1, 2, 3}, {2, 3, 4}) враћа {1}
# find_difference({1, 2, 3, 5, 6}, {2, 3, 4}) враћа {1, 5, 6}

def find_difference(set1, set2):
    return set1 - set2

print(find_difference({1, 2, 3}, {2, 3, 4}))
print(find_difference({1, 2, 3, 5, 6}, {2, 3, 4}))
# 5. Написати функцију merge_inventories(inv1: dict, inv2: dict) -> dict која спаја складишта две продавнице
# Input: {'apples': 3, 'bananas': 2}, {'bananas': 4, 'oranges': 1}
# Output: {'apples': 3, 'bananas': 6, 'oranges': 1}
test3 = {'apples': 3, 'bananas': 2}
test4 = {'bananas': 4, 'oranges': 1}

# def merge_inventories(inv1, inv2):    ako se pokrece ovo resenje komentirati donje resenje jer dictionary pamti vrednost ako mu je menjamo unutar funkcije pamti je i spolja
#     for i in inv2:
#         if i in inv1:
#             inv1[i] += inv2[i]
#         else:
#             inv1[i] = inv2[i]
#     return inv1

# merge_inventories(test3, test4)

# resenje profe
def merge_inventories2(inv1, inv2):
    merged = dict(inv1)

    for iteam, quantity in inv2.items():
        merged[iteam] = merged.get(iteam, 0) + quantity
    return merged


merge_inventories2(test3, test4)
# 6. Написати функцију filter_allowed_keys(data: dict, allowed: set) -> dict која филтрира дозвољене вредности (приватност података)
# Input: {'username': 'alice', 'email': 'a@test.com', 'password': '123'}, {'username', 'email'}
# Output: {'username': 'alice', 'email': 'a@test.com'}
test5 = {'username': 'alice', 'email': 'a@test.com', 'password': '123'}
test6 = {'username', 'email', 'address'}

def filter_allowed_keys(data, allowed):
    novi = {}
    for i in allowed:
        if i in data:
            novi[i] = data[i]
    return novi

filter_allowed_keys(test5, test6)
# 7. Написати функцију group_by_length(words: set) -> dict која групише речи по дужини
# Input 1: {'a', 'to', 'is', 'car', 'dog'}
# Output 1: {1: ['a'], 2: ['to', 'is'], 3: ['car', 'dog']}
# Input 2: {'team', 'score', 'goal', 'point', 'draw'}
# Output 2: {5: ['point', 'score'], 4: ['team', 'draw', 'goal']}
test7 = {'a', 'to', 'is', 'car', 'dog'}
test8 = {'team', 'score', 'goal', 'point', 'draw'}

def group_by_length(words):
    final_dict = {}
    for i in words:
        duzina_reci = len(i)
        if duzina_reci not in final_dict:
            final_dict[duzina_reci] = [i]
        else:
            final_dict[duzina_reci].append(i)

    return final_dict

print(group_by_length(test7))
print(group_by_length(test8))