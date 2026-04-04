# =============================================================================
# FireExam.py – Lernquiz: Feuer & Feuerwehr für die 3. Klasse
# Zielgruppe: Kinder 8-9 Jahre
# Sprache:    Deutsch
# Bibliotheken: nur Standardbibliothek (random, os, sys, time)
# =============================================================================

import random
import os
import sys
import time

# =============================================================================
# FRAGENDATENBANK
# Jede Karte ist ein Dictionary mit folgenden Schlüsseln:
#   thema          : Themenbereich (string)
#   frage          : Die Frage (string)
#   typ            : "mc" | "wahr_falsch" | "freitext"
#   antworten      : Liste [A, B, C, D] – nur bei typ "mc"
#   richtige_antwort: "A"/"B"/"C"/"D" | "wahr"/"falsch" | Musterlösung (string)
#   erklaerung     : Kurze Erklärung warum das die richtige Antwort ist
#   schluesselwoerter: Liste von Schlüsselbegriffen – nur bei typ "freitext"
# =============================================================================

KARTEN = [
    # ------------------------------------------------------------------
    # 1. SICHERHEITSREGELN
    # ------------------------------------------------------------------
    {
        "thema": "Sicherheitsregeln",
        "frage": "Was sollst du NIEMALS tun, wenn du alleine bist?",
        "typ": "mc",
        "antworten": [
            "A) Mit Streichhölzern oder Feuerzeugen spielen",
            "B) Ein Glas Wasser trinken",
            "C) Ein Buch lesen",
            "D) Hausaufgaben machen"
        ],
        "richtige_antwort": "A",
        "erklaerung": "Streichhölzer und Feuerzeuge sind keine Spielzeuge – sie können schnell einen Brand auslösen und Menschen verletzen.",
        "schluesselwoerter": []
    },
    {
        "thema": "Sicherheitsregeln",
        "frage": "Kerzen dürfen brennen, auch wenn niemand im Raum ist.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "falsch",
        "erklaerung": "Brennende Kerzen dürfen NIE unbeaufsichtigt bleiben – sie können Dinge entzünden und einen Brand verursachen.",
        "schluesselwoerter": []
    },
    {
        "thema": "Sicherheitsregeln",
        "frage": "Was solltest du tun, wenn du Streichhölzer oder ein Feuerzeug findest?",
        "typ": "mc",
        "antworten": [
            "A) Damit spielen, weil es interessant aussieht",
            "B) Es einem Erwachsenen geben",
            "C) Es in deinen Rucksack stecken",
            "D) Es verstecken"
        ],
        "richtige_antwort": "B",
        "erklaerung": "Gefundene Zündmittel gehören sofort zu einem Erwachsenen – so vermeidest du Unfälle.",
        "schluesselwoerter": []
    },
    {
        "thema": "Sicherheitsregeln",
        "frage": "Vorhänge und Gardinen sollten nahe an einer brennenden Kerze hängen.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "falsch",
        "erklaerung": "Gardinen und Vorhänge können sich leicht entzünden. Kerzen immer weit weg von brennbaren Stoffen aufstellen.",
        "schluesselwoerter": []
    },
    {
        "thema": "Sicherheitsregeln",
        "frage": "Welche Aussage über das Hantieren am Herd ist RICHTIG?",
        "typ": "mc",
        "antworten": [
            "A) Kinder dürfen ganz alleine am Herd kochen",
            "B) Am Herd sollte immer ein Erwachsener dabei sein",
            "C) Es ist egal, wie alt man ist",
            "D) Kochen ist für Kinder verboten"
        ],
        "richtige_antwort": "B",
        "erklaerung": "Am Herd können Töpfe umkippen und Fett sich entzünden – deshalb brauchen Kinder immer Aufsicht.",
        "schluesselwoerter": []
    },

    # ------------------------------------------------------------------
    # 2. NOTRUF
    # ------------------------------------------------------------------
    {
        "thema": "Notruf",
        "frage": "Welche Nummer rufst du bei einem Brand an?",
        "typ": "mc",
        "antworten": [
            "A) 110",
            "B) 911",
            "C) 112",
            "D) 118"
        ],
        "richtige_antwort": "C",
        "erklaerung": "112 ist die Notrufnummer der Feuerwehr und des Rettungsdienstes in ganz Europa – kostenlos und immer erreichbar.",
        "schluesselwoerter": []
    },
    {
        "thema": "Notruf",
        "frage": "Du kannst die Notrufnummer 112 auch von einem Handy ohne Guthaben anrufen.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "wahr",
        "erklaerung": "Notrufnummern können immer kostenlos angerufen werden – auch ohne Guthaben oder SIM-Karte.",
        "schluesselwoerter": []
    },
    {
        "thema": "Notruf",
        "frage": "Was sind die FÜNF W-Fragen, die du beim Notruf beantworten musst?",
        "typ": "freitext",
        "antworten": [],
        "richtige_antwort": "Die fünf W-Fragen: Wer ruft an? Wo ist das Feuer? Was brennt? Wie viele Verletzte? Warten auf Rückfragen.",
        "erklaerung": "Die fünf W-Fragen helfen der Leitstelle, schnell die richtigen Helfer zu schicken.",
        "schluesselwoerter": ["wer", "wo", "was", "wie", "warten"]
    },
    {
        "thema": "Notruf",
        "frage": "Was ist KEINE Aufgabe der Feuerwehr?",
        "typ": "mc",
        "antworten": [
            "A) Brände löschen",
            "B) Menschen retten",
            "C) Einkaufen für ältere Menschen",
            "D) Tierrettung bei Unfällen"
        ],
        "richtige_antwort": "C",
        "erklaerung": "Die Feuerwehr rettet Menschen und Tiere, löscht Brände und hilft bei Unfällen – Einkaufen gehört nicht dazu.",
        "schluesselwoerter": []
    },
    {
        "thema": "Notruf",
        "frage": "Nach dem Notruf sollst du auflegen und warten, bis die Feuerwehr kommt.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "falsch",
        "erklaerung": "Leg NICHT sofort auf! Die Leitstelle kann noch wichtige Rückfragen haben – warte, bis sie sagt, dass du auflegen kannst.",
        "schluesselwoerter": []
    },

    # ------------------------------------------------------------------
    # 3. FEUEREXPERIMENT
    # ------------------------------------------------------------------
    {
        "thema": "Feuerexperiment",
        "frage": "Was passiert mit einer Kerze, wenn du ein Glas darüberstülpst?",
        "typ": "mc",
        "antworten": [
            "A) Die Kerze brennt heller",
            "B) Die Kerze erlischt nach kurzer Zeit",
            "C) Die Kerze brennt ewig weiter",
            "D) Das Glas schmilzt sofort"
        ],
        "richtige_antwort": "B",
        "erklaerung": "Unter dem Glas wird der Sauerstoff verbraucht. Ohne Sauerstoff kann das Feuer nicht weiter brennen und erlischt.",
        "schluesselwoerter": []
    },
    {
        "thema": "Feuerexperiment",
        "frage": "Beschreibe in 1-2 Sätzen, was bei einem Kerzenexperiment mit einem Glas passiert und warum.",
        "typ": "freitext",
        "antworten": [],
        "richtige_antwort": "Wenn man ein Glas über eine Kerze stülpt, erlischt die Flamme, weil der Sauerstoff im Glas verbraucht wird.",
        "erklaerung": "Feuer braucht Sauerstoff zum Brennen – ist er aufgebraucht, geht die Flamme aus.",
        "schluesselwoerter": ["kerze", "glas", "sauerstoff", "erlischt", "brennt"]
    },
    {
        "thema": "Feuerexperiment",
        "frage": "Feuer kann ohne Sauerstoff brennen.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "falsch",
        "erklaerung": "Sauerstoff ist eine der drei notwendigen Bedingungen für Feuer – ohne Sauerstoff erlischt jede Flamme sofort.",
        "schluesselwoerter": []
    },
    {
        "thema": "Feuerexperiment",
        "frage": "Welche Beobachtung macht man, wenn eine Kerze unter einem Glas ausgeht?",
        "typ": "mc",
        "antworten": [
            "A) Das Glas füllt sich mit Wasser",
            "B) Die Flamme flackert zuerst und wird dann kleiner, bis sie ausgeht",
            "C) Die Kerze explodiert",
            "D) Das Glas springt auf"
        ],
        "richtige_antwort": "B",
        "erklaerung": "Die Flamme flackert, weil immer weniger Sauerstoff vorhanden ist, und erlischt schließlich ganz.",
        "schluesselwoerter": []
    },

    # ------------------------------------------------------------------
    # 4. VERBRENNUNGSDREIECK
    # ------------------------------------------------------------------
    {
        "thema": "Verbrennungsdreieck",
        "frage": "Welche DREI Dinge braucht Feuer zum Brennen? (Verbrennungsdreieck)",
        "typ": "mc",
        "antworten": [
            "A) Wasser, Luft und Erde",
            "B) Brennstoff, Sauerstoff und Wärme/Zündung",
            "C) Holz, Wind und Regen",
            "D) Licht, Schatten und Kälte"
        ],
        "richtige_antwort": "B",
        "erklaerung": "Das Verbrennungsdreieck besteht aus Brennstoff (z.B. Holz), Sauerstoff (aus der Luft) und Wärme/Zündung (z.B. Streichholz).",
        "schluesselwoerter": []
    },
    {
        "thema": "Verbrennungsdreieck",
        "frage": "Was ist ein BRENNSTOFF im Verbrennungsdreieck?",
        "typ": "mc",
        "antworten": [
            "A) Sauerstoff aus der Luft",
            "B) Die Zündtemperatur",
            "C) Ein Material das brennen kann, z.B. Holz oder Papier",
            "D) Wasser"
        ],
        "richtige_antwort": "C",
        "erklaerung": "Als Brennstoff bezeichnet man alles, was brennen kann – zum Beispiel Holz, Papier, Kohle oder Benzin.",
        "schluesselwoerter": []
    },
    {
        "thema": "Verbrennungsdreieck",
        "frage": "Wenn man eine Kerze mit einer Löschglocke abdeckt, entfernt man den Sauerstoff und das Feuer geht aus.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "wahr",
        "erklaerung": "Die Löschglocke schneidet den Sauerstoff ab – ohne eine Seite des Verbrennungsdreiecks erlischt das Feuer.",
        "schluesselwoerter": []
    },
    {
        "thema": "Verbrennungsdreieck",
        "frage": "Erkläre in eigenen Worten, warum Feuer erlischt, wenn man Wasser darauf schüttet.",
        "typ": "freitext",
        "antworten": [],
        "richtige_antwort": "Wasser kühlt den Brennstoff ab und nimmt die Wärme weg. Ohne Wärme fehlt eine Seite des Verbrennungsdreiecks und das Feuer geht aus.",
        "erklaerung": "Wasser entzieht dem Feuer die Wärme – eine Seite des Dreiecks fehlt, also erlischt die Flamme.",
        "schluesselwoerter": ["wasser", "kühlt", "wärme", "dreieck", "erlischt"]
    },
    {
        "thema": "Verbrennungsdreieck",
        "frage": "Welche Aussage zum Verbrennungsdreieck ist FALSCH?",
        "typ": "mc",
        "antworten": [
            "A) Feuer braucht Sauerstoff",
            "B) Feuer braucht einen Brennstoff",
            "C) Feuer braucht Wärme zur Zündung",
            "D) Feuer braucht Wasser zum Brennen"
        ],
        "richtige_antwort": "D",
        "erklaerung": "Wasser löscht Feuer – es gehört NICHT zum Verbrennungsdreieck, sondern wirkt gegen das Feuer.",
        "schluesselwoerter": []
    },

    # ------------------------------------------------------------------
    # 5. VERHALTENSREGELN IM BRANDFALL
    # ------------------------------------------------------------------
    {
        "thema": "Verhaltensregeln im Brandfall",
        "frage": "Was tust du ALS ERSTES, wenn du einen Brand bemerkst?",
        "typ": "mc",
        "antworten": [
            "A) Feuer selbst löschen versuchen",
            "B) Rausgehen, Türen schließen und laut rufen",
            "C) Sachen einpacken und mitnehmen",
            "D) Unter dem Bett verstecken"
        ],
        "richtige_antwort": "B",
        "erklaerung": "Zuerst in Sicherheit bringen, Türen schließen (Rauch breitet sich langsamer aus) und Erwachsene alarmieren.",
        "schluesselwoerter": []
    },
    {
        "thema": "Verhaltensregeln im Brandfall",
        "frage": "Im Brandfall soll man den Aufzug benutzen.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "falsch",
        "erklaerung": "Im Brandfall NIEMALS den Aufzug benutzen! Der Strom kann ausfallen und der Aufzug sich mit Rauch füllen. Immer Treppen nehmen.",
        "schluesselwoerter": []
    },
    {
        "thema": "Verhaltensregeln im Brandfall",
        "frage": "Wie schützt du dich vor Rauch, wenn du einen verrauchten Raum durchqueren musst?",
        "typ": "mc",
        "antworten": [
            "A) Schnell aufrecht laufen",
            "B) Gebückt laufen oder kriechen, da unten weniger Rauch ist",
            "C) Auf dem Rücken rutschen",
            "D) Mit geschlossenen Augen laufen"
        ],
        "richtige_antwort": "B",
        "erklaerung": "Rauch steigt nach oben – am Boden ist die Luft sauberer. Deshalb gebückt oder kriechend bewegen.",
        "schluesselwoerter": []
    },
    {
        "thema": "Verhaltensregeln im Brandfall",
        "frage": "Wenn du festsitzt und nicht rauskommst, sollst du dich bemerkbar machen (z.B. ans Fenster gehen und rufen).",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "wahr",
        "erklaerung": "Am Fenster sehen dich Feuerwehrleute und können dir helfen. Türritzen mit Tüchern abdichten, damit kein Rauch eindringt.",
        "schluesselwoerter": []
    },
    {
        "thema": "Verhaltensregeln im Brandfall",
        "frage": "Was solltest du im Brandfall auf KEINEN FALL tun?",
        "typ": "mc",
        "antworten": [
            "A) Die Feuerwehr anrufen",
            "B) Das Gebäude verlassen",
            "C) Sachen holen und Zeit verlieren",
            "D) Andere warnen"
        ],
        "richtige_antwort": "C",
        "erklaerung": "Im Brandfall ist jede Sekunde wichtig! Sachen sind ersetzbar – dein Leben nicht. Sofort raus und Notruf wählen.",
        "schluesselwoerter": []
    },
]

