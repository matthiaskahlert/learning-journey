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
'Einen Schritt zurückzugehen physisch oder metaphorisch \nist eine großartige Übung. Sie wird dir helfen, \ndie Dinge aus einer neuen Perspektive zu sehen.',
'Deine Bedürfnisse zu äußern \nwird niemals eine echte Verbindung ruinieren.',
'Wenn wir nicht aufrichtig "Ja" sagen, sagen wir widerwillig "Ja", und das führt zu viel mehr Problemen, als wenn wir von vornherein "Nein" gesagt hätten.',
'Die richtige Richtung \nist so viel wichtiger \nals die Geschwindigkeit.']

# Diese Funktion wird ausgewählt, wenn die Schaltfläche angeklickt wird.
# Sie wählt einen zufälligen Spruch aus der Liste aus und aktualisiert den Text des Labels.

# --- Spruch direkt auf Canvas zeichnen ---
spruch_id = None  # wird nach dem Canvas erzeugt
animation_job = None

def fade_out_in_canvas(new_text, steps=10, delay=28):
    global animation_job

    if gradient_canvas is None or not gradient_canvas.winfo_exists() or spruch_id is None:
        return

    # Bei schnellem Klicken alte Animation beenden und neu starten.
    if animation_job is not None:
        try:
            fenster.after_cancel(animation_job)
        except TclError:
            pass
        animation_job = None

    min_brightness = 80
    fade_out = [int(255 - (255 - min_brightness) * (i / steps)) for i in range(steps + 1)]
    fade_in = list(reversed(fade_out))
    sequence = fade_out + ['switch'] + fade_in

    def run_step(index=0):
        global animation_job

        if gradient_canvas is None or not gradient_canvas.winfo_exists() or spruch_id is None:
            animation_job = None
            return

        try:
            state = sequence[index]
            if state == 'switch':
                gradient_canvas.itemconfig(spruch_id, text=new_text)
            else:
                color = f'#{state:02x}{state:02x}{state:02x}'
                gradient_canvas.itemconfig(spruch_id, fill=color)
        except TclError:
            animation_job = None
            return

        if index + 1 < len(sequence):
            animation_job = fenster.after(delay, run_step, index + 1)
        else:
            animation_job = None
            try:
                gradient_canvas.itemconfig(spruch_id, fill='white')
            except TclError:
                pass

    run_step(0)

def auswählen():
    current = gradient_canvas.itemcget(spruch_id, 'text')
    possible = [spruch for spruch in SPRÜCHE if spruch != current]
    text = choice(possible) if possible else current
    fade_out_in_canvas(text)

fenster = Tk()
screen_w = fenster.winfo_screenwidth()
screen_h = fenster.winfo_screenheight()
window_w = max(900, min(1600, screen_w - 80))
window_h = max(700, min(1000, screen_h - 120))
fenster.geometry(f'{window_w}x{window_h}+20+20')
fenster.config(bg='black')
fenster.title('Motivation Booster!')

# Frame für die obere Zeile
top_frame = Frame(fenster, bg='black')
top_frame.pack(fill='x', pady=12)

controls_frame = Frame(top_frame, bg='black')
controls_frame.pack(anchor='n')

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

# Bildgröße dynamisch an verfügbare Fensterbreite anpassen.
max_img_width = max(180, int(window_w * 0.22))
img1 = scale_image(img1, max_img_width)
img2 = scale_image(img2, max_img_width)

img_label1 = Label(controls_frame, image=img1, bg='black')
img_label2 = Label(controls_frame, image=img2, bg='black')
button = Button(
    master=controls_frame,
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

def update_button_style(width):
    # Skalierung für Lesbarkeit und sauberes Layout auf verschiedenen Auflösungen.
    button_font_size = max(14, min(24, int(width / 55)))
    button_padx = max(16, min(40, int(width / 40)))
    button_pady = max(10, min(20, int(width / 90)))
    button.config(
        font=('Comic Sans MS', button_font_size, 'bold'),
        padx=button_padx,
        pady=button_pady
    )

update_button_style(window_w)

def on_enter(e):
    button.config(bg='#00fff7', fg='black')
def on_leave(e):
    button.config(bg='#ff2fd6', fg='black')
button.bind('<Enter>', on_enter)
button.bind('<Leave>', on_leave)

img_label1.grid(row=0, column=0, padx=10)
button.grid(row=0, column=1, padx=10)
img_label2.grid(row=0, column=2, padx=10)


# --- Dynamischer Spruchbereich (passt sich der Auflösung an) ---
center_frame = Frame(fenster, bg='black')
center_frame.pack(fill='both', expand=True, padx=20, pady=20)

gradient_canvas = Canvas(center_frame, highlightthickness=0, bd=0, bg='black')
gradient_canvas.pack(fill='both', expand=True)

def draw_gradient(event=None):
    global spruch_id

    width = gradient_canvas.winfo_width()
    height = gradient_canvas.winfo_height()
    if width < 2 or height < 2:
        return

    gradient_canvas.delete('gradient')
    for i in range(height):
        rel = abs(i - height / 2) / (height / 2)
        b = int(228 * (1 - rel))
        color = f'#0000{b:02x}'
        gradient_canvas.create_line(0, i, width, i, fill=color, tags='gradient')

    # Hintergrundlinien immer hinter den Spruch legen.
    gradient_canvas.tag_lower('gradient')

    if spruch_id is None:
        spruch_id = gradient_canvas.create_text(
            width // 2,
            height // 2,
            text=SPRÜCHE[0],
            font=('Segoe Script', 40, 'bold'),
            fill='white',
            justify='center',
            width=max(300, int(width * 0.78))
        )
    else:
        gradient_canvas.coords(spruch_id, width // 2, height // 2)
        gradient_canvas.itemconfig(spruch_id, width=max(300, int(width * 0.78)))

gradient_canvas.bind('<Configure>', draw_gradient)
fenster.after(50, draw_gradient)

def on_window_resize(event):
    if event.widget is fenster:
        update_button_style(event.width)

fenster.bind('<Configure>', on_window_resize)

# Sicherstellen, dass der erste Spruch beim Start angezeigt wird
if spruch_id is not None:
    gradient_canvas.itemconfig(spruch_id, text=SPRÜCHE[0])
else:
    print("Fehler: spruch_id wurde nicht korrekt initialisiert.")

# Frame für die unterste Zeile
bottom_frame = Frame(fenster, bg='black')
bottom_frame.pack(side='bottom', fill='x')

# Bilder unten
img_label1_bottom = Label(bottom_frame, image=img1, bg='black')
img_label2_bottom = Label(bottom_frame, image=img2, bg='black')
img_label1_bottom.pack(side='left', padx=10, pady=10)
img_label2_bottom.pack(side='right', padx=10, pady=10)

fenster.mainloop()
