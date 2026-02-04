"""Erstelle ein Python-Programm für ein Spieler-Inventarsystem mit folgenden Anforderungen:
Datenstrukturen
1. Rucksack (Dictionary)

Kapazität: 10 Items (Gewicht: 1 pro Item)
Kann verschiedene Datentypen enthalten

2. Truhe/Chest (Dictionary, z.B. chest_01)

Kapazität: 100 Gewichtseinheiten
Maximale Item-Slots: 4 verschiedene Item-Typen
Kann verschiedene Datentypen enthalten

3. Item-Typen mit Eigenschaften:

Waffen: name, schaden, gewicht, stacklimit, itemID
Rüstungen: name, rüstungswert, gewicht, stacklimit, itemID
Währungen: name, wert, stacklimit, itemID
Tränke: name, wirkung, expirationdate, stacklimit, itemID
Crafting-Materialien: name, verwendung, stacklimit, itemID


Funktionen
a) fill_backpack()

Füllt den Rucksack mit zufälligen Items aus allen fünf Item-Typen
Beachtet Rucksack-Kapazität (10 Items)

b) add_to_chest(item_id, quantity, chest)

Verschiebt ausgewählte Items vom Rucksack in die Truhe
Parameter: item_id, quantity, chest
Validierung:

Gewichtslimit (100 Einheiten)
Slot-Limit (maximal 4 verschiedene Item-Typen)


Fehlermeldungen bei Überschreitung

c) quick_fill_chest(chest)

Verschiebt alle Items vom Rucksack in die Truhe
Bedingung: Item-Typ muss bereits in der Truhe vorhanden sein
Füllt bis zum Stack-Limit, nutzt bei Bedarf weitere Slots
Beachtet Slot- und Gewichtslimits

d) view_and_remove_items(container)

Parameter: container (Rucksack oder Truhe)
Zeigt Inventar-Inhalt an
Ermöglicht dem Spieler, Items zu entfernen

e) empty_chest_to_backpack(chest)

Verschiebt alle Items aus der Truhe in den Rucksack
Nur wenn Platz im Rucksack verfügbar ist
Fehlermeldung bei zu wenig Platz

f) create_new_chest(chest_name)

Erstellt neue Truhe mit identischen Eigenschaften (z.B. chest_02)
Parameter: chest_name für individuelle Benennung

g) main()

Hauptfunktion mit Benutzer-Interface (Menü)
Ermöglicht Aufrufen aller Funktionen (a-f)
Benutzerfreundliche Navigation


Zusätzliche Anforderungen

Implementiere Stack-Limits für alle Item-Typen
Verwende sinnvolle Fehlerbehandlung und klare Ausgaben
Stelle sicher, dass alle Gewichts- und Slot-Beschränkungen eingehalten werden"""
import random
from datetime import datetime, timedelta

# Globale Item-Datenbank
ITEM_DATABASE = {
    "Waffen": [
        {"name": "Schwert", "schaden": 50, "gewicht": 5, "stacklimit": 1},
        {"name": "Bogen", "schaden": 35, "gewicht": 3, "stacklimit": 1},
        {"name": "Dolch", "schaden": 25, "gewicht": 2, "stacklimit": 1},
    ],
    "Rüstungen": [
        {"name": "Plattenrüstung", "rüstungswert": 100, "gewicht": 10, "stacklimit": 1},
        {"name": "Lederrüstung", "rüstungswert": 50, "gewicht": 5, "stacklimit": 1},
    ],
    "Währungen": [
        {"name": "Gold", "wert": 1, "stacklimit": 1000},
        {"name": "Silber", "wert": 0.1, "stacklimit": 5000},
    ],
    "Tränke": [
        {"name": "Heiltrank", "wirkung": "Heilt 50 HP", "stacklimit": 10},
        {"name": "Manatrank", "wirkung": "Stellt 30 Mana wieder her", "stacklimit": 10},
    ],
    "Crafting-Materialien": [
        {"name": "Eisenerz", "verwendung": "Schmieden", "stacklimit": 50},
        {"name": "Holz", "verwendung": "Zimmern", "stacklimit": 100},
    ]
}

