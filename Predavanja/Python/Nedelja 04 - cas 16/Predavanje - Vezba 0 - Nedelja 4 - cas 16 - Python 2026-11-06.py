# 1) Написати конвертор валута. Сачувај курсеве у односу на евро: `{‘USD’: 1.08, ‘RSD’: 117.2, ‘GBP’: 0.85}` 
# Функција прима валуту (str) и количину за конверзију (float)

def convert_euro(currency, amount):
    referent_values = {"USD": 1.08, "RSD": 117.2, "GBP": 0.85}
    return f"You will get for {amount} EUR = {referent_values[currency] * amount} {currency}"

print(convert_euro("RSD", 110.0))
# 2) Написати функцију available_books(library: dict) -> list која враћа листу књига које се могу позајмити
# Вредност True означава да је књига доступна, а False да је позајмљена
# available_books({'1984': True, 'Дина': False, 'Хобит': True}) враћа ['1984', 'Хобит']
test1 = {"1984": True, "Дина": False, "Хобит": True}

def available_books(library):
    temp = []
    for i in library:
        if library[i]:
            temp.append(i)

    return temp

print(available_books(test1))
# 3) Написати функцију grades_average(grades: list) -> float која враћа просек описних оцена
# За податке, користити речник: {'одличан': 5, 'врлодобар': 4, 'добар': 3, 'довољан': 2, 'недовољан': 1}
# grades_average(['одличан', 'добар', 'врлодобар']) враћа 4.0
test2 = ["одличан", "добар", "врлодобар"]

def grades_average(grades):
    grade_dict = {"одличан": 5, "врлодобар": 4, "добар": 3, "довољан": 2, "недовољан": 1}
    sum = 0.0
    count = 0
    for i in grades:
        sum += grade_dict[i]
        count += 1

    return sum / count

print(grades_average(test2))
# 4) Написати функцију count_votes(votes: list) -> dict која враћа број гласова за сваку опцију
# count_votes(['пица', 'бургер', 'пица', 'такос', 'пица', 'бургер']) враћа {'пица': 3, 'бургер': 2, 'такос': 1}
test3 = ["пица", "бургер", "пица", "такос", "пица", "бургер"]

def count_votes(votes):
    total_votes = {}
    for i in votes:
        if i in total_votes:
            total_votes[i] += 1
        else:
            total_votes[i] = 1

    return total_votes

print(count_votes(test3))
# 5) Користећи функцију count_votes, написати функцију winner(votes: list) -> str која враћа опцију са највише гласова
# winner(['пица', 'бургер', 'пица', 'такос', 'пица', 'бургер']) враћа 'пица'

def winner(votes: list):
    winner_dict = count_votes(votes)
    winner_votes = 0
    category = ""
    for i in winner_dict:
        if winner_dict[i] > winner_votes:
            winner_votes = winner_dict[i]
            category = i
    
    return category

print(winner(test3))
# 6) Написати функцију translate(dictionary: dict, word: str) -> str која враћа превод енглеске речи на српски
# Ако реч не постоји у речнику, функција враћа None
# translate({'hello': 'здраво', 'thanks': 'хвала', 'water': 'вода'}, 'water') враћа 'вода'
# translate({'hello': 'здраво', 'thanks': 'хвала', 'water': 'вода'}, 'bread') враћа None
test4 = {"hello": "здраво", "thanks": "хвала", "water": "вода"}

def translate(dictionary: dict, word: str):
    return dictionary.get(word)

print(translate(test4, "water"))
print(translate(test4, "bread"))