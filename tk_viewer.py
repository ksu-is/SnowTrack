
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
img = Image.open("photo.jpg")
img.thumbnail((800, 800))
photo = ImageTk.PhotoImage(img)        # keep a reference, or the image disappears
label = tk.Label(root, image=photo)
label.image = photo                    # this line prevents garbage collection
label.pack()
root.mainloop()