# Globale Variablen
backpack = {}
chests = {}
item_counter = 1

def generate_item_id():
    """Generiert eine eindeutige Item-ID"""
    global item_counter
    item_id = item_counter
    item_counter += 1
    return item_id

def create_item(item_type):
    """Erstellt ein Item mit allen notwendigen Eigenschaften"""
    template = random.choice(ITEM_DATABASE[item_type])
    item = template.copy()
    item["itemID"] = generate_item_id()
    item["typ"] = item_type
    item["gewicht"] = item.get("gewicht", 1)
    item["quantity"] = 1
    
    if item_type == "Tränke":
        item["expirationdate"] = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    
    return item

def fill_backpack():
    """Füllt den Rucksack mit zufälligen Items"""
    global backpack
    backpack = {}
    
    item_types = list(ITEM_DATABASE.keys())
    items_to_add = min(10, random.randint(5, 10))
    
    for _ in range(items_to_add):
        item_type = random.choice(item_types)
        item = create_item(item_type)
        backpack[item["itemID"]] = item
    
    print(f"\n✓ Rucksack wurde mit {len(backpack)} Items gefüllt!")
    view_container(backpack, "Rucksack")

def calculate_weight(container):
    """Berechnet das Gesamtgewicht eines Containers"""
    return sum(item["gewicht"] * item["quantity"] for item in container.values())

def count_item_types(container):
    """Zählt die verschiedenen Item-Typen in einem Container"""
    return len(set(item["typ"] for item in container.values()))

def add_to_chest(item_id, quantity, chest_name):
    """Fügt Items vom Rucksack zur Truhe hinzu"""
    if chest_name not in chests:
        print(f"✗ Truhe '{chest_name}' existiert nicht!")
        return
    
    if item_id not in backpack:
        print(f"✗ Item mit ID {item_id} nicht im Rucksack gefunden!")
        return
    
    chest = chests[chest_name]
    item = backpack[item_id]
    
    if item["quantity"] < quantity:
        print(f"✗ Nicht genügend Items im Rucksack! Verfügbar: {item['quantity']}")
        return
    
    # Prüfe Gewichtslimit
    item_weight = item["gewicht"] * quantity
    current_weight = calculate_weight(chest)
    
    if current_weight + item_weight > 100:
        print(f"✗ Gewichtslimit überschritten! Aktuell: {current_weight}, Hinzufügen: {item_weight}, Limit: 100")
        return
    
    # Prüfe Item-Typ-Limit
    if item_id not in chest:
        current_types = count_item_types(chest)
        if current_types >= 4:
            print(f"✗ Slot-Limit erreicht! Maximal 4 verschiedene Item-Typen erlaubt.")
            return
    
    # Verschiebe Items
    if item_id in chest:
        chest[item_id]["quantity"] += quantity
    else:
        chest[item_id] = item.copy()
        chest[item_id]["quantity"] = quantity
    
    backpack[item_id]["quantity"] -= quantity
    if backpack[item_id]["quantity"] == 0:
        del backpack[item_id]
    
    print(f"✓ {quantity}x {item['name']} zur Truhe '{chest_name}' hinzugefügt!")

def quick_fill_chest(chest_name):
    """Füllt die Truhe schnell mit allen passenden Items aus dem Rucksack"""
    if chest_name not in chests:
        print(f"✗ Truhe '{chest_name}' existiert nicht!")
        return
    
    chest = chests[chest_name]
    items_moved = 0
    
    # Nur Items verschieben, deren Typ bereits in der Truhe ist
    for item_id in list(backpack.keys()):
        item = backpack[item_id]
        
        # Prüfe ob Item-Typ bereits in Truhe
        type_in_chest = any(chest_item["typ"] == item["typ"] for chest_item in chest.values())
        
        if type_in_chest:
            quantity = item["quantity"]
            
            # Prüfe Gewichtslimit
            item_weight = item["gewicht"] * quantity
            current_weight = calculate_weight(chest)
            
            if current_weight + item_weight <= 100:
                if item_id in chest:
                    chest[item_id]["quantity"] += quantity
                else:
                    chest[item_id] = item.copy()
                
                del backpack[item_id]
                items_moved += quantity
    
    print(f"✓ {items_moved} Items wurden zur Truhe verschoben!")

