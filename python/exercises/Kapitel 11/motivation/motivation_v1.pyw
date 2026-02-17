from tkinter import *
from random import choice
SPRÜCHE = ['Veränderung beginnt im Kopf, \npassiert aber im Tun.',
'Man hat schon einiges, \nwenn man manches weglässt.',
'Heute ist dein Tag!',
'Alle anderen wissen auch nicht was sie tun.',
'Du musst nicht besonders gut in etwas sein, \ndamit es gut für dich ist.',
'Das kalte Wasser wird nicht wärmer, \nwenn du später springst.',
'Die Welt ist nicht gerecht, \naber du kannst es sein.',
'Lieber erledigt als perfekt!',
'Deine Bedürfnisse zu äußern \nwird niemals eine echte Verbindung ruinieren.']

# Diese Funktion wird ausgewählt, wenn die Schaltfläche angeklickt wird.
# Sie wählt einen zufälligen Spruch aus der Liste aus und aktualisiert den Text des Labels.
def auswählen():
    text = choice(SPRÜCHE)
    label.config(text=text)

fenster = Tk()
fenster.geometry('1300x400')
fenster.config(bg='black')
button = Button(
    master=fenster,
    text='Neue Motivation',
    command=auswählen,
    font=('Comic Sans MS', 24, 'bold'),  # größere Schrift
    padx=40,  # mehr horizontaler Abstand
    pady=20,   # mehr vertikaler Abstand
    bd=5,                # Rahmenbreite
	relief='ridge',       # Relief-Rahmen
    bg='darkgray',           # Hintergrundfarbe dunkelgrau
)

label = Label(
    master=fenster, 
    font=('Segoe Script', 40, 'bold'),
	fg='white',           # Schriftfarbe weiß
	bg='black',
    text=SPRÜCHE[0]
    )



# Bilder laden und skalieren (maximal 300px Breite)
img1 = PhotoImage(file=r"python\exercises\Kapitel 11\motivation\img\rainbow1.png")
img2 = PhotoImage(file=r"python\exercises\Kapitel 11\motivation\img\rainbow2.png")

def scale_image(img, max_width=300):
    w = img.width()
    h = img.height()
    if w > max_width:
        scale = max_width / w
        new_w = int(w * scale)
        new_h = int(h * scale)
        return img.subsample(int(w / new_w), int(h / new_h))
    return img

img1 = scale_image(img1)
img2 = scale_image(img2)
img_label1 = Label(fenster, image=img1, bg='black')
img_label2 = Label(fenster, image=img2, bg='black')

img_label1.pack(side='left', padx=10)
img_label2.pack(side='right', padx=10)
button.pack()
label.pack()

fenster.mainloop()
