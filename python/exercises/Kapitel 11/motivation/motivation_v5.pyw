from tkinter import *
from random import choice

# Sprüche
SPRÜCHE = [
    'Veränderung beginnt im Kopf, \npassiert aber im Tun.',
    'Man hat schon einiges, \nwenn man manches weglässt.',
    'Heute ist dein Tag!',
    'Alle anderen wissen auch nicht was sie tun.',
    'Du musst nicht besonders gut in etwas sein, \ndamit es gut für dich ist.',
    'Das kalte Wasser wird nicht wärmer, \nwenn du später springst.',
    'Die Welt ist nicht gerecht, \naber du kannst es sein.',
    'Lieber erledigt als perfekt!',
    'Deine Bedürfnisse zu äußern \nwird niemals eine echte Verbindung ruinieren.',
    'Die richtige Richtung \nist so viel wichtiger \nals die Geschwindigkeit.'
]

# --- Fade Funktion (rekursiv, effizient) ---
def fade(step=10, fade_in=False, new_text=None):
    if not fade_in:
        color = f'#{step*15:02x}{step*15:02x}{step*15:02x}'
        label.config(fg=color)
        if step > 0:
            fenster.after(30, fade, step-1, False, new_text)
        else:
            label.config(text=new_text)
            fenster.after(30, fade, 0, True, new_text)
    else:
        color = f'#{step*15:02x}{step*15:02x}{step*15:02x}'
        label.config(fg=color)
        if step < 10:
            fenster.after(30, fade, step+1, True, new_text)
        else:
            label.config(fg='white')  # finale Farbe

# --- Neue Motivation auswählen ---
def auswählen():
    current = label.cget('text')
    possible = [spruch for spruch in SPRÜCHE if spruch != current]
    text = choice(possible) if possible else current
    fade(new_text=text)

# --- Fenster ---
fenster = Tk()
fenster.geometry('1800x1200')
fenster.title('Motivation Booster!')

# --- Gradient Background ---
# Tkinter hat keinen echten Gradient, aber wir können Frame nutzen
bg_frame = Canvas(fenster, width=1800, height=1200)
bg_frame.pack(fill='both', expand=True)

# Einfacher vertikaler Gradient (blau-schwarz)
for i in range(0, 1200):
    color = f'#{0:02x}{0:02x}{14+i//10:02x}'  # von #00000e bis #0000e4
    bg_frame.create_line(0, i, 1800, i, fill=color)

# Alles in bg_frame platzieren
container = Frame(bg_frame, bg='black', bd=0)
container.place(relx=0.5, rely=0.5, anchor='center')

# --- Bilder laden ---
img1 = PhotoImage(file=r"python\exercises\Kapitel 11\motivation\img\rainbow3.png")
img2 = PhotoImage(file=r"python\exercises\Kapitel 11\motivation\img\rainbow4.png")

def scale_image(img, max_width=600):
    w, h = img.width(), img.height()
    if w > max_width:
        scale = max_width / w
        return img.subsample(int(w / (w*scale)), int(h / (h*scale)))
    return img

img1 = scale_image(img1)
img2 = scale_image(img2)

# --- Top Frame ---
top_frame = Frame(container, bg='black', bd=0)
top_frame.pack(pady=20)

img_label1 = Label(top_frame, image=img1, bg='black')
img_label2 = Label(top_frame, image=img2, bg='black')

img_label1.grid(row=0, column=0, padx=10)
img_label2.grid(row=0, column=2, padx=10)

# --- Button ---
button = Button(
    master=top_frame,
    text='Neue Motivation',
    command=auswählen,
    font=('Comic Sans MS', 24, 'bold'),
    padx=40,
    pady=20,
    bd=5,
    relief='ridge',
    bg='#ff2fd6', # Neon pink
    fg='black',
    activebackground='#ffe600', # Neon gelb beim Klicken
    activeforeground='black',
    highlightthickness=2,
    highlightbackground='#00fff7' # Neon cyan border
)

# Hover Effekte
def on_enter(e):
    button.config(bg='#00fff7', fg='black')
def on_leave(e):
    button.config(bg='#ff2fd6', fg='black')
button.bind('<Enter>', on_enter)
button.bind('<Leave>', on_leave)
button.grid(row=0, column=1, padx=10)

# Pulsierender Button
def pulse():
    current_color = button.cget('highlightbackground')
    new_color = '#00fff7' if current_color == '#ff2fd6' else '#ff2fd6'
    button.config(highlightbackground=new_color)
    fenster.after(800, pulse)
pulse()

# --- Motivationslabel (Text-Glow optional) ---
# Optionaler Glow Layer
glow_label = Label(container,
    font=('Segoe Script', 40, 'bold'),
    fg='#00fff7', # Cyan Glow
    bg='black',
    text=SPRÜCHE[0]
)
glow_label.place(relx=0.5, rely=0.55, anchor='center')

# Hauptlabel (scharf)
label = Label(
    container,
    font=('Segoe Script', 40, 'bold'),
    fg='white',
    bg='black',
    text=SPRÜCHE[0]
)
label.place(relx=0.5, rely=0.55, anchor='center')

# Optional: Rahmen entfernen / dezenter
# label.config(bd=0, relief='flat', highlightthickness=0)

# --- Bottom Frame (Bilder unten) ---
bottom_frame = Frame(container, bg='black', bd=0)
bottom_frame.pack(side='bottom', fill='x', pady=20)
img_label1_bottom = Label(bottom_frame, image=img1, bg='black')
img_label2_bottom = Label(bottom_frame, image=img2, bg='black')
img_label1_bottom.pack(side='left', padx=10)
img_label2_bottom.pack(side='right', padx=10)

fenster.mainloop()