def view_container(container, name):
    """Zeigt den Inhalt eines Containers an"""
    if not container:
        print(f"\n{name} ist leer!")
        return
    
    print(f"\n=== {name} ===")
    print(f"Gewicht: {calculate_weight(container)}/{'10' if name == 'Rucksack' else '100'}")
    print(f"Item-Typen: {count_item_types(container)}/{'10' if name == 'Rucksack' else '4'}")
    print("-" * 60)
    
    for item_id, item in container.items():
        print(f"ID: {item_id} | {item['name']} ({item['typ']}) x{item['quantity']}")
        
        if item["typ"] == "Waffen":
            print(f"  → Schaden: {item['schaden']}, Gewicht: {item['gewicht']}")
        elif item["typ"] == "Rüstungen":
            print(f"  → Rüstungswert: {item['rüstungswert']}, Gewicht: {item['gewicht']}")
        elif item["typ"] == "Währungen":
            print(f"  → Wert: {item['wert']}")
        elif item["typ"] == "Tränke":
            print(f"  → Wirkung: {item['wirkung']}, Ablauf: {item['expirationdate']}")
        elif item["typ"] == "Crafting-Materialien":
            print(f"  → Verwendung: {item['verwendung']}")

def view_and_remove_items(container_name):
    """Zeigt Container-Inhalt und ermöglicht das Entfernen von Items"""
    if container_name == "Rucksack":
        container = backpack
    elif container_name in chests:
        container = chests[container_name]
    else:
        print(f"✗ Container '{container_name}' nicht gefunden!")
        return
    
    view_container(container, container_name)
    
    if not container:
        return
    
    choice = input("\nItem entfernen? (ID eingeben oder Enter zum Abbrechen): ").strip()
    
    if choice:
        try:
            item_id = int(choice)
            if item_id in container:
                quantity = int(input(f"Wie viele entfernen? (Max: {container[item_id]['quantity']}): "))
                
                if quantity <= container[item_id]["quantity"]:
                    container[item_id]["quantity"] -= quantity
                    
                    if container[item_id]["quantity"] == 0:
                        del container[item_id]
                    
                    print(f"✓ {quantity} Item(s) entfernt!")
                else:
                    print("✗ Ungültige Anzahl!")
            else:
                print("✗ Item-ID nicht gefunden!")
        except ValueError:
            print("✗ Ungültige Eingabe!")

def empty_chest_to_backpack(chest_name):
    """Leert die Truhe in den Rucksack"""
    if chest_name not in chests:
        print(f"✗ Truhe '{chest_name}' existiert nicht!")
        return
    
    chest = chests[chest_name]
    items_moved = 0
    
    for item_id in list(chest.keys()):
        item = chest[item_id]
        
        # Prüfe Platz im Rucksack
        if len(backpack) >= 10:
            print(f"✗ Rucksack voll! {items_moved} Items wurden verschoben.")
            return
        
        if item_id in backpack:
            backpack[item_id]["quantity"] += item["quantity"]
        else:
            backpack[item_id] = item.copy()
        
        items_moved += item["quantity"]
        del chest[item_id]
    
    print(f"✓ Truhe geleert! {items_moved} Items wurden in den Rucksack verschoben.")

def create_new_chest(chest_name):
    """Erstellt eine neue Truhe"""
    if chest_name in chests:
        print(f"✗ Truhe '{chest_name}' existiert bereits!")
        return
    
    chests[chest_name] = {}
    print(f"✓ Truhe '{chest_name}' wurde erstellt!")

