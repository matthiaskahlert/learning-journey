from tkinter import Tk, Canvas

fenster = Tk()
fenster.title("Canvas Beispiele")

canvas = Canvas(master=fenster, width=400, height=300, bg="white")
canvas.pack()

# 1️⃣ KREIS (50x50 Pixel)
# Breite = 150-50 = 100, Höhe = 150-50 = 100 → Kreis!
canvas.create_oval(50, 50, 150, 150, fill="blue", outline="black", width=2)
canvas.create_text(100, 170, text="Kreis (100x100)")

# 2️⃣ ELLIPSE (gestreckt horizontal)
# Breite = 200-170 = 30, Höhe = 130-80 = 50 → Ellipse!
canvas.create_oval(170, 80, 370, 130, fill="red", outline="black", width=2)
canvas.create_text(270, 150, text="Ellipse (200x50)")

# 3️⃣ RECHTECK
canvas.create_rectangle(50, 200, 150, 250, fill="green", outline="black", width=2)
canvas.create_text(100, 270, text="Rechteck")

# 4️⃣ LINIE
canvas.create_line(170, 200, 370, 250, fill="purple", width=3)
canvas.create_text(270, 270, text="Linie")



# # 5️⃣ MEHRERE KREISE nebeneinander
# for i in range(5):
#     x = 50 + i * 60
#     canvas.create_oval(x, 50, x+40, 90, fill="orange")
# 
# # 6️⃣ RANDOM KREISE
# import random
# for _ in range(10):
#     x1 = random.randint(0, 300)
#     y1 = random.randint(0, 250)
#     size = random.randint(20, 50)
#     farbe = random.choice(["red", "blue", "green", "yellow"])
#     canvas.create_oval(x1, y1, x1+size, y1+size, fill=farbe)
# 
# # 7️⃣ TEXT auf dem Canvas
# canvas.create_text(200, 150, text="Hallo Canvas!", font=("Arial", 20), fill="red")
# 
# # 8️⃣ MEHRERE LINIEN (Stern)
# canvas.create_line(100, 50, 150, 150)
# canvas.create_line(150, 50, 100, 150)
# canvas.create_line(125, 50, 125, 150)

fenster.mainloop()