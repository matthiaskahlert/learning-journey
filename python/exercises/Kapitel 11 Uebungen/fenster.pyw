from tkinter import Tk, Label
fenster = Tk()
label = Label(master = fenster, text = 'Moin!', font=('Courier', 40))
label.pack()
fenster.title('Hallo Welt!')
fenster.geometry('400x200')
fenster.mainloop()
"""
man muss das objekt fenster mit der methode mainloop() aufrufen, damit es angezeigt wird.
mainloop() aktiviert das Ereignis-Handling, damit das Fenster auf Benutzereingaben reagieren kann. 
Ohne diesen Aufruf würde das Fenster sofort wieder geschlossen werden, da das Programm nach der Erstellung des Fensters weiterläuft und endet.
die Dateiendung pyw sorgt dafür, dass das Skript ohne Konsolenfenster ausgeführt wird, was für GUI-Anwendungen wie diese sinnvoll ist.
mit pack() wird das Layout festgelegt, damit das Label im Fenster angezeigt wird. Ohne pack() würde das Label nicht sichtbar sein, da es nicht in das Fenster eingefügt wird.
"""
