from tkinter import *
from tkinter import simpledialog, messagebox
from random import randint
from _thread import start_new_thread
from time import sleep
import json
import os
from threading import Lock

class Zahl:
    def __init__(self, app):
        self.canvas = app.canvas
        self.schläger = app.schläger
        self.app = app
        self.wert = 0
        self.id = None
        self.aktiv = True
        start_new_thread(self.run, ())

    def run(self):
        c = self.canvas
        try:
            while self.aktiv and self.app.spiel_aktiv:
                x, y = randint(10, 290), -10
                self.wert = randint(-10, 10)
                
                try:
                    self.id = c.create_text(x, y, text=str(self.wert))
                except:
                    break
                
                c.coords(self.id, x, y)
                x1, y1, x2, y2 = c.coords(self.schläger.id)
                hit = self.id in c.find_overlapping(x1, y1, x2, y2)
                sleep(randint(0, 30) / 10)
                
                while (y < 200) and not hit and self.aktiv and self.app.spiel_aktiv:
                    sleep(0.05)
                    try:
                        x, y = c.coords(self.id)
                        c.move(self.id, 0, 5)
                        x1, y1, x2, y2 = c.coords(self.schläger.id)
                        hit = self.id in c.find_overlapping(x1, y1, x2, y2)
                    except:
                        break
                
                # Zahl wurde getroffen
                if hit and self.aktiv and self.app.spiel_aktiv:
                    with self.app.lock:
                        self.app.punkte += self.wert
                    self.app.punkte_aktualisieren()
                
                # Zahl löschen (egal ob getroffen oder nicht)
                try:
                    c.delete(self.id)
                except:
                    pass
                
                # Kurze Pause vor nächster Zahl
                sleep(0.1)
        except:
            pass

class Schläger:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 185, 40, 190, fill='blue')
    
    def links(self):
        try:
            self.canvas.move(self.id, -20, 0)
        except:
            pass
    
    def rechts(self):
        try:
            self.canvas.move(self.id, 20, 0)
        except:
            pass

