import random

# Leest woorden uit bestand
with open("C:\\School\\Semester-1\\PROG-AI\\PROG-1\\Nano App Store\\Nano-appstore\\galgjewoorden.txt", "r") as file:
    woordenlijst = file.readlines()

woordenlijst = [woord.strip() for woord in woordenlijst]

galgje_woord = random.choice(woordenlijst).lower()

geraden_letters = []
foute_beurten = 0
max_foute_beurten = 6
woord_geraden = False

huidige_status = ["_" for _ in galgje_woord]

print("Welkom bij Galgje!")
print(f"Het woord heeft {len(galgje_woord)} letters.")

while not woord_geraden and foute_beurten < max_foute_beurten:

    print("\nHuidige status: " + " ".join(huidige_status))
    print(f"Je hebt {foute_beurten}/{max_foute_beurten} fouten gemaakt.")
    
    gok = input("Raad een letter: ").lower()

    if len(gok) != 1 or not gok.isalpha():
        print("Voer een geldige letter in!")
        continue

    
    if gok in geraden_letters:
        print("Je hebt deze letter al geraden. Probeer een andere.")
        continue

    
    geraden_letters.append(gok)

    if gok in galgje_woord:
        print(f"Goed gedaan! De letter '{gok}' zit in het woord.")
        for i, letter in enumerate(galgje_woord):
            if letter == gok:
                huidige_status[i] = gok
    else:
        foute_beurten += 1
        print(f"Helaas, de letter '{gok}' zit niet in het woord.")

    if "_" not in huidige_status:
        woord_geraden = True

if woord_geraden:
    print("\nGefeliciteerd! Je hebt het woord geraden: " + galgje_woord)
else:
    print("\nJammer, je hebt verloren. Het woord was: " + galgje_woord)

