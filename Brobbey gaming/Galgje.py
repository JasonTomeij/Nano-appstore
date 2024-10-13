import random
import time

def categoriseer_woorden(woordenlijst):
    makkelijk = []
    gemiddeld = []
    moeilijk = []

    for woord in woordenlijst:
        lengte = len(woord)
        if lengte <= 7:  
            makkelijk.append(woord)
        elif 7 <= lengte <= 10:  
            gemiddeld.append(woord)
        else:  
            moeilijk.append(woord)

    return makkelijk, gemiddeld, moeilijk

def galgje_spel():
    with open(r"C:\School\Semester-1\PROG-AI\PROG-1\Nano App Store\Nano-appstore\Brobbey gaming\galgjewoorden.txt", "r") as file:
        woordenlijst = file.readlines()

    woordenlijst = [woord.strip() for woord in woordenlijst]
    
    makkelijk, gemiddeld, moeilijk = categoriseer_woorden(woordenlijst)

    print("Kies een moeilijkheidsgraad: ")
    print("1. Makkelijk")
    print("2. Gemiddeld")
    print("3. Moeilijk")

    keuze = input("Voer het nummer van je keuze in (1/2/3): ")
    
    if keuze == '1':
        galgje_woord = random.choice(makkelijk).lower()
    elif keuze == '2':
        galgje_woord = random.choice(gemiddeld).lower()
    elif keuze == '3':
        galgje_woord = random.choice(moeilijk).lower()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return

    geraden_letters = []
    foute_beurten = 0
    max_foute_beurten = 6
    woord_geraden = False

    huidige_status = [" " if letter == " " else "_" for letter in galgje_woord]

    print("Welkom bij Galgje! Let op de woorden hebben te maken met XXX")
    time.sleep(1)
    print(f"Het woord heeft {len(galgje_woord)} tekens (inclusief spaties).")
    time.sleep(2)

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
        time.sleep(2)
    else:
        print("\nJammer, je hebt verloren. Het woord was: " + galgje_woord)
        time.sleep(2)


if __name__ == "__main__":
    galgje_spel()


#Bronnen 

# https://docs.python.org/3/tutorial/modules.html // Dit heeft mij heel goed gelopen en dan vooral 6 en 6.1.1 Dit heeft mij If __name__ geleerd! 
# Timesleep = https://www.datacamp.com/tutorial/python-time-sleep?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720821&utm_adgroupid=157156375191&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=716160943156&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9102671&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-row-p1_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-oct24&gad_source=1&gclid=CjwKCAjw3624BhBAEiwAkxgTOo9Cpb0aT_xw2c_eQ5y28NcWvyZRKgPUL5jBp3ilpj7CbwqFHXtIoBoC9HIQAvD_BwE // Onder Kop Time.sleep()
# Voorkennis studie
# Canvas --> Module 1 tot 9 
