from tkinter import Tk, Label
from tkinter.font import BOLD
fenster = Tk()
label = Label(
	master=fenster,
	text=f'Verdammte Axt! \nDas ist ja schwarz wie die Nacht!',
	font=('Segoe Script', 40, BOLD),
	fg='white',           # Schriftfarbe weiß
	bg='black',           # Hintergrundfarbe schwarz
)
label.pack()
fenster.title('Hallo Welt!')
# fenster.geometry('600x200') fixiert die Abmessungen, das Widget passt sich aber auch an die erforderliche Breite dynamisch an.
fenster.configure(background='black')
fenster.mainloop()
"""
man muss das objekt fenster mit der methode mainloop() aufrufen, damit es angezeigt wird.
mainloop() aktiviert das Ereignis-Handling, damit das Fenster auf Benutzereingaben reagieren kann. 
Ohne diesen Aufruf würde das Fenster sofort wieder geschlossen werden, da das Programm nach der Erstellung des Fensters weiterläuft und endet.
die Dateiendung pyw sorgt dafür, dass das Skript ohne Konsolenfenster ausgeführt wird, was für GUI-Anwendungen wie diese sinnvoll ist.
mit pack() wird das Layout festgelegt, damit das Label im Fenster angezeigt wird. Ohne pack() würde das Label nicht sichtbar sein, da es nicht in das Fenster eingefügt wird.
"""
