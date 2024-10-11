import random

max_getal, aantal_pogingen = 10, 3
geheim_getal = random.randint(1, max_getal)

print(f"Raad het getal tussen 1 en {max_getal} in {aantal_pogingen} pogingen.")

for poging in range(1, aantal_pogingen + 1):
    gok = int(input(f"Poging {poging}: "))
    
    if gok == geheim_getal:
        print(f"Gefeliciteerd! {geheim_getal} is correct.")
        break
    print("Hoger!" if gok < geheim_getal else "Lager!")

if gok != geheim_getal:
    print(f"Helaas, het juiste getal was {geheim_getal}.")
