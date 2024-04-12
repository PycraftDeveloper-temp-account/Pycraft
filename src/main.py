import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry("734x542")
root.configure(background='red')
img = ImageTk.PhotoImage(Image.open(r"C:\Users\pamj0\Documents\GitHub\Pycraft\src\Banner.png"))
panel = tkinter.Label(root, image = img, highlightthickness=0, borderwidth=0)
panel.place(x=0, y=0)

root.mainloop()