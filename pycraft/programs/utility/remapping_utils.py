if __name__ != "__main__":
    try:
        import pygame
        
        import logging_utils
        import text_utils
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

        def draw_remap_function(
                self,
                remap_pos,
                options,
                hovering,
                mouse_over,
                font,
                backup_font,
                maximum_remap_width,
                display_events,
                scrollbar_needed,
                aa,
                font_color,
                display,
                mouse_x,
                mouse_y,
                input_key,
                accent_color,
                shape_color,
                logging_dictionary,
                output_log,
                platform,
                base_folder,
                selected_input_reconfig,
                language,
                translated_text,
                connection_permission):
            
            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            position = [
                scroll_x_offset,
                remap_pos]

            index = 0
            enable = False
            maximum_height = 0
            for key in options:
                text = f"Function: {list(options.keys())[index]}, is bound to: {options[key]}."

                (translated_text,
                    returned_text) = text_utils.text_formatter.format_text(
                    text,
                    language,
                    display,
                    ("right", 200*self.y_scale_factor),
                    font_color,
                    aa,
                    False,
                    False,
                    False,
                    font,
                    backup_font,
                    translated_text,
                    logging_dictionary,
                    output_log,
                    platform,
                    base_folder,
                    connection_permission,
                    blit=False)

                button_text_width = returned_text.get_width() + 20

                if button_text_width > maximum_remap_width:
                    maximum_remap_width = button_text_width
                    
                button_text_height = returned_text.get_height() + 20

                display.blit(returned_text, (position[0] + 10, position[1] + 10))

                rect = pygame.Rect(
                    position[0],
                    position[1],
                    maximum_remap_width,
                    button_text_height)

                if (mouse_x > position[0] and
                    mouse_x < maximum_remap_width and
                    mouse_y > position[1] and
                    mouse_y < position[1] + button_text_height):

                    hovering = True
                    mouse_over = True
                    disable_events = True
                    enable = True

                    keydown = False

                    for event in display_events:
                        if (event.type == pygame.KEYDOWN and
                                selected_input_reconfig == "keyboard"):
                            
                            keydown = True

                            try:
                                i = 0
                                for element in input_key:
                                    if event.key == input_key[element][0]:
                                        rebind = True
                                        for bound_key in options:
                                            if options[bound_key] == list(input_key.keys())[i]:
                                                rebind = False

                                        if rebind:
                                            key_pressed = list(input_key.keys())[i]
                                            break
                                        
                                    i += 1

                                for key_id, value in input_key.items():
                                    if input_key[key_pressed] == value:
                                        break
                                    
                                options[list(options.keys())[index]] = key_id

                            except Exception as Message:
                                log_message = "DrawingUtils > draw_setting_elements > draw_remap_function: " + str(Message)

                                logging_utils.create_log_message.update_log_warning(
                                    logging_dictionary,
                                    log_message,
                                    output_log,
                                    platform,
                                    base_folder)

                    if keydown:
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
                    pygame.draw.rect(
                        display,
                        shape_color,
                        rect,
                        width=1,
                        border_radius=10)

                position[1] += button_text_height + 3
                maximum_height += button_text_height + 3

                index += 1

            if enable is False:
                disable_events = False

            return (maximum_height,
                        hovering,
                        mouse_over,
                        maximum_remap_width,
                        disable_events,
                        translated_text)

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