def main():
    """Hauptmenü"""
    print("=" * 60)
    print("  WILLKOMMEN ZUM INVENTARSYSTEM")
    print("=" * 60)
    
    # Erstelle Standard-Truhe
    create_new_chest("chest_01")
    
    while True:
        print("\n" + "=" * 60)
        print("HAUPTMENÜ")
        print("=" * 60)
        print("1. Rucksack mit zufälligen Items füllen")
        print("2. Item zur Truhe hinzufügen")
        print("3. Schnell-Füllen (Rucksack → Truhe)")
        print("4. Inventar anzeigen / Items entfernen")
        print("5. Truhe leeren (Truhe → Rucksack)")
        print("6. Neue Truhe erstellen")
        print("7. Alle Truhen anzeigen")
        print("0. Beenden")
        
        choice = input("\nWähle eine Option: ").strip()
        
        if choice == "1":
            fill_backpack()
        
        elif choice == "2":
            view_container(backpack, "Rucksack")
            chest_name = input("\nTruhen-Name (z.B. chest_01): ").strip()
            try:
                item_id = int(input("Item-ID: "))
                quantity = int(input("Anzahl: "))
                add_to_chest(item_id, quantity, chest_name)
            except ValueError:
                print("✗ Ungültige Eingabe!")
        
        elif choice == "3":
            chest_name = input("Truhen-Name: ").strip()
            quick_fill_chest(chest_name)
        
        elif choice == "4":
            print("\nVerfügbare Container:")
            print("- Rucksack")
            for chest_name in chests.keys():
                print(f"- {chest_name}")
            
            container = input("\nContainer-Name: ").strip()
            view_and_remove_items(container)
        
        elif choice == "5":
            chest_name = input("Truhen-Name: ").strip()
            empty_chest_to_backpack(chest_name)
        
        elif choice == "6":
            chest_name = input("Name der neuen Truhe: ").strip()
            create_new_chest(chest_name)
        
        elif choice == "7":
            print("\nVerfügbare Truhen:")
            for chest_name in chests.keys():
                view_container(chests[chest_name], chest_name)
        
        elif choice == "0":
            print("\nAuf Wiedersehen!")
            break
        
        else:
            print("✗ Ungültige Option!")

if __name__ == "__main__":
    main()
# Bugs: 
# gewichtslimit im rucksack geht nicht, beim füllen des backpacks werden items in den rucksack getan die die kapazität übersteigen. 
# zudem ist das cap von 10 hardgecoded, hier braucht es eine variable, 
# items stacken nicht richtig, braucht weitere tests, ist eine neue id notwendig, wenn sich nur die menge ändert? es soll sich dann nur die anzahl ändern
# quick fill füllt kategorie und nicht item durch die anwendung von chest_item["typ"] == item["typ"]

