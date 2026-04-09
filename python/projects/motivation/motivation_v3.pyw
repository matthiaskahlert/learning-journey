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
'Deine Bedürfnisse zu äußern \nwird niemals eine echte Verbindung ruinieren.',
'Die richtige Richtung \nist so viel wichtiger \nals die Geschwindigkeit.']

# Diese Funktion wird ausgewählt, wenn die Schaltfläche angeklickt wird.
# Sie wählt einen zufälligen Spruch aus der Liste aus und aktualisiert den Text des Labels.
def auswählen():
    current = label.cget('text')
    possible = [spruch for spruch in SPRÜCHE if spruch != current]
    if possible:
        text = choice(possible)
    else:
        text = current
    label.config(text=text)

fenster = Tk()
fenster.geometry('1800x1200')
fenster.config(bg='black')
fenster.title('Motivation Booster!')

# Frame für die obere Zeile
top_frame = Frame(fenster, bg='black')
top_frame.pack()

# Bilder laden und skalieren (maximal 600px Breite)
img1 = PhotoImage(file=r"python\projects\motivation\img\rainbow3.png")
img2 = PhotoImage(file=r"python\projects\motivation\img\rainbow4.png")

def scale_image(img, max_width=600):
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

img_label1 = Label(top_frame, image=img1, bg='black')
img_label2 = Label(top_frame, image=img2, bg='black')
button = Button(
    master=top_frame,
    text='Neue Motivation',
    command=auswählen,
    font=('Comic Sans MS', 24, 'bold'),
    padx=40,
    pady=20,
    bd=5,
    relief='ridge',
    bg='darkgray',
)

img_label1.grid(row=0, column=0, padx=10)
button.grid(row=0, column=1, padx=10)
img_label2.grid(row=0, column=2, padx=10)

label = Label(
    master=fenster,
    font=('Segoe Script', 40, 'bold'),
    fg='white',
    bg='black',
    text=SPRÜCHE[0]
)

label.pack(pady=20)

# Frame für die unterste Zeile
bottom_frame = Frame(fenster, bg='black')
bottom_frame.pack(side='bottom', fill='x')

# Bilder unten
img_label1_bottom = Label(bottom_frame, image=img1, bg='black')
img_label2_bottom = Label(bottom_frame, image=img2, bg='black')
img_label1_bottom.pack(side='left', padx=10, pady=10)
img_label2_bottom.pack(side='right', padx=10, pady=10)

fenster.mainloop()
