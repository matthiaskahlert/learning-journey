from urllib.request import urlopen


WDR = 'https://www1.wdr.de/index.html'
f = urlopen(WDR)  #1
htmltext = f.read().decode()  #2
f.close()

liste = htmltext.split('Max:')  #3
heute = liste[1].split('°')[0]  #4
morgen = liste[2].split('°')[0]  #5

print('Wie warm wird es?')
print(f'Höchsttemperatur heute: {heute} °C')
print(f'Höchsttemperatur morgen: {morgen} °C')