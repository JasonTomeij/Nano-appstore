App_name = """
██████╗ ██████╗  ██████╗ ██████╗ ██████╗ ███████╗██╗   ██╗    ███╗   ██╗ █████╗ ███████╗██╗      ███████╗████████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝╚██╗ ██╔╝    ████╗  ██║██╔══██╗██╔════╝██║      ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝██║   ██║██████╔╝██████╔╝█████╗   ╚████╔╝     ██╔██╗ ██║███████║███████╗██║█████╗███████╗   ██║   ██║   ██║██████╔╝█████╗  
██╔══██╗██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══╝    ╚██╔╝      ██║╚██╗██║██╔══██║╚════██║██║╚════╝╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝  
██████╔╝██║  ██║╚██████╔╝██████╔╝██████╔╝███████╗   ██║       ██║ ╚████║██║  ██║███████║██║      ███████║   ██║   ╚██████╔╝██║  ██║███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝      ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
"""
introductie = "Welkom in de Brobbey Nasi-Store \nSpeel zoveel mogelijk spellen en vergeet niet een Nasietje te eten!\n"


print(App_name)
print(introductie)

def keuze_menu():
    print("Welk spel wil je spelen? ")


    print("[1] Raad het nummer spel")
    print("[2] Galgje ")
    print("[3] Raad de quote van de speler!")

keuze_menu()
keuze = int(input("Kies jouw keuze: "))

while keuze != 0:
    if keuze == 1:
        #Doe optie 1
        print("Test keuze1")
    elif keuze == 2:
        #doe keuze 2 
        print("Test keuze2")
    elif keuze == 3:
        #DOe keuze 3:
        print("Test keuze3")
    else:
        print("Dit is geen keuze")
    keuze_menu()
    keuze = int(input("Kies jouw keuze: "))

print("Dankjewel voor het spelen van Brobbey Nasi-Store")


