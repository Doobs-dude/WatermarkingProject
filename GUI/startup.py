import tkinter as tk
from PIL import Image

root = tk.Tk()
root.geometry("1600x900")

bg_image = Image.open("Component4.png") 
bg_image = bg_image.resize((1600, 900)) 
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1) 

root.mainloop()