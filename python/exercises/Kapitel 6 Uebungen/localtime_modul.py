from time import *
zeitpunkt = localtime()
print(zeitpunkt.tm_year) # 2025
print(zeitpunkt.tm_mon) # 12

# uhr
from time import localtime, sleep
durchlauf = 0
max_durchlaeufe = 5
# Diese Schleife zeigt die aktuelle Uhrzeit alle 10 Sekunden an
# Abbruch erfolgt bei max_durchlaeufe = 5
while True:
    zeit = localtime()
    print(zeit.tm_hour, 'Uhr', zeit.tm_min, 'und',zeit.tm_sec, 'Sekunden')
    
    durchlauf += 1
    if durchlauf >= max_durchlaeufe:
        print("Maximale Durchläufe erreicht, Schleife beendet.")
        break

    sleep(10)
