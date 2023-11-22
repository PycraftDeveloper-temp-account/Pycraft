if __name__ != "__main__":
    try:
        import os

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

    class TextFormatter(Registry):
        def __init__(self) -> None:
            colors = color_utils.Colors().color

            self.custom_character_set_color = {
                "R": colors["red"],
                "O": colors["orange"],
                "Y": colors["yellow"],
                "G": colors["green"],
                "B": colors["blue"],
                "P": colors["purple"],
                "I": colors["indigo"],
                "V": colors["violet"],
                "K": colors["black"],
                "W": colors["white"],
                "S": Registry.themes.shape_color,
                "C": -1}

            self.custom_character_set_format = {
                "b": None, # bold
                "u": None, # underline
                "i": None, # italic
                "n": None} # newline

    class FontStyleNotFoundError(Exception):
        def __init__(self) -> None:
            Exception.__init__(self, "Font style not found")

    class InvalidCharacterError(Exception):
        def __init__(self) -> None:
            Exception.__init__(self, "Character entered is invalid")

    class TextRenderer(Registry):
        def __init__(self) -> None:
            pygame.font.init()

            fonts_path = f"{Registry.base_path}/pycraft/fonts/Noto_Sherrif"
            fonts_path = f"{fonts_path}/NotoSerif-VariableFont_wdth,wght.ttf"
            self.font_path = path_utils.Path(fonts_path).path

            self.fonts = {}

        def get_text_size(self, text: str, size:int) -> int:
            found_size = False
            for font_sizes in self.fonts:
                if font == str(size):
                    font = self.fonts[font_sizes]
                    found_size = True
                    break

            if found_size is False:
                self.fonts[str(size)] = pygame.font.Font(self.font_path)

            font = self.fonts[str(size)]

            if "$(" in text:
                index = 0
                remove = False
                string = ""
                for character in text:
                    if text[index] == "$":
                        if index + 1 < len(text):
                            if text[index + 1] == "(":
                                remove = True
                    if text[index - 1] == ")" and remove:
                        remove = False

                    if remove is False:
                        string += character

                    index += 1
            else:
                string = text

            return font.size(string)

        def font_metrics(
                self,
                character,
                size: int=20):

            found_size = False
            for font_sizes in self.fonts:
                if font == str(size):
                    font = self.fonts[font_sizes]
                    found_size = True
                    break

            if found_size is False:
                self.fonts[str(size)] = pygame.font.Font(self.font_path)

            font = self.fonts[str(size)]

            return font.metrics(character)

        def render_text(
                self,
                text: str,
                size: str,
                position: list=[0, 0],
                surface: pygame.Surface=None,
                blit: bool=True,
                aa: bool=True,
                fg_color: tuple=None,
                bg_color: tuple=None,
                wrap: bool=True,
                underline: bool=False,
                bold: bool=False,
                italic: bool=False) -> int:

            found_size = False
            for font_sizes in self.fonts:
                if font == str(size):
                    font = self.fonts[font_sizes]
                    found_size = True
                    break

            if found_size is False:
                self.fonts[str(size)] = pygame.font.Font(self.font_path)

            font = self.fonts[str(size)]

            character_height = font.size(" ")[1]

            if surface is None:
                using_display = True
                surface = Registry.displays.display
                max_width = surface.get_width() - 64
                max_height = surface.get_height()
            else:
                using_display = False
                max_width = surface.get_width()
                max_height = surface.get_height()

            if "$(" in text:
                index = 0
                remove = False
                string = ""
                for character in text:
                    if text[index] == "$":
                        if index + 1 < len(text):
                            if text[index + 1] == "(":
                                remove = True
                    if text[index - 1] == ")" and remove:
                        remove = False

                    if remove is False:
                        string += character

                    index += 1
            else:
                string = text

            rendered_text_size = font.size(string)

            if position[0] == CENTERED:
                if using_display:
                    offset = 64
                else:
                    offset = 0
                position[0] = offset + (max_width - rendered_text_size[0]) / 2
            elif position[0] == LEFT:
                position[0] = 0
            elif position[0] == RIGHT:
                position[0] = max_width - rendered_text_size[0]

            if position[1] == CENTERED:
                position[0] = (max_height - rendered_text_size[1]) / 2
            elif position[1] == TOP:
                position[1] = 0
            elif position[1] == BOTTOM:
                position[1] = max_height - rendered_text_size[1]

            x_pos = position[0]
            y_pos = position[1]

            if fg_color is None:
                text_color = Registry.themes.font_color
            else:
                text_color = fg_color

            initial_font_color = text_color

            if bg_color is None:
                text_bg_color = None
            else:
                text_bg_color = bg_color

            font.set_underline(underline)
            font.set_bold(bold)
            font.set_italic(italic)

            if wrap is False and not "$(" in text:
                text_x = position[0] + rendered_text_size[0]
                if text_x < max_width and text_x >= 0:
                    text_y = position[1] + rendered_text_size[1]
                    if text_y < max_height and text_y >= 0:
                        rendered_text = font.render(
                            string,
                            aa,
                            text_color,
                            text_bg_color).convert_alpha()

                        surface.blit(
                            rendered_text,
                            position)

                        font.set_bold(False)
                        font.set_underline(False)
                        font.set_italic(False)
                        return (y_pos - position[1]) + rendered_text_size[1]

            index = 0
            remove = False
            for character in text:
                if text[index] == "$":
                    if index + 1 < len(text):
                        if text[index + 1] == "(":
                            remove = True
                if text[index - 1] == ")" and remove:
                    remove = False

                if remove is False:
                    rendered_character = font.render(
                        character,
                        aa,
                        text_color,
                        text_bg_color)

                    rendered_character = rendered_character.convert_alpha()

                else:
                    text_formatter = TextFormatter()
                    for key in text_formatter.custom_character_set_color:
                        if character == key:
                            color = text_formatter.custom_character_set_color[key]
                            if text_color == color or color == -1:
                                text_color = initial_font_color
                            else:
                                text_color = color

                    for key in TextFormatter().custom_character_set_format:
                        if character == key:
                            if key == "b":
                                font.set_bold(not font.get_bold())
                            elif key == "u":
                                font.set_underline(not font.get_underline())
                            elif key == "i":
                                font.set_italic(not font.get_italic())
                            elif key == "n":
                                x_pos = position[0]
                                y_pos += character_height

                if remove is False:
                    if rendered_character.get_width() + x_pos > max_width and wrap:
                        x_pos = position[0]
                        y_pos += character_height
                        if y_pos > max_height:
                            break
                    if blit:
                        surface.blit(
                            rendered_character,
                            (x_pos, y_pos))

                    x_pos += rendered_character.get_width()

                index += 1

            font.set_bold(False)
            font.set_underline(False)
            font.set_italic(False)
            return (y_pos - position[1]) + rendered_text_size[1]

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
