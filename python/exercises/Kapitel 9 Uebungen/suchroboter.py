from urllib.request import urlopen

url = input("URL der Webseite: ")
try:
    html = urlopen(url).read().decode()
except Exception:
    print("Webseite konnte nicht geöffnet werden.")
    exit()

# Preprocessing: Ersetze Anführungszeichen und > durch Leerzeichen
for ch in "\"'>":
    html = html.replace(ch, " ")

fragmente = html.split()
urls = [f for f in fragmente if (f.startswith("http://") or f.startswith("https://")) and f.endswith(".html")]

if urls:
    print("Gefundene URLs:")
    for link in urls:
        print(link)
else:
    print("Keine passenden URLs gefunden.")