# feature request 1:truhen namensliste anzeigen beim erstellen von neuen truhen
# feature request 2: einzelne items aus truhe entnehmen
# feature request 3: items anlegen an charakter
# feature request 4: die funktion fill_backpack soll als lootausschüttung auch beim bekämpfen von monstern genutzt werden, dafür brauchen wir eine random liste an monstern mit sinnvollen werten.
# monster können nur bekämpft werden, wenn charakter eine waffe ausgerüstet hat und der rucksack nicht zu schwer ist.
# charakter hat hitpoints und heiltränke füllen diese nach oder im kampf wieder auf.
# character kann sterben, wenn hitpoints auf null. dann brauchen wir einen death screen, wo der charakter wiederbelebt werden kann gege  gold. ein dialog wie: ein böser magier kommt vorbei, der deine seele einsammelt, aber gegen gold lässt er dich nochmal frei.
# kampfsimulation ist rundenbasiert und  muss angriffs und verteidigungswert berechnen basierend auf ausrüstung und basiswerten der entitäten characvter und monster.
# im kampfsystem soll es auch kritische treffer geben, die kritische trefferwahrscheinlichkeit soll vom charakter und monster abhängen.
# nutzer kann entscheiden ob er angreift, sich heilt, flieht. 
# character muss sich bewegen können in einer einfachen map, wo monster spawnen. movement soll über eingabe von richtungen (nord, süd, ost, west) funktionieren.
# es gibt räume, jeder raum hat eine gewisse chance auf ein monster. je mehr schritte der charactert von der base entfernt ist, desto höher der angriffs und verteidigungswert der monster. 
# die räume müssen gespeichert werden, also die map soll einfach als dictionary mit räumen und deren inhalten (monster, items) realisiert werden.
# es muss verschiedene monsterkategorien geben: nornmale monster und boss monster. boss monster haben speziellen loot, sind aber auch schwer zu bekämpfen.
# zudem soll der character die items auch verkaufen können, er bekommt einen entsprechenden gegenwert vom händler.
# der händler soll auch items anbieten können wie tränke oder ausrüstung.
# über die crafting materialien soll der user blöcke erstellen können um sich eine base zu bauen. 
# der sinn der base könnte sein, dass der character dort sicher ist vor monstern und sich ausruhen kann um hp und mana wiederherzustellen.
# das menü muss also die option haben sich auszuruhen, wenn base vorhanden. character kann sich nur ausruhen, wenn er ein feuer gemacht hat und ein bett gecraftet hat. 
# es muss eine liste erstellt werden, die die craftbaren items beinhaltet und entsprechend ein crafting menü, in dem der user interagiert. 
# craften soll nur zuhause gehen. 
# bei tod verliert der user seinen rucksack inhalt, wiederbeleben spawnt ihn wieder zuhause.
# alle neuen features brauchen entsprechende funktionen und tests.
# der user soll seinem charakter einen namen geben können
# der user soll seine character werte sehen können basierend auf seinen basis werten und seiner ausrüstung, also angriffs, verteidigungswert, hitpoints.
# wenn es mana gibt, soll der user auch seine manapunkte sehen können.
# mit mana soll der user zauber wirken können, die im kampf helfen, z.b. feuerball oder heilzauber.
# zauber kann er nur beherrschem, wenn er zauberbücher findet. die können beim händler erworben werden gegen eine hohen gold wert.
# gold bekommt der user aus dem verkauf von items oder als loot von monstern.
# monster geben auch erfahrungspunkte, die den user aufleveln lassen.
# aufleveln verändert die basiswerte des charakters.
# es soll möglich sein zu speichern um das spiel später fortsetzen zu können.
# speichern und laden soll in dateien erfolgen.
# daher soll es beim start ein menü geben, ob man ein neues spiel starten will oder ein gespeichertes spiel laden möchte.
# das speichern und laden muss alle relevanten daten des charakters, rucksack und truhen, basen etc beinhalten.
# es soll eine taverne geben, hier gibt es die möglichkeit beim wirt quests anzunehmen.
# in der taverne sitzen auch gäste, mit denen man sich unterhalten kann.
# die unterhaltungen sollen aus einem dialog dictionary kommen, das verschiedene antwortmöglichkeiten und reaktionen beinhaltet.
# unterhaltung 1: gast erzählt das er saich verfolgt gefühlt hat, es war so gruselig, dass er seinem pferd die sporen gab.
    # möglicher questeinstieg
# unterhaltung 2: ein versteckter schatzt an einem geheimen aber verfluchten ort
    # möglicher questeinstieg
# quests geben belohnungen wie gold items, oder erfahrungspunkte. 
# dafür brauchen wir eine art questsystem, in dem man aus einem dictionary von quests auswähöen kann.
# es soll eine art questchain geben ,also quests haben eine vorbedingung, die erfülkt werden muss, beispielsweise eine quest id einer vorherigen quest.
# wir starten mit einer questline von fünf quests.
# ein kräuterweib erzählt zb das es keine pilze mehr sammeln kann, 
# quest teil 1: wir verfolgen die spur im wald, in der die pilze schlecht aussehen
    # headline: Pilze verschwinden
# quest teil 2: im zuge dessen stoßen wir auf eine vergiftete quelle, die wir reinigen müssen
    # headline: Vergiftete Quelle
