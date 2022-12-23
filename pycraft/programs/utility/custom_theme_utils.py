if __name__ != "__main__":
    try:
        import pygame
        
        import sound_utils
        import theme_utils
        import translation_utils
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
            
    class draw_setting_elements:
        def __init__(self):
            pass

        def draw_custom_theme_options(
                self,
                button_pos,
                font,
                backup_font,
                hovering,
                mouse_over,
                scrollbar_needed,
                aa,
                font_color,
                display,
                mouse_x,
                mouse_y,
                sound,
                accent_color,
                shape_color,
                platform,
                base_folder,
                use_mouse_input,
                sound_volume,
                background_color,
                secondary_font_color,
                language,
                logging_dictionary,
                output_log,
                translated_text,
                connection_permission,
                custom_theme_choice,
                custom_theme,
                display_events):

            if (language == "ar" or
                    language == "hy" or
                    language == "zh-tw" or
                    language == "zh-cn" or
                    language == "ka" or
                    language == "el" or
                    language == "hi" or
                    language == "he" or
                    language == "iw" or
                    language == "ja" or
                    language == "kk" or
                    language == "km" or
                    language == "ko" or
                    language == "mn" or
                    language == "my" or
                    language == "ne" or
                    language == "ps" or
                    language == "ru" or
                    language == "ta" or
                    language == "th" or
                    language == "uk" or
                    language == "ur"):
                font = backup_font
            
            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            position = [
                scroll_x_offset,
                button_pos]

            total_height = 0

            button_text_array = []
            for key in custom_theme:
                formatted_key = key.replace("_", " ")
                formatted_color = f"({str(custom_theme[key])[1:-1]})"
                option = f"{formatted_key}: "
                details = [option, formatted_color]
                button_text_array.append(details)

            for i in range(len(button_text_array)):
                if custom_theme_choice == list(custom_theme)[i]:
                    index = 0
                    string = str(custom_theme[list(custom_theme)[i]])[1:-1]
                    for event in display_events:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                if len(string) == 0:
                                    (_,
                                        font_color,
                                        background_color,
                                        shape_color,
                                        accent_color,
                                        secondary_font_color) = theme_utils.determine_theme_colours.get_colors(
                                            self,
                                            "custom",
                                            self.custom_theme,
                                            self.colour_presets)

                                    default_custom_theme = {
                                        "font_color": font_color,
                                        "background_color": background_color,
                                        "shape_color": shape_color,
                                        "accent_color": accent_color,
                                        "secondary_font_color": secondary_font_color}
            
                                    string = str(default_custom_theme[list(custom_theme)[i]])[1:-1]
                                else:
                                    string = string[:-1]
                            else:
                                try:
                                    converted = chr(event.key)
                                except:
                                    pass
                                else:
                                    if ord(converted) >= 32 and ord(converted) <= 126:
                                        string += converted
                                
                            del display_events[index]

                        index += 1

                    custom_theme[list(custom_theme)[i]] = f"[{string}]"

                    button_text_array = []
                    for key in custom_theme:
                        formatted_key = key.replace("_", " ")
                        formatted_color = f"({str(custom_theme[key])[1:-1]})"
                        option = f"{formatted_key}: "
                        details = [option, formatted_color]
                        button_text_array.append(details)
                                
                (translated_output,
                    translated_text) = translation_utils.string_translator.change_language(
                        language,
                        button_text_array[i][0],
                        translated_text,
                        logging_dictionary,
                        output_log,
                        platform,
                        base_folder,
                        connection_permission)
                
                returned_text = font.render(
                    translated_output + button_text_array[i][1],
                    aa,
                    font_color)

                button_text_width = returned_text.get_width() + 20
                button_text_height = returned_text.get_height() + 20

                rect = pygame.Rect(
                    position[0],
                    position[1],
                    button_text_width,
                    button_text_height)

                if (mouse_x > position[0] and
                    mouse_x < position[0] + button_text_width and
                    mouse_y > position[1] and
                    mouse_y < position[1] + button_text_height):

                    hovering = True
                    mouse_over = True

                    if self.mouse_button_down:
                        self.mouse_button_down = False

                        if custom_theme_choice == list(custom_theme)[i]:
                            custom_theme_choice = None
                        else:
                            custom_theme_choice = list(custom_theme)[i]
                            
                        if use_mouse_input is False:
                            mouse_y = button_pos + 5 + button_text_height

                        if sound:
                            sound_utils.play_sound.play_click_sound(
                                platform,
                                base_folder,
                                sound_volume)

                        pygame.draw.rect(
                            display,
                            accent_color,
                            rect,
                            width=1,
                            border_radius=10)

                    else:
                        pygame.draw.rect(
                            display,
                            font_color,
                            rect,
                            width=1,
                            border_radius=10)

                else:
                    if custom_theme_choice == list(custom_theme)[i]:
                        pygame.draw.rect(
                            display,
                            accent_color,
                            rect,
                            width=1,
                            border_radius=10)

                    else:
                        pygame.draw.rect(
                            display,
                            shape_color,
                            rect,
                            width=1,
                            border_radius=10)

                display.blit(
                    returned_text,
                    (position[0]+10,
                        position[1]+10))

                position[1] += button_text_height + 3
                total_height += button_text_height

            return (total_height + 20,
                hovering,
                mouse_over,
                translated_text,
                custom_theme_choice,
                custom_theme)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
