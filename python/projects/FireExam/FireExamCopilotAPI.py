# =============================================================================
# FireExamCopilotAPI.py – Lernquiz: Feuer & Feuerwehr für die 3. Klasse
# Zielgruppe: Kinder 8-9 Jahre
# Sprache:    Deutsch
# Bibliotheken: nur Standardbibliothek (random, os, sys, time, urllib, json)
#
# BEWERTUNGS-BACKEND: GitHub Models API (kostenlos, kein Premium nötig)
#
# SETUP:
#   1. GitHub Personal Access Token (classic) erstellen:
#      https://github.com/settings/tokens/new
#      Benötigte Berechtigung: nur "models:read" (oder gar keine –
#      bei manchen Accounts reicht das Standard-Read-Token)
#
#   2. Umgebungsvariable setzen, bevor das Programm gestartet wird:
#      Windows PowerShell:  $env:GITHUB_TOKEN = "ghp_dein_token_hier"
#      Windows CMD:         set GITHUB_TOKEN=ghp_dein_token_hier
#      Linux/Mac:           export GITHUB_TOKEN=ghp_dein_token_hier
#
# KOSTEN / LIMITS (GitHub Models Free Tier, Stand 2026):
#   gpt-4o-mini : 15 Anfragen/Min, 150 Anfragen/Tag  ← Standard hier
#   gpt-4o      : 10 Anfragen/Min,  50 Anfragen/Tag
#   Kein Premium-Copilot-Abo nötig!
#
# FUNKTIONEN:
#   - GitHub Models bewertet Freitextantworten intelligent
#   - Versteht kindliche Umschreibungen und Synonyme
#   - Automatischer Fallback auf Keyword-Matching wenn API offline
# =============================================================================

import random
import os
import sys
import time
import json
import urllib.request
import urllib.error

# =============================================================================
# GITHUB MODELS API-KONFIGURATION
# Alle Einstellungen können über Umgebungsvariablen überschrieben werden.
# =============================================================================

# GitHub Models API-Endpunkt (OpenAI-kompatibles Format, kostenlos)
COPILOT_API_URL = os.environ.get(
    "GITHUB_MODELS_URL",
    "https://models.inference.ai.azure.com/chat/completions"
)

# GitHub-Token aus Umgebungsvariable (niemals im Code hardcoden!)
COPILOT_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Modell: gpt-4o-mini ist im Free Tier kostenlos (150 Anfragen/Tag).
# Weitere Optionen: "gpt-4o" (50/Tag), "meta-llama-3.1-8b-instruct" (unbegrenzt)
COPILOT_MODELL = os.environ.get("GITHUB_MODELL", "gpt-4o-mini")

