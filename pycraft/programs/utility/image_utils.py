if __name__ != "__main__":
    try:
        from tkinter import messagebox
        import tkinter
        
        import pygame
        from PIL import Image
        from PIL import ImageTk
    except Exception as Message:
        try:
            import sys
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "Startup Fail",
                str(Message))
            sys.exit()

        except Exception as Message:
            print(Message)
            sys.exit()
    
    class ConvertImage:
        def __init__(self):
            pass

        def pilImageToSurface(pilImage):
            return pygame.image.fromstring(
                pilImage.tobytes(),
                pilImage.size,
                pilImage.mode)

    class tkinter_installer:
        def __init__(self):
            pass

        def open_img(root, file):
            try:
                load = Image.open(file)

                render = ImageTk.PhotoImage(load, master=root)

                img = tkinter.Label(
                    root,
                    image=render)

                img.image = render
                img.place(
                    x=-3,
                    y=-5)

                return render, load

            except Exception as Message:
                messagebox.showerror(
                    "Module Not Found",
                    "".join(("This installer requires the module Pillow, ",
                             "this should have been installed automatically ",
                             "if you got this installer from PyPi, or are ",
                             "running this as a (.exe) file.\nIf you have ",
                             "grabbed this installer from GitHub then I ",
                             "advice you to install PIL with the command:",
                             "\n\npip install pillow\n\nShould any further ",
                             "problems occur then feel free to contact the ",
                             "developer with the links available at: ",
                             "https://github.com/PycraftDeveloper/Pycraft",
                             f"\n\nFull Error Message:\n{Message}")))
                quit()

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail",
                         "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()
