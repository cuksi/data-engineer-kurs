# Određivanje doba dana. Napisati Python program koji za svaki sat u toku dana
# (od 0 do 23) ispisuje odgovarajuće doba dana:
# noć (od 22 do 6 časova),
# jutro (od 6 do 12 časova),
# popodne (od 12 do 18 časova) ili
# veče (od 18 do 22 časa).
sat = 0
for i in range(0, 24, 1):
    if sat >= 6 and sat < 12:
        print("jutro")
    elif sat >= 12 and sat < 18:
        print("popodne")
    elif sat >= 18 and sat < 22:
        print("veče")
    else:
        print("noć")
    
    sat += 1