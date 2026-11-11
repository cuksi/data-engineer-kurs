int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'

open("ne_postoji.pdf") # FileNotFoundError: [Errno 2] No such file or directory: 'ne_postoji.pdf'

x = [1,2,3,4]
x[5] # IndexError: list index out of range

employee = {"salary" : "55555"}
employee["bonus"]    # KeyError: 'bonus'

y = [1,2,3,4]
y["test"]   # TypeError: list indices must be integers or slices, not str

"42" + 5    # TypeError: can only concatenate str (not "int") to str

5 + "42"    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

a = []
sum(a) / len(a)     # ZeroDivisionError: division by zero
text = "abc"

try:
    n = int(text)
    print("Number: ", n)
except ValueError:
    print("Not a number", text)

print("Continues...")


text = "55"

try:
    n = int(text)
    print("Number: ", n)
except ValueError:
    print("Not a number", text)

print("Continues...")
def safe_average(values: list) -> float:
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:
        return 0.0

safe_average([])
text = "abc"

try:
    n = int(text)
    print("Number: ", n)
except ValueError as e:
    print("Error", e)
    print("Not a number", text)

print("Continues...")
print("34".isdigit())   # True
print("-34".isdigit())  # False
print("3.4".isdigit())  # False (Float izbacuje kao False)
print("asjf".isdigit()) # False
print("".isdigit())     # False
print("  7   ".isdigit())   # False
def is_number(text: str) -> bool:
    try:
        float(text)
        return True
        # return float(text)    # ako ovo uradimo onda ne bi otisao u except
    except ValueError:
        return False
    except Exception as e: # ovo je generalni except tj. ako se ne uklapa u gornji except
        print(e)    # ako vracamo ovo e onda mora da se upise Exception a ako necemo da vracamo onda samo except: i mozemo nesto da ispisemo ili nesto drugo
        print("Something is terribly wrong")
    
print(is_number("34"))   # True
print(is_number("-34"))  # True
print(is_number("3.4")) # True
print(is_number("asjf")) # False
print(is_number(""))     # False
print(is_number("  7   ")) # True

# Broj veci od 0
def is_valid_salary(text: str) -> bool:
    return is_number(text) and float(text) >= 0     # ako je ovo desno float(text) error a desno False nece ni proveravati ovaj float(text) jer je atumoatski False. 
                                                    # A da je True onda bi bio Error zato sto bi onda proveravao desnu stranu float(text)

# Lazy eval - lenjo izvrsavanja zato sto kad nema potrebe da proverava desnu stranu Python ce to preskociti
# and   
False and 5 // 0    # ako je ovo desno 5 // 0  error a desno False nece ni proveravati ovaj 5 // 0  jer je atumoatski False. A da je True onda bi bio Error zato sto bi onda proveravao desnu stranu 5 // 0 
# or
False or 5 // 0 # ovde i da je True i False nece ovo desno proveravati zato sto ima ispunjen jedan uslov ovaj drugi nije bitan i nece ga proveravati