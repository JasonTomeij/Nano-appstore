import time
import NummerRaadSpel
import Galgje


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
time.sleep(2)
print(introductie)
time.sleep(2)

def keuze_menu():
    print("Welk spel wil je spelen? ")


    print("[1] Raad het nummer spel")
    print("[2] Galgje ")
    print("[3] Raad de quote van de speler!")

keuze_menu()
keuze = int(input("Kies jouw keuze: "))

while keuze != 0:
    if keuze == 1:
        NummerRaadSpel.raad_getal_spel()
        time.sleep(2)
        break
    elif keuze == 2:
        Galgje.galgje_spel()
        break
    elif keuze == 3:
        #DOe keuze 3:
        print("Test keuze3")
    else:
        print("Dit is geen keuze")
        time.sleep(2)
    keuze_menu()
    keuze = int(input("Kies jouw keuze: "))

print("Dankjewel voor het spelen van Brobbey Nasi-Store")



# https://docs.python.org/3/tutorial/modules.html // Dit heeft mij heel goed gelopen en dan vooral 6 en 6.1.1 Dit heeft mij If __name__ geleerd! 
# Timesleep = https://www.datacamp.com/tutorial/python-time-sleep?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720821&utm_adgroupid=157156375191&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=716160943156&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9102671&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-row-p1_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-oct24&gad_source=1&gclid=CjwKCAjw3624BhBAEiwAkxgTOo9Cpb0aT_xw2c_eQ5y28NcWvyZRKgPUL5jBp3ilpj7CbwqFHXtIoBoC9HIQAvD_BwE // Onder Kop Time.sleep()
# Voorkennis studie -- Met name van Import module - Random en Timesleep 
# Canvas --> Module 1 tot 9 
# Introductie Brobbey nasi store --> Gekopieerd vanuit deze link: https://patorjk.com/software/taag/#p=display&f=Modular&t=Nano%20App%20Store
# Poster gemaakt met Canva! 
#Github link --> https://github.com/JasonTomeij/Nano-appstore.git