# =============================================================================
# HILFSFUNKTIONEN
# =============================================================================

def bildschirm_leeren():
    """Terminal leeren – funktioniert auf Windows und Linux/Mac."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(sekunden: float = 1.5):
    """Kurze Pause, damit Kinder den Text lesen können."""
    time.sleep(sekunden)


def fortschrittsbalken(sicher: int, gesamt: int, breite: int = 20) -> str:
    """Gibt einen ASCII-Fortschrittsbalken zurück.
    
    Beispiel: [████░░░░░░] 4/10 Karten sicher
    """
    gefuellt = int((sicher / gesamt) * breite) if gesamt > 0 else 0
    balken = "█" * gefuellt + "░" * (breite - gefuellt)
    return f"Fortschritt: [{balken}] {sicher}/{gesamt} Karten sicher"


def eingabe_bereinigen(text: str) -> str:
    """Eingabe in Kleinbuchstaben ohne führende/nachfolgende Leerzeichen."""
    return text.strip().lower()


def schluesselwoerter_pruefen(antwort: str, schluessel: list, mindest_treffer: int = 3) -> bool:
    """Prüft, ob genug Schlüsselwörter in der Freitextantwort vorkommen."""
    antwort_lower = antwort.lower()
    treffer = sum(1 for wort in schluessel if wort.lower() in antwort_lower)
    return treffer >= mindest_treffer


def sterne_bewertung(korrekt: int, gesamt: int) -> str:
    """Gibt eine Sternbewertung basierend auf der Trefferquote zurück."""
    if gesamt == 0:
        return ""
    quote = korrekt / gesamt
    if quote >= 0.9:
        return "★★★★★  Fantastisch!"
    elif quote >= 0.75:
        return "★★★★☆  Sehr gut!"
    elif quote >= 0.6:
        return "★★★☆☆  Gut gemacht!"
    elif quote >= 0.4:
        return "★★☆☆☆  Weiter üben!"
    else:
        return "★☆☆☆☆  Nicht aufgeben – du schaffst das!"


# =============================================================================
# ANZEIGE-FUNKTIONEN
# =============================================================================

def willkommen_anzeigen():
    """Begrüßungsbildschirm anzeigen."""
    bildschirm_leeren()
    print("=" * 60)
    print()
    print("       🔥  FEUER & FEUERWEHR  🚒")
    print("       Lernquiz für die 3. Klasse")
    print()
    print("=" * 60)
    print()
    print("  Hallo! In diesem Quiz lernst du alles über:")
    print()
    print("  🔹 Sicherheitsregeln beim Umgang mit Feuer")
    print("  🔹 Den Notruf 112 richtig nutzen")
    print("  🔹 Feuerexperimente erklären")
    print("  🔹 Das Verbrennungsdreieck")
    print("  🔹 Richtiges Verhalten im Brandfall")
    print()
    print("-" * 60)
    print()
    print("  📋 So funktioniert das Quiz:")
    print("     • Beantworte jede Frage so gut du kannst")
    print("     • Bei MC-Fragen: tippe A, B, C oder D")
    print("     • Bei Wahr/Falsch: tippe 'wahr' oder 'falsch'")
    print("     • Bei Freitextfragen: schreibe 1-2 Sätze")
    print("     • Alle Karten müssen SICHER werden!")
    print()
    print("=" * 60)
    print()
    input("  Drücke ENTER um zu starten... 🚀")


def frage_anzeigen(karte: dict, nummer: int, gesamt: int,
                   sicher_anzahl: int, versuch: int):
    """Eine Frage formatiert anzeigen."""
    bildschirm_leeren()

    # Thema-Banner
    thema_symbole = {
        "Sicherheitsregeln": "⚠️ ",
        "Notruf": "📞",
        "Feuerexperiment": "🧪",
        "Verbrennungsdreieck": "🔺",
        "Verhaltensregeln im Brandfall": "🏃",
    }
    symbol = thema_symbole.get(karte["thema"], "❓")

    print("=" * 60)
    print(f"  {symbol}  Thema: {karte['thema']}")
    print("-" * 60)
    print(f"  {fortschrittsbalken(sicher_anzahl, gesamt)}")
    print("=" * 60)
    print()
    print(f"  Frage {nummer} von {gesamt}:")
    print()
    print(f"  {karte['frage']}")
    print()

    # Antwortoptionen je nach Typ
    if karte["typ"] == "mc":
        for option in karte["antworten"]:
            print(f"    {option}")
        print()
        print("  👉 Deine Antwort (A/B/C/D): ", end="")

    elif karte["typ"] == "wahr_falsch":
        print("    → wahr")
        print("    → falsch")
        print()
        print("  👉 Deine Antwort (wahr/falsch): ", end="")

    elif karte["typ"] == "freitext":
        print("  📝 Schreibe 1-2 Sätze:")
        print()
        print("  👉 Deine Antwort: ", end="")


def feedback_anzeigen(korrekt: bool, karte: dict):
    """Feedback nach einer Antwort anzeigen."""
    print()
    print("-" * 60)

    # Ermutigung
    if korrekt:
        ermutigungen = [
            "Super gemacht! 🌟",
            "Toll! Du bist ein Feuerwehr-Profi! 🚒",
            "Richtig! Weiter so! ⭐",
            "Klasse! Das hast du dir gemerkt! 🎉",
            "Perfekt! Du bist großartig! 🏆",
        ]
        print(f"  ✅  {random.choice(ermutigungen)}")
    else:
        ermutigungen = [
            "Fast! Versuch es nochmal 💪",
            "Nicht ganz – du schaffst das! 🔄",
            "Noch nicht ganz richtig – weiter üben! 📚",
            "Keine Sorge – beim nächsten Mal klappt's! 💡",
        ]
        print(f"  ❌  {random.choice(ermutigungen)}")

    print()

    # Richtige Antwort immer anzeigen
    print(f"  📌 Richtige Antwort:  {karte['richtige_antwort']}")
    print()
    print(f"  💡 Warum? {karte['erklaerung']}")
    print()
    print("-" * 60)
    input("  Drücke ENTER für die nächste Frage... ")


def zusammenfassung_anzeigen(korrekt: int, gesamt_versuche: int,
                              karten_anzahl: int):
    """Abschlussbildschirm mit Zusammenfassung anzeigen."""
    bildschirm_leeren()
    falsch = gesamt_versuche - korrekt

    print("=" * 60)
    print()
    print("       🎉  GLÜCKWUNSCH! Du hast es geschafft!  🎉")
    print()
    print("=" * 60)
    print()
    print("  📊 Deine Ergebnisse:")
    print()
    print(f"     Fragen beantwortet:  {gesamt_versuche}")
    print(f"     ✅ Richtig:          {korrekt}")
    print(f"     ❌ Falsch:           {falsch}")
    print(f"     🃏 Lernkarten:       {karten_anzahl} alle SICHER!")
    print()
    print("-" * 60)
    print()

    bewertung = sterne_bewertung(korrekt, gesamt_versuche)
    print(f"  {bewertung}")
    print()
    print("  Du hast heute viel über Feuer und Feuerwehr gelernt!")
    print("  Bleib immer sicher! 🔥🚒")
    print()
    print("=" * 60)
    print()


# =============================================================================
# LERNSCHLEIFE MIT SPACED-REPETITION
# =============================================================================

def lernschleife_starten(karten: list):
    """
    Hauptlernschleife mit Karteikartensystem.
    
    Schwierigkeitsstufen:
      'unsicher' → erscheint am häufigsten (Gewicht 5)
      'gut'      → erscheint mittel häufig   (Gewicht 2)
      'sicher'   → erscheint nicht mehr im Zug (fertig)
    
    Die Sitzung endet, wenn ALLE Karten 'sicher' sind.
    """

    # Zustandsdict für jede Karte: index → status
    status = {i: "unsicher" for i in range(len(karten))}

    # Statistik
    gesamt_versuche = 0
    gesamt_korrekt = 0
    fragenummer = 0

    while True:
        # Prüfen ob alle Karten 'sicher' sind
        if all(s == "sicher" for s in status.values()):
            break

        # Gewichtete Auswahl: 'unsicher' öfter als 'gut', 'sicher' gar nicht
        gewichte = []
        indizes = []
        for idx, s in status.items():
            if s == "unsicher":
                gewichte.append(5)
                indizes.append(idx)
            elif s == "gut":
                gewichte.append(2)
                indizes.append(idx)
            # 'sicher' wird nicht mehr ausgewählt

        if not indizes:
            break

        # Zufällige Karte gemäß Gewichten wählen
        ausgewaehlter_idx = random.choices(indizes, weights=gewichte, k=1)[0]
        karte = karten[ausgewaehlter_idx]

        # Anzahl sicherer Karten für Fortschrittsbalken
        sicher_anzahl = sum(1 for s in status.values() if s == "sicher")
        fragenummer += 1

        # Frage anzeigen
        frage_anzeigen(karte, fragenummer, len(karten),
                       sicher_anzahl, gesamt_versuche)

        # Eingabe lesen
        try:
            antwort_roh = input()
        except (EOFError, KeyboardInterrupt):
            print("\n\nQuiz beendet.")
            sys.exit(0)

        antwort = eingabe_bereinigen(antwort_roh)
        gesamt_versuche += 1

        # Antwort auswerten
        korrekt = False

        if karte["typ"] == "mc":
            korrekt = antwort.upper() == karte["richtige_antwort"].upper()

        elif karte["typ"] == "wahr_falsch":
            korrekt = antwort in ("wahr", "falsch") and \
                      antwort == karte["richtige_antwort"].lower()

        elif karte["typ"] == "freitext":
            # Mindestens 3 von den Schlüsselwörtern müssen vorkommen
            mindest = min(3, len(karte["schluesselwoerter"]))
            korrekt = schluesselwoerter_pruefen(
                antwort, karte["schluesselwoerter"], mindest
            )

        # Statistik aktualisieren
        if korrekt:
            gesamt_korrekt += 1

        # Kartenstatus aktualisieren (Spaced-Repetition-Logik)
        aktueller_status = status[ausgewaehlter_idx]
        if korrekt:
            if aktueller_status == "unsicher":
                status[ausgewaehlter_idx] = "gut"
            elif aktueller_status == "gut":
                status[ausgewaehlter_idx] = "sicher"
            # 'sicher' bleibt 'sicher'
        else:
            status[ausgewaehlter_idx] = "unsicher"  # Zurücksetzen

        # Feedback anzeigen
        feedback_anzeigen(korrekt, karte)

    # Abschlussbildschirm
    zusammenfassung_anzeigen(gesamt_korrekt, gesamt_versuche, len(karten))


# =============================================================================
# EINSTIEGSPUNKT
# =============================================================================

def main():
    """Hauptfunktion – startet das Quiz."""
    try:
        # Karten mischen für abwechslungsreiche Reihenfolge
        karten = KARTEN.copy()
        random.shuffle(karten)

        # Willkommensbildschirm
        willkommen_anzeigen()

        # Lernschleife starten
        lernschleife_starten(karten)

    except KeyboardInterrupt:
        print("\n\nQuiz abgebrochen. Auf Wiedersehen! 👋")
        sys.exit(0)


if __name__ == "__main__":
    main()