class App:
    def __init__(self):
        self.punkte = 0
        self.zeit_rest = 30
        self.spiel_aktiv = False
        self.lock = Lock()
        self.zahlen = []
        
        # Fenster Setup
        self.fenster = Tk()
        self.fenster.title("Zahlenregen Spiel")
        self.fenster.geometry("400x500")
        
        # Top Frame - Punkte und Zeit
        top_frame = Frame(self.fenster)
        top_frame.pack(pady=10)
        
        # Punkte Label
        self.punkte_label = Label(top_frame, text="Punkte: 0", 
                                  font=('Arial', 18, 'bold'), fg='green')
        self.punkte_label.pack()
        
        # Zeit Label
        self.zeit_label = Label(top_frame, text="Zeit: 30s", 
                               font=('Arial', 16, 'bold'), fg='blue')
        self.zeit_label.pack()
        
        # Canvas
        self.canvas = Canvas(self.fenster, width=300, height=200, bg='white')
        self.schläger = Schläger(self.canvas)
        self.canvas.pack(pady=10)
        
        # Buttons Frame
        button_frame = Frame(self.fenster)
        button_frame.pack(pady=10)
        
        self.b_start = Button(button_frame, text='START', 
                             command=self.spiel_starten, 
                             font=('Arial', 12, 'bold'), 
                             bg='green', fg='white')
        self.b_start.pack(side=LEFT, padx=5)
        
        self.b_links = Button(button_frame, text='<-', 
                             command=self.schläger.links)
        self.b_links.pack(side=LEFT, padx=5)
        
        self.b_rechts = Button(button_frame, text='->',
                              command=self.schläger.rechts)
        self.b_rechts.pack(side=LEFT, padx=5)
        
        # Keybindings
        self.fenster.bind('<Left>', lambda event: self.schläger.links())
        self.fenster.bind('<Right>', lambda event: self.schläger.rechts())
        self.fenster.bind('a', lambda event: self.schläger.links())
        self.fenster.bind('d', lambda event: self.schläger.rechts())
        
        # Highscores anzeigen
        self.highscores_label = Label(self.fenster, text="", 
                                     font=('Arial', 10), 
                                     justify=LEFT, fg='navy')
        self.highscores_label.pack(pady=10)
        
        # Highscores laden und anzeigen
        self.highscores = self.lade_highscores()
        self.zeige_highscores()
        
        self.fenster.mainloop()
    
    def lade_highscores(self):
        """Lade Highscores aus JSON-Datei"""
        datei = "highscores.json"
        if os.path.exists(datei):
            try:
                with open(datei, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def speichere_highscores(self):
        """Speichere Highscores in JSON-Datei"""
        try:
            with open("python\\exercises\\Kapitel 14 Uebungen\\highscores.json", 'w') as f:
                json.dump(self.highscores, f, indent=2)
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Speichern: {e}")
    
    def zeige_highscores(self):
        """Zeige Top 5 Highscores im Label"""
        if not self.highscores:
            text = "Keine Highscores vorhanden"
        else:
            text = "Top 5 Highscores:\n"
            for i, hs in enumerate(sorted(self.highscores, 
                                         key=lambda x: x['punkte'], 
                                         reverse=True)[:5], 1):
                text += f"{i}. {hs['name']}: {hs['punkte']} Punkte\n"
        
        self.highscores_label.config(text=text)
    
    def spiel_starten(self):
        """Starte ein neues Spiel"""
        if self.spiel_aktiv:
            return
        
        # Alte Zahlen beenden
        for zahl in self.zahlen:
            zahl.aktiv = False
        
        # Reset
        self.punkte = 0
        self.zeit_rest = 30
        self.spiel_aktiv = True
        self.canvas.delete("all")
        self.schläger = Schläger(self.canvas)
        self.zahlen = []
        
        # Update UI
        self.punkte_aktualisieren()
        self.zeit_label.config(text=f"Zeit: {self.zeit_rest}s")
        self.b_start.config(state=DISABLED)
        
        # Starte Zahlen
        for i in range(12):
            self.zahlen.append(Zahl(self))
        
        # Starte Timer in separatem Thread
        start_new_thread(self.timer_laufen, ())
    
    def timer_laufen(self):
        """Countdown Timer im separaten Thread"""
        while self.zeit_rest > 0 and self.spiel_aktiv:
            sleep(1)
            if self.spiel_aktiv:
                self.zeit_rest -= 1
                # Update via after() für Thread-Sicherheit
                self.fenster.after(0, lambda: self.zeit_label.config(
                    text=f"Zeit: {self.zeit_rest}s"))
        
        # Spiel beenden
        self.fenster.after(0, self.spiel_beenden)
    
    def spiel_beenden(self):
        """Spielende - Highscore Dialog"""
        self.spiel_aktiv = False
        
        # Alle Zahlen-Threads stoppen
        for zahl in self.zahlen:
            zahl.aktiv = False
        
        # Canvas leeren
        self.canvas.delete("all")
        self.b_start.config(state=NORMAL)
        
        # Dialog für Namenseingabe
        if self.punkte > 0:
            name = simpledialog.askstring("Spielende", 
                                         f"Glückwunsch! Deine Punkte: {self.punkte}\n\nGib deinen Namen ein:")
        else:
            name = simpledialog.askstring("Spielende", 
                                         f"Deine Punkte: {self.punkte}\n\nGib deinen Namen ein:")
        
        if name and name.strip():
            # Highscore speichern
            with self.lock:
                self.highscores.append({'name': name.strip(), 'punkte': self.punkte})
            self.speichere_highscores()
            self.zeige_highscores()
            messagebox.showinfo("Erfolg", "Highscore gespeichert!")
        
        self.zeit_rest = 30
        self.zeit_label.config(text=f"Zeit: {self.zeit_rest}s")
    
    def punkte_aktualisieren(self):
        """Update Punkte-Label mit Farbe (Thread-sicher)"""
        with self.lock:
            punkte = self.punkte
        
        if punkte >= 0:
            farbe = 'green'
        else:
            farbe = 'red'
        
        self.punkte_label.config(text=f"Punkte: {punkte}", fg=farbe)

# Hauptprogramm starten
App()
