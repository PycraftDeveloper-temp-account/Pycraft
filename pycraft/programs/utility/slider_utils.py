if __name__ != "__main__":
    try:
        import pygame
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

        def draw_slider(self,
                slider_pos,
                minimum,
                maximum,
                value,
                argument_variable,
                hovering,
                mouse_over,
                scrollbar_needed,
                font_color,
                display,
                mouse_x,
                mouse_y,
                accent_color,
                shape_color,
                music,
                sound,
                real_window_width,
                vsync,
                background_color):
            
            if scrollbar_needed:
                scroll_x_offset = 9
                
            else:
                scroll_x_offset = 0
                
            if (argument_variable == "music_volume" and
                    music is False):

                enable = False

            elif (argument_variable == "sound_volume" and
                    sound is False):

                enable = False

            elif (argument_variable == "fps" and
                    vsync):

                enable = False

            else:
                enable = True

            position = [
                scroll_x_offset,
                slider_pos]

            height = 10
            slider_range = maximum - minimum
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

            pygame.draw.rect(
                display,
                background_color,
                rect,
                width=3,
                border_radius=10)

            circle_pos_x = ((value - minimum) /
                            (slider_range / length)) + scroll_x_offset
            circle_pos_y = position[1] + height/2
            circle_pos = (circle_pos_x, circle_pos_y)

            if (mouse_x > position[0] and
                    mouse_x < length and
                    mouse_y > position[1] - 15 and
                    mouse_y < position[1] + height + 15 and
                    enable):

                hovering = True
                mouse_over = True

                if self.mouse_button_down:
                    pygame.event.set_blocked(
                        pygame.MOUSEMOTION)
                    
                    self.__dict__[argument_variable] = (
                        (slider_range / length) * mouse_x) + minimum

                    pygame.draw.rect(
                        display,
                        accent_color,
                        rect,
                        width=1,
                        border_radius=10)

                    pygame.draw.circle(
                        display,
                        accent_color,
                        circle_pos,
                        radius=10)

                    pygame.draw.circle(
                        display,
                        background_color,
                        circle_pos,
                        radius=6)

                else:
                    pygame.event.set_allowed(
                        pygame.MOUSEMOTION)

                    pygame.draw.rect(
                        display,
                        font_color,
                        rect,
                        width=1,
                        border_radius=10)

                    pygame.draw.circle(
                        display,
                        font_color,
                        circle_pos,
                        radius=10)

                    pygame.draw.circle(
                        display,
                        background_color,
                        circle_pos,
                        radius=6)

            else:
                pygame.draw.rect(
                    display,
                    shape_color,
                    rect,
                    width=1,
                    border_radius=10)

                pygame.draw.circle(
                    display,
                    shape_color,
                    circle_pos,
                    radius=10)

                pygame.draw.circle(
                    display,
                    background_color,
                    circle_pos,
                    radius=6)

            return height + 20, hovering, mouse_over

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
