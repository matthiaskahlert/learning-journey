from urllib.request import urlopen
import re
import html

url = input("URL der Webseite: ")
try:
    htmltext = urlopen(url).read().decode()
except Exception:
    print("Webseite konnte nicht geöffnet werden.")
    exit()

# HTML-Entities entschlüsseln
htmltext = html.unescape(htmltext)

# Suche nach E-Mail-Adressen (auch mailto:)
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', htmltext)
emails += re.findall(r'mailto:([\w\.-]+@[\w\.-]+\.\w+)', htmltext)

# Duplikate entfernen
emails = list(set(emails))

if emails:
    print("Gefundene E-Mail-Adressen:")
    for mail in emails:
        print(mail)
else:
    print("Keine E-Mail-Adressen gefunden.")