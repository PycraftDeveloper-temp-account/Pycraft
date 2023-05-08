if __name__ != "__main__":
    try:
        import pygame
        
        from registry_utils import Registry
        
        import sound_utils
        import setting_preset_utils
        import theme_utils
        import text_utils
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in button_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class draw_setting_elements(Registry):
        def draw_multi_buttons(
                self,
                button_pos: int,
                button_text_array: list,
                font: pygame.font.Font,
                backup_font: pygame.font.Font,
                argument_variable,
                hovering: bool,
                mouse_over: bool,
                scrollbar_needed: bool):

            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            position = [
                scroll_x_offset,
                button_pos]

            for text in button_text_array:
                returned_text = text_utils.text_formatter.format_text(
                    text,
                    ("left", "top"),
                    font,
                    backup_font,
                    blit=False)

                button_text_width = returned_text.get_width() + 20
                button_text_height = returned_text.get_height() + 20

                rect = pygame.Rect(
                    position[0],
                    position[1],
                    button_text_width,
                    button_text_height)
                
                if rect.collidepoint((
                        Registry.mouse_x,
                        Registry.mouse_y)):

                    hovering = True
                    mouse_over = True

                    if Registry.primary_mouse_button_down:
                        Registry.primary_mouse_button_down = False

                        if Registry.use_mouse_input is False:
                            Registry.mouse_y = button_pos + 5 + button_text_height

                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        pygame.draw.rect(
                            Registry.display,
                            Registry.accent_color,
                            rect,
                            width=1,
                            border_radius=10)
                        
                        updated_argument = Registry.__dict__[argument_variable]
                        
                        updated_argument[text] = not updated_argument[text]
                        setattr(Registry, argument_variable, updated_argument)

                        theme_utils.determine_theme_colors.get_colors()

                        setting_preset_utils.presets.update_profile()

                    else:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.font_color,
                            rect,
                            width=1,
                            border_radius=10)

                else:
                    if Registry.__dict__[argument_variable][text]:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.accent_color,
                            rect,
                            width=1,
                            border_radius=10)

                    else:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.shape_color,
                            rect,
                            width=1,
                            border_radius=10)

                Registry.display.blit(
                    returned_text,
                    (position[0]+10,
                        position[1]+10))

                position[0] += button_text_width + 3

            return (button_text_height + 20,
                hovering,
                mouse_over)

        def draw_buttons(
                self,
                button_pos: int,
                button_text_array: list,
                font: pygame.font.Font,
                backup_font: pygame.font.Font,
                value: str,
                argument_variable,
                hovering: bool,
                mouse_over: bool,
                files_to_remove: bool,
                clear_languages: bool,
                scanned_files: bool,
                scrollbar_needed: bool):
            
            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            if (argument_variable == "aa_quality" and
                    Registry.aa is False):

                enable = False

            elif (argument_variable == "clear_cache" and
                        (files_to_remove is False or
                            Registry.remove_file_permission is False)):

                enable = False

            elif (argument_variable == "clear_languages_cache" and
                        (clear_languages is False or
                            Registry.remove_file_permission is False)):

                enable = False

            elif (argument_variable == "scan_pycraft" and
                    scanned_files):

                enable = False

            else:
                enable = True
                
            position = [
                scroll_x_offset,
                button_pos]

            for text in button_text_array:
                if enable:
                    returned_text = text_utils.text_formatter.format_text(
                        text,
                        ("left", "top"),
                        font,
                        backup_font,
                        blit=False,
                        font_color=Registry.font_color)
                    
                else:
                    returned_text = text_utils.text_formatter.format_text(
                        text,
                        ("left", "top"),
                        font,
                        backup_font,
                        blit=False,
                        font_color=Registry.shape_color)

                button_text_width = returned_text.get_width() + 20
                button_text_height = returned_text.get_height() + 20

                rect = pygame.Rect(
                    position[0],
                    position[1],
                    button_text_width,
                    button_text_height)
                
                pygame.draw.rect(
                    Registry.display,
                    Registry.background_color,
                    rect,
                    border_radius=10)
                
                if (rect.collidepoint((
                            Registry.mouse_x,
                            Registry.mouse_y))
                        and enable):

                    hovering = True
                    mouse_over = True

                    if Registry.primary_mouse_button_down:
                        Registry.primary_mouse_button_down = False

                        if Registry.use_mouse_input is False:
                            Registry.mouse_y = button_pos + 5 + button_text_height

                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        pygame.draw.rect(
                            Registry.display,
                            Registry.accent_color,
                            rect,
                            width=1,
                            border_radius=10)
                        
                        setattr(Registry, argument_variable, text)

                        theme_utils.determine_theme_colors.get_colors()

                        setting_preset_utils.presets.update_profile()

                    else:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.font_color,
                            rect,
                            width=1,
                            border_radius=10)

                else:
                    if text == value:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.accent_color,
                            rect,
                            width=1,
                            border_radius=10)

                    else:
                        pygame.draw.rect(
                            Registry.display,
                            Registry.shape_color,
                            rect,
                            width=1,
                            border_radius=10)

                Registry.display.blit(
                    returned_text,
                    (position[0]+10,
                        position[1]+10))

                position[0] += button_text_width + 3

            return (button_text_height + 20,
                hovering,
                mouse_over)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
