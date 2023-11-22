if __name__ != "__main__":
    try:
        import tkinter.ttk
        import tkinter

        from PIL import Image, ImageTk

        from registry_utils import Registry

        import error_utils
        import path_utils
        import image_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (splash_menu.py).\nMore Details: {error}")

    class SplashMenu(Registry):
        def __init__(self) -> None:
            try:
                image_size = (485, 193)

                self.__root = tkinter.Tk()
                self.__root.title("Pycraft: Splash Screen")

                resources_path = f"{Registry.base_path}/src/resources/general"
                image_path = path_utils.Path(f"{resources_path}/pycraft_logo_smaller_colorkey.png").path

                logo_path = f"{resources_path}/icon.png"
                image_path = path_utils.Path(image_path).path

                image = Image.open(image_path)

                image = image.resize(image_size)

                self.__splash_image = ImageTk.PhotoImage(image)

                icon=tkinter.PhotoImage(
                    file=logo_path)

                self.__root.iconphoto(
                    True,
                    icon)

                self.__color_key = "#%02x%02x%02x" % (255, 0, 255)
                self.__root.configure(background=self.__color_key)

                self.__root.resizable(
                    width=False,
                    height=False)

                self.__root.overrideredirect(True)

                self.__root.lift()
                self.__root.wm_attributes("-topmost", True)
                self.__root.wm_attributes("-disabled", True)
                self.__root.wm_attributes("-transparentcolor", self.__color_key)

                screen_size_x = self.__root.winfo_screenwidth()
                screen_size_y = self.__root.winfo_screenheight()
                centred_x_position = int((screen_size_x-image_size[0])/2)
                centred_y_position = int((screen_size_y-image_size[1])/2)
                self.__root.geometry(f"{image_size[0]}x{image_size[1]}+{centred_x_position}+{centred_y_position}")
                self.__root.focus()

                self.main_splash_menu()
            except Exception as error:
                print(error)
                error_utils.Error(error=error)

        def main_splash_menu(self) -> None:
            try:
                image = tkinter.Label(
                    self.__root,
                    background=self.__color_key,
                    image=self.__splash_image)
                image.pack()

                self.__root.mainloop()
            except Exception as error:
                error_utils.Error(error=error)

else:
    MESSAGE = "You need to run this as part of Pycraft, please run the 'main.py' file"
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
