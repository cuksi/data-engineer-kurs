# 1. Напишите функцију goals_per_match(goals, matches) која враћа просек голова по утакмици, заокружен на две децимале.
def goals_per_match(goals, matches):
    return round(goals / matches, 2 )

goals_per_match(2, 1) # test
# 2. Напишите функцију scoreline(home_team, home_goals, away_goals, away_team) која враћа текст Kingsbridge City 3-1 Ashford Rovers.
def scoreline(home_team, home_goals, away_goals, away_team):
    return f"{home_team} {home_goals}-{away_goals} {away_team}"

print(scoreline("Kingsbridge City", 3, 1, "Ashford Rovers")) # test
# 3. Претворите разврставање посете из Сесије 1 у функцију crowd_category(attendance) која враћа категорију. Позовите је за None, 0, 15000 и 30000.
def crowd_category(attendance):
    if attendance is not None and attendance >= 30000:
        return "Large"
    elif attendance is not None and attendance >= 15000 and attendance < 30000:
        return "Medium"
    elif attendance is not None and attendance < 15000:
        return "Small"
    else:
        return "Unknown"

poseta = [None, 0, 15000, 30000]

for i in poseta:
    print(crowd_category(i))

print("Ispod resenje profe")

# Drugi nacin resenja od profe
def crowd_category2(attendance):
    if attendance is None:
        return "Unknown"
    elif attendance < 15000:
        return "Small"
    elif attendance < 30000:
        return "Medium"
    else:
        return "Large"
    
poseta = [None, 0, 15000, 30000]

for i in poseta:
    print(crowd_category2(i))
# 4. Напишите функцију added_minute(minute, added=None) која враћа 90+3, или само 90 када надокнада није наведена.
def added_minute(minute, added=None):
    if added is None:
        return f"{minute}"
    else:
        return f"{minute}+{added}"

print(added_minute(90))
print(added_minute(90,5))

print("Ispod resenje profe")

# Drugi nacin resenja od profe
def added_minute2(minute, added=None):
    if added is None:
        return f"{minute}"
    
    return f"{minute}+{added}"
    
print(added_minute2(90))
print(added_minute2(90,5))
# 5. Напишите функцију is_derby(home_city, away_city) која враћа True ако су оба клуба из истог града.
def is_derby(home_city, away_city):
    if home_city == away_city:
        return True
    else:
        return False

print(is_derby("Belgrade", "Belgrade"))

print(is_derby("Belgrade", "New Now"))

print("Ispod resenje profe")

# Drugi nacin resenja od profe
def is_derby2(home_city, away_city):
    return home_city == away_city
    
print(is_derby2("Belgrade", "Belgrade"))

print(is_derby2("Belgrade", "New Now"))