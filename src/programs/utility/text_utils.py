if __name__ != "__main__":
    try:
        import os
        from tkinter import font

        import pygame

        from registry_utils import Registry

        import color_utils
        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (text_utils.py).\nMore Details: {error}")

    CENTERED = "Centered"
    LEFT = "Left"
    RIGHT = "Right"
    TOP = "Top"
    BOTTOM = "Bottom"

    def get_system_font(size=None, bold=None, italic=None):
        system_font = font.nametofont("TkTextFont")
        system_font_dictionary = system_font.actual()
        pygame.font.SysFont(system_font_dictionary["family"], 16)


    class TextFormatter(Registry):
        pass

    class FontStyleNotFoundError(Exception):
        def __init__(self) -> None:
            Exception.__init__(self, "Font style not found")

    class InvalidCharacterError(Exception):
        def __init__(self) -> None:
            Exception.__init__(self, "Character entered is invalid")

    class TextRenderer(Registry):
        pass

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
