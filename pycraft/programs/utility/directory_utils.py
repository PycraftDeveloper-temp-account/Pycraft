if __name__ != "__main__":
    try:
        import pygame
        
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

        def draw_directory_structure(
                self,
                slider_pos,
                font,
                backup_font,
                hovering,
                mouse_over,
                hover_id,
                hovering_over_key,
                scrollbar_needed,
                aa,
                font_color,
                display,
                mouse_x,
                mouse_y,
                shape_color,
                real_window_width,
                file_structure,
                folder_size,
                background_color,
                language,
                logging_dictionary,
                output_log,
                platform,
                base_folder,
                translated_text,
                connection_permission):
            
            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            position = [
                scroll_x_offset,
                slider_pos]

            height = 23
            total_height = height
            length = real_window_width/2

            rect = pygame.Rect(
                position[0],
                position[1],
                length,
                height)

            pygame.draw.rect(
                display,
                shape_color,
                rect,
                border_radius=10)

            x_pos = 0
            hover_area = False
            for key in file_structure:
                width = ((real_window_width/2)/folder_size) * file_structure[key]["size"]

                if ((mouse_x > position[0] + x_pos and
                            mouse_x < position[0] + x_pos + width and
                            mouse_y > position[1] and
                            mouse_y < position[1] + height) or
                        hover_id == file_structure[key]):

                    hovering = True
                    mouse_over = True

                    if hover_id != file_structure[key]:
                        hover_id = file_structure[key]
                        hover_area = True
                
                inside_rect = pygame.Rect(
                    position[0] + x_pos,
                    position[1],
                    width,
                    height)

                if hover_id is not None:
                    if hover_id == file_structure[key]:
                        pygame.draw.rect(
                            display,
                            file_structure[key]["color"],
                            inside_rect)
                        
                else:
                    pygame.draw.rect(
                        display,
                        file_structure[key]["color"],
                        inside_rect)

                x_pos += width

            pygame.draw.rect(
                display,
                background_color,
                rect,
                width=3,
                border_radius=10)

            padding_rect = pygame.Rect(
                position[0]-10,
                position[1]-10,
                length+20,
                height+20)

            pygame.draw.rect(
                display,
                background_color,
                padding_rect,
                width=10,
                border_radius=20)

            total_height += 20

            text_position = [scroll_x_offset, slider_pos + height + 20]

            text_max_height = 0

            hover_text = False
            for key in file_structure:
                percentage = (100/folder_size) * file_structure[key]["size"]
                    
                if (hover_id is not None or
                        hovering_over_key):

                    (translated_text,
                        returned_text) = text_utils.text_formatter.format_text(
                        f"{str(key)}: {int(percentage)}%",
                        language,
                        display,
                        text_position,
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

                else:
                    (translated_text,
                        returned_text) = text_utils.text_formatter.format_text(
                        f"{str(key)}: {int(percentage)}%",
                        language,
                        display,
                        text_position,
                        file_structure[key]["color"],
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
                    
                text_width = returned_text.get_width()
                text_height = returned_text.get_height()

                if text_position[0] + text_width > (real_window_width / 2):
                    text_position[0] = scroll_x_offset
                    text_position[1] += text_height + 20
                    total_height += text_height + 20

                if ((mouse_x > text_position[0] - 10 and
                            mouse_x < text_position[0] + text_width + 10 and
                            mouse_y > text_position[1] - 10 and
                            mouse_y < text_position[1] + text_height + 10) or
                        hover_id == file_structure[key]):

                    hovering = True
                    hovering_over_key = True
                    mouse_over = True

                    (translated_text,
                        returned_text) = text_utils.text_formatter.format_text(
                        f"{str(key)}: {int(percentage)}%",
                        language,
                        display,
                        text_position,
                        file_structure[key]["color"],
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
                    
                    if hover_id != file_structure[key]:
                        hover_id = file_structure[key]
                        hover_text = True
                
                if text_height > text_max_height:
                    text_max_height = text_height
                    
                display.blit(returned_text, text_position)
                text_position[0] += text_width + 20

            if hover_area is False and hover_text is False:
                hover_id = None

            if (mouse_x > position[0] and
                    mouse_x < length and
                    mouse_y > position[1] - 15 and
                    mouse_y < position[1] + height + 15):

                hovering = True
                mouse_over = True

                pygame.event.set_allowed(
                    pygame.MOUSEMOTION)

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

            total_height += text_height + 40

            return total_height, hovering, mouse_over, hover_id, translated_text

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
