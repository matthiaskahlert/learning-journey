deutsch = [
    "der", "die", "und", "ist", "ein", "nicht", "zu", "auf", "mit", "sich",
    "dem", "des", "im", "für", "an", "als", "auch", "es", "aus", "bei",
    "wie", "er", "sie", "wir", "man", "noch", "nach", "so", "aber", "oder"
]
englisch = [
    "the", "and", "is", "in", "it", "you", "of", "to", "a", "that",
    "for", "on", "with", "as", "was", "at", "by", "this", "from", "be",
    "are", "not", "have", "an", "they", "which", "or", "we", "his", "but"
]

while True:
    text = input("Text eingeben (mind. 50 Zeichen): ").lower()
    if len(text) >= 50:
        break
    print("Bitte gib einen Text mit mindestens 50 Zeichen ein.")

woerter = text.split()

de_count = sum(woerter.count(w) for w in deutsch)
en_count = sum(woerter.count(w) for w in englisch)

if de_count > en_count:
    print("Der Text ist wahrscheinlich Deutsch.")
elif en_count > de_count:
    print("Der Text ist wahrscheinlich Englisch.")
else:
    print("Sprache nicht eindeutig erkennbar.")