# quest teil 3: beim reinigen der quelle werden wir von monstern angegriffen, die wir besiegen müssen
    # headline: Angriff der Kreaturen
# quest teil 4: nach dem kampf finden wir heraus, dass ein hexer ein versteck in einer höhle hat, in der ein dunkles ritual stattgefunden jat
    # headline: Hexerversteck
# quest teil 5: wir stellen uns dem hexer in einem finalen kampf und besiegen ihn, die quelle ist gereinigt und die pilze wachsen wieder gesund.
    # Headline: Der Fall des dunklen Hexers


# der user muss über das menü dementsprechend auch eine aktive quest sehen können. quests brauchen daher eine art headline, also einen namen.
# die lore der quests soll sich an diablo und dem schwarzen auge orientieren.
# monster können sein, wilde wölfe, wildschweine, hexer, skelettkrieger, verzauberte nymphen die dich einschläfern wollen und als bnoss monster zb ein dämonenfürst, ein böse gewordfener dunkler paladin, ein magier der die seele von charakteren stiehlt
    # wölfe basiswerte level 1: lebenspunkte 30, angriff 10 (Biss!), verteidigung 5, gold 5-10, erfahrung 20
    # wildschweine basiswerte level 1: lebenspunkte 50, angriff 15 (Rammstoß!), verteidigung 8, gold 10-15, erfahrung 30
    # skelettkrieger basiswerte level 1: lebenspunkte 70, angriff 20 (Schwertschlag!), verteidigung 10, gold 15-20, erfahrung 40
    # verzauberte nymphen basiswerte level 1: lebenspunkte 40, angriff 5 (Einschläfern!), verteidigung 5, gold 20-25, erfahrung 25
    # zombies basiswerte level 1: lebenspunkte 80, angriff 12 (Fauliger Schlag!), verteidigung 12, gold 8-12, erfahrung 35
    # bosse:
    # dämonenfürst basiswerte level 5: lebenspunkte 300, angriff 50 (Höllenfeuer!), verteidigung 30, gold 100-150, erfahrung 200
    # dunkler paladin basiswerte level 5: lebenspunkte 350, angriff 60 (Schattenhieb!), verteidigung 40, gold 150-200, erfahrung 250
    # magier der seele basiswerte level 5: lebenspunkte 250, angriff 70 (Seelenraub!), verteidigung 20, gold 200-250, erfahrung 300
# die quests sollen auch in einer art questlog gespeichert werden, damit der user den überblick behält.
# mit steigendem level steigen auch die basiswerte der monster an, sie skalieren mit sinnvollen werten, die es schwierig aber auch lohnenswert machen
# pro monsterlevel steigen die werte wie angriff, lebenspunkte aber auch belohnung und erfahrung mit einem faktor von 1.14 an.
# das kampfsystem muss entsprechend angepasst werden, dass es die level der monster berücksichtigt.
# speziele angriffe der monster: fluch, vergiftung, einschläfern, bluten
# diese debuffs muss der user mit einem zauber bekämpfen können, diese zauber muss er vorher gelernt haben.
# es soll in der taverne auch eine heilerin geben die ihn gegen gold von bösen zuständen befreit
# das kampfsystem muss diese damage over time effekte berücksichtigen können. da es rundenbasierende kömpfe sind und der character sich auch bewegt kann er pro runde oder zur einen hitpunkt verlieren.
# manche waffen wollen kritische treffer steigern.
# levelbalancing des characters: mit jedem levelup bekommt der charakter 5 zusätzliche lebenspunkte, 2 angriffs und 2 verteidigungs punkte.
# erfahrungswerte tabelle:
# Level,  XP for Level Up, Total XP:
# (1,0,0)
# (2,300,300)
# (3,600,900)
# (4, 1800, 2700)
# (5, 3800, 6500)
# (6, 6500, 13000)
# (7, 8000, 21000)
# (8, 9000, 30000)
# (9, 12000, 42000)
# (10, 14000, 56000)
# (11, 20000, 76000)
# (12, 24000, 100000)






