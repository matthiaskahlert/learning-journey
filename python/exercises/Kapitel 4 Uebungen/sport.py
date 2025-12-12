# eingabe Wetterbedingungen wenn sonne, und keine hohe luftfeuchtigkeit dann sport
def ask_yes_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ("j", "n"):
            return answer
        print("❌ Ungültige Eingabe. Bitte 'j' oder 'n' eingeben.")


antwort_sonne = ask_yes_no("Scheint die Sonne? (j/n): ")
if antwort_sonne == "j":
    print("Okay!")
    antwort_luft = ask_yes_no("Hohe Luftfeuchtigkeit? (j/n): ")
    if antwort_luft == "j":
        print("Trotz Sonne kein Sport bei hoher Luftfeuchtigkeit.")
    else:
        print("Sport bei Sonnenschein!")
else:
    print("Okay!")
    antwort_regen = ask_yes_no("Regnet es? (j/n): ")
    if antwort_regen == "j":
        antwort_wind = ask_yes_no("Starker Wind? (j/n): ")
        if antwort_wind == "j":
            print("Kein Sport bei Regen und starkem Wind.")
        else:
            print("Sport bei Regen, aber ohne starken Wind!")
    else:
        print("Sport bei bewölktem Himmel!")