# =============================================================================
# FRAGENDATENBANK
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
    {
        "thema": "Sicherheitsregeln",
        "frage": "Kerzen dürfen brennen, auch wenn niemand im Raum ist.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "falsch",
        "erklaerung": "Brennende Kerzen dürfen NIE unbeaufsichtigt bleiben – sie können Dinge entzünden und einen Brand verursachen.",
        "schluesselwoerter": [],
        "freitext_kontext": ""
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
    {
        "thema": "Sicherheitsregeln",
        "frage": "Vorhänge und Gardinen sollten nahe an einer brennenden Kerze hängen.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "falsch",
        "erklaerung": "Gardinen und Vorhänge können sich leicht entzünden. Kerzen immer weit weg von brennbaren Stoffen aufstellen.",
        "schluesselwoerter": [],
        "freitext_kontext": ""
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
    {
        "thema": "Notruf",
        "frage": "Du kannst die Notrufnummer 112 auch von einem Handy ohne Guthaben anrufen.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "wahr",
        "erklaerung": "Notrufnummern können immer kostenlos angerufen werden – auch ohne Guthaben oder SIM-Karte.",
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
    {
        "thema": "Notruf",
        "frage": "Was sind die FÜNF W-Fragen, die du beim Notruf beantworten musst?",
        "typ": "freitext",
        "antworten": [],
        "richtige_antwort": "Die fünf W-Fragen: Wer ruft an? Wo ist das Feuer? Was brennt? Wie viele Verletzte? Warten auf Rückfragen.",
        "erklaerung": "Die fünf W-Fragen helfen der Leitstelle, schnell die richtigen Helfer zu schicken.",
        "schluesselwoerter": ["wer", "wo", "was", "wie", "warten"],
        "freitext_kontext": "Die Frage nach den 5 W-Fragen beim Notruf 112. Die korrekten Fragen sind: Wer ruft an? Wo ist der Notfall? Was ist passiert? Wie viele Verletzte gibt es? Warten auf Rückfragen der Leitstelle. Das 'Warum' gehört NICHT dazu – stattdessen 'Wie viele Verletzte'."
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
    {
        "thema": "Notruf",
        "frage": "Nach dem Notruf sollst du auflegen und warten, bis die Feuerwehr kommt.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "falsch",
        "erklaerung": "Leg NICHT sofort auf! Die Leitstelle kann noch wichtige Rückfragen haben – warte, bis sie sagt, dass du auflegen kannst.",
        "schluesselwoerter": [],
        "freitext_kontext": ""
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
    {
        "thema": "Feuerexperiment",
        "frage": "Beschreibe in 1-2 Sätzen, was bei einem Kerzenexperiment mit einem Glas passiert und warum.",
        "typ": "freitext",
        "antworten": [],
        "richtige_antwort": "Wenn man ein Glas über eine Kerze stülpt, erlischt die Flamme, weil der Sauerstoff im Glas verbraucht wird.",
        "erklaerung": "Feuer braucht Sauerstoff zum Brennen – ist er aufgebraucht, geht die Flamme aus.",
        "schluesselwoerter": ["kerze", "glas", "sauerstoff", "erlischt", "brennt"],
        "freitext_kontext": "Kerzenexperiment: Ein Glas wird über eine brennende Kerze gestülpt. Die Flamme flackert und erlischt dann, weil der Sauerstoff im Glas verbraucht wird. Das Kind soll beschreiben was passiert (Flamme geht aus) UND warum (kein Sauerstoff mehr)."
    },
    {
        "thema": "Feuerexperiment",
        "frage": "Feuer kann ohne Sauerstoff brennen.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "falsch",
        "erklaerung": "Sauerstoff ist eine der drei notwendigen Bedingungen für Feuer – ohne Sauerstoff erlischt jede Flamme sofort.",
        "schluesselwoerter": [],
        "freitext_kontext": ""
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
    {
        "thema": "Verbrennungsdreieck",
        "frage": "Wenn man eine Kerze mit einer Löschglocke abdeckt, entfernt man den Sauerstoff und das Feuer geht aus.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "wahr",
        "erklaerung": "Die Löschglocke schneidet den Sauerstoff ab – ohne eine Seite des Verbrennungsdreiecks erlischt das Feuer.",
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
    {
        "thema": "Verbrennungsdreieck",
        "frage": "Erkläre in eigenen Worten, warum Feuer erlischt, wenn man Wasser darauf schüttet.",
        "typ": "freitext",
        "antworten": [],
        "richtige_antwort": "Wasser kühlt den Brennstoff ab und nimmt die Wärme weg. Ohne Wärme fehlt eine Seite des Verbrennungsdreiecks und das Feuer geht aus.",
        "erklaerung": "Wasser entzieht dem Feuer die Wärme – eine Seite des Dreiecks fehlt, also erlischt die Flamme.",
        "schluesselwoerter": ["wasser", "kühlt", "wärme", "dreieck", "erlischt"],
        "freitext_kontext": "Verbrennungsdreieck: Feuer braucht Brennstoff, Sauerstoff und Wärme. Wasser löscht Feuer, weil es den Brennstoff abkühlt und die Wärme wegnimmt. Ohne Wärme fehlt eine Seite des Dreiecks. Das Kind muss verstehen, dass Wasser die Wärme/Temperatur senkt."
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
    {
        "thema": "Verhaltensregeln im Brandfall",
        "frage": "Im Brandfall soll man den Aufzug benutzen.",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "falsch",
        "erklaerung": "Im Brandfall NIEMALS den Aufzug benutzen! Der Strom kann ausfallen und der Aufzug sich mit Rauch füllen. Immer Treppen nehmen.",
        "schluesselwoerter": [],
        "freitext_kontext": ""
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
    {
        "thema": "Verhaltensregeln im Brandfall",
        "frage": "Wenn du festsitzt und nicht rauskommst, sollst du dich bemerkbar machen (z.B. ans Fenster gehen und rufen).",
        "typ": "wahr_falsch",
        "antworten": [],
        "richtige_antwort": "wahr",
        "erklaerung": "Am Fenster sehen dich Feuerwehrleute und können dir helfen. Türritzen mit Tüchern abdichten, damit kein Rauch eindringt.",
        "schluesselwoerter": [],
        "freitext_kontext": ""
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
        "schluesselwoerter": [],
        "freitext_kontext": ""
    },
]


# =============================================================================
# COPILOT-BEWERTUNG FÜR FREITEXTANTWORTEN
# =============================================================================

def ki_freitext_bewerten(frage: str, antwort: str, richtige_antwort: str,
                          kontext: str) -> tuple[bool, str]:
    """
    Bewertet eine Freitextantwort mit GitHub Copilot (OpenAI-kompatible API).
    Gibt zurück: (korrekt: bool, feedback: str)

    Versteht kindliche Umschreibungen, Synonyme und unvollständige Sätze.
    Falls kein Token gesetzt ist oder die API nicht erreichbar ist,
    fällt das Programm automatisch auf Keyword-Matching zurück.
    """

    # Ohne Token sofort auf Fallback – kein KI-Kommentar anzeigen
    if not COPILOT_TOKEN:
        korrekt, _ = _fallback_bewertung(antwort)
        return korrekt, ""  # Leeres Feedback: Hinweis steht bereits im Startbildschirm

    # System-Prompt: Copilot als Grundschullehrer
    system_prompt = (
        "Du bist ein freundlicher Grundschullehrer (Klasse 3, 8-9 Jahre). "
        "Du bewertest kurze Freitextantworten von Kindern zu einem Quiz über "
        "Feuer und Feuerwehr.\n\n"
        "BEWERTUNGSREGELN:\n"
        "- Sei GROSSZÜGIG bei Formulierungen, Rechtschreibfehlern und Umschreibungen\n"
        "- 'die Flamme geht aus' bedeutet dasselbe wie 'erlischt' → richtig\n"
        "- 'kühlt ab' bedeutet dasselbe wie 'entzieht Wärme' → richtig\n"
        "- Bewerte ob das KIND DAS KONZEPT VERSTANDEN HAT, nicht ob es perfekt formuliert\n"
        "- Bei Fragen mit mehreren Teilen (z.B. 5 W-Fragen): mindestens 4 von 5 müssen stimmen\n"
        "- Gib eine kurze, ermutigende Rückmeldung auf Deutsch (max. 2 Sätze): "
        "was gut war und was noch fehlte (falls falsch)\n\n"
        "Antworte NUR als reines JSON-Objekt, ohne Markdown-Backticks oder anderen Text:\n"
        '{"korrekt": true, "feedback": "Dein Feedback hier"}'
    )

    user_message = (
        f"Frage: {frage}\n"
        f"Kontext für Bewerter: {kontext}\n"
        f"Richtige Antwort (Musterlösung): {richtige_antwort}\n"
        f"Antwort des Kindes: {antwort}\n\n"
        "Ist diese Antwort inhaltlich richtig?"
    )

    try:
        # OpenAI-kompatibles Request-Format für GitHub Copilot
        daten = json.dumps({
            "model": COPILOT_MODELL,
            "max_tokens": 200,
            "temperature": 0.1,   # Niedrig für konsistente Bewertungen
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_message}
            ]
        }).encode("utf-8")

        anfrage = urllib.request.Request(
            COPILOT_API_URL,
            data=daten,
            headers={
                "Content-Type": "application/json",
                # GitHub Copilot-Authentifizierung via Bearer Token
                "Authorization": f"Bearer {COPILOT_TOKEN}",
            },
            method="POST"
        )

        with urllib.request.urlopen(anfrage, timeout=15) as antwort_obj:
            ergebnis = json.loads(antwort_obj.read().decode("utf-8"))

            # OpenAI-Antwortformat: choices[0].message.content
            text = ergebnis["choices"][0]["message"]["content"].strip()

            # Eventuelle Markdown-Backticks entfernen
            text = text.replace("```json", "").replace("```", "").strip()

            geparst = json.loads(text)
            return bool(geparst["korrekt"]), str(geparst.get("feedback", ""))

    except urllib.error.HTTPError as e:
        # HTTP-Fehler ausgeben (z.B. 401 Unauthorized → Token ungültig)
        fehler_text = e.read().decode("utf-8", errors="replace")[:120]
        print(f"\n  ⚠️  GitHub Models API Fehler {e.code}: {fehler_text}")
        print("  Fallback auf Keyword-Matching...")
        korrekt, _ = _fallback_bewertung(antwort)
        return korrekt, "(KI nicht erreichbar – vereinfachte Bewertung)"

    except (urllib.error.URLError, json.JSONDecodeError, KeyError, ValueError):
        # Netzwerkfehler, Timeout, JSON-Parse-Fehler → stiller Fallback
        korrekt, _ = _fallback_bewertung(antwort)
        return korrekt, "(KI nicht erreichbar – vereinfachte Bewertung)"


def _fallback_bewertung(antwort: str) -> tuple[bool, str]:
    """
    Fallback-Bewertung ohne API.
    Prüft auf Synonyme und wichtige Konzepte.
    """
    a = antwort.lower()

    # Synonymgruppen: Wenn ein Begriff aus der Gruppe gefunden wird,
    # gilt das Konzept als erkannt
    synonymgruppen = [
        ["erlischt", "geht aus", "hört auf", "aus", "ausgeht", "verlöscht"],
        ["sauerstoff", "luft", "o2"],
        ["wärme", "temperatur", "kühlt", "kalt", "abkühlt", "abkühlen"],
        ["brennstoff", "holz", "papier", "material", "brennt"],
        ["dreieck", "drei", "seiten", "bedingung"],
        ["wer", "wo", "was", "wie", "warten"],
    ]

    treffer = 0
    for gruppe in synonymgruppen:
        if any(syn in a for syn in gruppe):
            treffer += 1

    korrekt = treffer >= 2
    feedback = "(KI offline – vereinfachte Bewertung)"
    return korrekt, feedback


# =============================================================================
# HILFSFUNKTIONEN
# =============================================================================

def bildschirm_leeren():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(sekunden: float = 1.5):
    time.sleep(sekunden)


def fortschrittsbalken(sicher: int, gesamt: int, breite: int = 20) -> str:
    """ASCII-Fortschrittsbalken – BUGFIX: benutzt aktuellen Echtzeitwert."""
    gefuellt = int((sicher / gesamt) * breite) if gesamt > 0 else 0
    balken = "█" * gefuellt + "░" * (breite - gefuellt)
    return f"Fortschritt: [{balken}] {sicher}/{gesamt} Karten sicher"


def eingabe_bereinigen(text: str) -> str:
    return text.strip().lower()


def sterne_bewertung(korrekt: int, gesamt: int) -> str:
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
    bildschirm_leeren()

    # Copilot-Status anzeigen
    if COPILOT_TOKEN:
        ki_status = f"✅ GitHub Models aktiv  (Modell: {COPILOT_MODELL})"
    else:
        ki_status = "⚠️  Kein Token – Keyword-Matching als Fallback"

    print("=" * 60)
    print()
    print("       🔥  FEUER & FEUERWEHR  🚒")
    print("       Lernquiz für die 3. Klasse")
    print()
    print("=" * 60)
    print()
    print(f"  🤖 KI-Bewerter: {ki_status}")
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


def frage_anzeigen(karte: dict, fragenummer_angezeigt: int, gesamt_karten: int,
                   sicher_anzahl: int):
    """
    BUGFIX: fragenummer_angezeigt zählt nur angezeigte Fragen (nicht Versuche).
    sicher_anzahl wird direkt übergeben und ist immer aktuell.
    """
    bildschirm_leeren()

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
    # BUGFIX: Fortschrittsbalken zeigt immer den aktuellen Echtzeitwert
    print(f"  {fortschrittsbalken(sicher_anzahl, gesamt_karten)}")
    print("=" * 60)
    print()
    # BUGFIX: Frage X von Y – Y ist die Gesamtzahl der Karten, nicht der Versuche
    print(f"  Frage {fragenummer_angezeigt} von {gesamt_karten}:")
    print()
    print(f"  {karte['frage']}")
    print()

    if karte["typ"] == "mc":
        for option in karte["antworten"]:
            print(f"    {option}")
        print()
        print("  👉 Deine Antwort (A/B/C/D): ", end="")

    elif karte["typ"] == "wahr_falsch":
        print("    W) wahr")
        print("    F) falsch")
        print()
        print("  👉 Deine Antwort (wahr/w  oder  falsch/f): ", end="")

    elif karte["typ"] == "freitext":
        print("  📝 Schreibe 1-2 Sätze:")
        print()
        print("  👉 Deine Antwort: ", end="")


def feedback_anzeigen(korrekt: bool, karte: dict, ki_feedback: str = ""):
    """Feedback anzeigen – mit optionalem KI-Feedback für Freitextfragen."""
    print()
    print("-" * 60)

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

    # KI-Feedback für Freitextfragen (erklärt was fehlte)
    if ki_feedback:
        print()
        print(f"  🤖 Lehrerkommentar: {ki_feedback}")

    print()
    print(f"  📌 Richtige Antwort:  {karte['richtige_antwort']}")
    print()
    print(f"  💡 Warum? {karte['erklaerung']}")
    print()
    print("-" * 60)
    input("  Drücke ENTER für die nächste Frage... ")


def zusammenfassung_anzeigen(korrekt: int, gesamt_versuche: int,
                              karten_anzahl: int):
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
# LERNSCHLEIFE MIT SPACED-REPETITION (BUGFIXES)
# =============================================================================

def lernschleife_starten(karten: list):
    """
    Hauptlernschleife mit Karteikartensystem und KI-Freitextbewertung.

    BUGFIXES in dieser Version:
    1. fragenummer_angezeigt zählt nur angezeigte Fragen (max = len(karten))
    2. sicher_anzahl wird VOR der Anzeige berechnet (Echtzeit-Fortschritt)
    3. Fortschrittsbalken geht korrekt zurück wenn Status auf 'unsicher' fällt
    4. Freitextbewertung nutzt Claude-API statt reines Keyword-Matching

    Schwierigkeitsstufen:
      'unsicher' → Gewicht 5 (erscheint am häufigsten)
      'gut'      → Gewicht 2
      'sicher'   → wird nicht mehr ausgewählt
    """

    # Status jeder Karte: index → "unsicher" | "gut" | "sicher"
    status = {i: "unsicher" for i in range(len(karten))}

    gesamt_versuche = 0
    gesamt_korrekt = 0

    # BUGFIX: Eigener Zähler für angezeigte Fragen (unabhängig von Versuchen)
    fragenummer_angezeigt = 0

    while True:
        # Alle Karten sicher? → Ende
        if all(s == "sicher" for s in status.values()):
            break

        # Gewichtete Auswahl
        gewichte = []
        indizes = []
        for idx, s in status.items():
            if s == "unsicher":
                gewichte.append(5)
                indizes.append(idx)
            elif s == "gut":
                gewichte.append(2)
                indizes.append(idx)

        if not indizes:
            break

        ausgewaehlter_idx = random.choices(indizes, weights=gewichte, k=1)[0]
        karte = karten[ausgewaehlter_idx]

        # BUGFIX: Sichere Karten JETZT zählen (vor Anzeige = Echtzeit)
        sicher_anzahl = sum(1 for s in status.values() if s == "sicher")

        # BUGFIX: Fragenummer ist begrenzt auf len(karten), nicht unbegrenzt
        fragenummer_angezeigt = min(fragenummer_angezeigt + 1, len(karten))

        # Frage anzeigen
        frage_anzeigen(karte, fragenummer_angezeigt, len(karten), sicher_anzahl)

        # Eingabe
        try:
            antwort_roh = input()
        except (EOFError, KeyboardInterrupt):
            print("\n\nQuiz beendet.")
            sys.exit(0)

        antwort = eingabe_bereinigen(antwort_roh)
        gesamt_versuche += 1

        # Antwort auswerten
        korrekt = False
        ki_feedback = ""

        if karte["typ"] == "mc":
            korrekt = antwort.upper() == karte["richtige_antwort"].upper()

        elif karte["typ"] == "wahr_falsch":
            # Kurzformen "w" und "f" akzeptieren
            if antwort == "w":
                antwort = "wahr"
            elif antwort == "f":
                antwort = "falsch"
            korrekt = antwort in ("wahr", "falsch") and \
                      antwort == karte["richtige_antwort"].lower()

        elif karte["typ"] == "freitext":
            # KI-Bewertung: versteht Umschreibungen und kindliche Formulierungen
            print()
            print("  ⏳ Antwort wird bewertet...")
            korrekt, ki_feedback = ki_freitext_bewerten(
                frage=karte["frage"],
                antwort=antwort,
                richtige_antwort=karte["richtige_antwort"],
                kontext=karte.get("freitext_kontext", "")
            )

        if korrekt:
            gesamt_korrekt += 1

        # BUGFIX: Kartenstatus korrekt aktualisieren
        # Bei falsch → IMMER zurück zu "unsicher" (auch von "gut")
        aktueller_status = status[ausgewaehlter_idx]
        if korrekt:
            if aktueller_status == "unsicher":
                status[ausgewaehlter_idx] = "gut"
            elif aktueller_status == "gut":
                status[ausgewaehlter_idx] = "sicher"
        else:
            # Zurücksetzen – der Fortschrittsbalken zeigt das beim nächsten Mal
            status[ausgewaehlter_idx] = "unsicher"

        # Nach Statusänderung: Fortschritt neu berechnen für nächste Runde
        # (Der Balken beim nächsten Aufruf von frage_anzeigen ist dadurch korrekt)

        feedback_anzeigen(korrekt, karte, ki_feedback)

    zusammenfassung_anzeigen(gesamt_korrekt, gesamt_versuche, len(karten))


# =============================================================================
# EINSTIEGSPUNKT
# =============================================================================

def main():
    try:
        karten = KARTEN.copy()
        random.shuffle(karten)
        willkommen_anzeigen()
        lernschleife_starten(karten)
    except KeyboardInterrupt:
        print("\n\nQuiz abgebrochen. Auf Wiedersehen! 👋")
        sys.exit(0)


if __name__ == "__main__":
    main()