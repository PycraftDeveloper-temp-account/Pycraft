if __name__ != "__main__":
    print("Started <Pycraft_Settings>")

    class GenerateSettings:
        def __init__(self):
            pass

        def update_profile(self):
            if self.settings_preset == "low":
                self.FPS = 15
                self.aa = False
                self.render_fog = False
                self.fancy_graphics = False
                self.fancy_particles = False
                self.aFPS = (self.aFPS/self.iteration)
                self.iteration = 1

            elif self.settings_preset == "medium":
                self.FPS = 30
                self.aa = True
                self.render_fog = False
                self.fancy_graphics = True
                self.fancy_particles = False
                self.aFPS = (self.aFPS/self.iteration)
                self.iteration = 1
                
            elif self.settings_preset == "high":
                self.FPS = 60
                self.aa = True
                self.render_fog = True
                self.fancy_graphics = True
                self.fancy_particles = True
                self.aFPS = (self.aFPS/self.iteration)
                self.iteration = 1
                
            elif self.settings_preset == "adaptive":
                CPU_Freq = (self.mod_psutil__.cpu_freq(percpu=True)[0][2])/10
                MEM_Total = self.mod_psutil__.virtual_memory().total

                if (CPU_Freq > 300 and
                        MEM_Total > 8589934592):

                    self.aa = True
                    self.render_fog = True
                    self.fancy_graphics = True
                    self.fancy_particles = True

                elif (CPU_Freq > 200 and
                        MEM_Total > 4294967296):

                    self.aa = True
                    self.render_fog = True
                    self.fancy_graphics = True
                    self.fancy_particles = False

                elif (CPU_Freq > 100 and
                        MEM_Total > 2147483648):

                    self.aa = False
                    self.render_fog = False
                    self.fancy_graphics = True
                    self.fancy_particles = False

                elif (CPU_Freq < 100 and
                        CPU_Freq > 75 and
                        MEM_Total > 1073741824):

                    self.aa = False
                    self.render_fog = False
                    self.fancy_graphics = False
                    self.fancy_particles = False

        def create_information_message(self, general_font, text, saved_y_position, max_x, info_offset):
            position = ((self.real_window_width/2) + 40, (saved_y_position + 10) - info_offset)
            width = self.real_window_width - (max_x + 40)
            
            info_text_height = self.mod_text_utils__.TextWrap.blit_text(
                self,
                text,
                position,
                general_font,
                self.font_color,
                width)

            rect = self.mod_pygame__.Rect(
                position[0] - 10,
                position[1] - 10,
                (width - position[0]) + 20,
                info_text_height + 20)

            self.mod_pygame__.draw.rect(
                self.display,
                self.font_color,
                rect,
                width=1,
                border_radius=10)

            max_y_value = position[1] + info_text_height + info_offset
            if max_y_value > self.real_window_height:
                info_offset = (max_y_value - self.real_window_height) + 10
                
            else:
                info_offset = 0

            return info_offset

        def draw_buttons(self, button_pos, button_text_array, general_font, value, argument_variable, hovering, mouse_over):
            position = [
                0,
                button_pos]
            
            for i in range(len(button_text_array)):
                button_text = general_font.render(
                    button_text_array[i],
                    self.aa,
                    self.font_color).convert_alpha()
                
                button_text_width = button_text.get_width() + 20
                button_text_height = button_text.get_height() + 20
                
                rect = self.mod_pygame__.Rect(
                    position[0],
                    position[1],
                    button_text_width,
                    button_text_height)
                    
                if (self.mouse_x > position[0] and
                            self.mouse_x < position[0] + button_text_width and
                            self.mouse_y > position[1] and
                            self.mouse_y < position[1] + button_text_height):

                    hovering = True
                    mouse_over = True

                    if self.mouse_button_down:
                        self.mouse_button_down = False

                        if self.use_mouse_input is False:
                            self.mouse_y = button_pos + 5 + button_text_height
                        
                        if self.sound:
                            self.mod_sound_utils__.play_sound.play_click_sound(
                                self)
                            
                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.accent_color,
                            rect,
                            width=1,
                            border_radius=10)

                        self.__dict__[argument_variable] = button_text_array[i]

                        self.mod_theme_utils__.determine_theme_colours.get_colors(self)

                        GenerateSettings.update_profile(self)
                        
                    else:
                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.font_color,
                            rect,
                            width=1, 
                            border_radius=10)

                else:
                    if button_text_array[i] == value:
                        self.mod_pygame__.draw.rect(
                        self.display,
                        self.accent_color,
                        rect,
                        width=1,
                        border_radius=10)
                        
                    else:
                        self.mod_pygame__.draw.rect(
                            self.display,
                            self.shape_color,
                            rect,
                            width=1,
                            border_radius=10)
                        
                self.display.blit(
                    button_text,
                    (position[0]+10,
                        position[1]+10))
                
                position[0] += button_text_width + 3

            return button_text_height + 20, hovering, mouse_over

        def draw_slider(self, slider_pos, minimum, maximum, value, argument_variable, hovering, mouse_over):
            if (argument_variable == "music_volume" and
                    self.music is False):
                
                enable = False
                
            elif (argument_variable == "sound_volume" and
                    self.sound is False):
                
                enable = False
                
            else:
                enable = True
                
            position = [
                0,
                slider_pos]
            
            height = 10
            slider_range = maximum - minimum
            length = self.real_window_width/2
            
            rect = self.mod_pygame__.Rect(
                position[0],
                position[1],
                length,
                height)
            
            self.mod_pygame__.draw.rect(
                self.display,
                self.shape_color,
                rect,
                border_radius=10)
            
            self.mod_pygame__.draw.rect(
                self.display,
                self.background_color,
                rect,
                width=3,
                border_radius=10)

            circle_pos_x = (value - minimum) / (slider_range / length)
            circle_pos_y = position[1] + height/2
            circle_pos = (circle_pos_x, circle_pos_y)

            if (self.mouse_x > position[0] and
                    self.mouse_x < length and
                    self.mouse_y > position[1] - 15 and
                    self.mouse_y < position[1] + height + 15 and
                    enable):

                hovering = True
                mouse_over = True

                if self.mouse_button_down:
                    self.mod_pygame__.event.set_blocked(self.mod_pygame__.MOUSEMOTION)
                    self.__dict__[argument_variable] = (
                        (slider_range / length) * self.mouse_x) + minimum

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.accent_color,
                        rect,
                        width=1,
                        border_radius=10)
                    
                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.accent_color,
                        circle_pos,
                        radius=10)
                    
                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.background_color,
                        circle_pos,
                        radius=6)
                    
                else:
                    self.mod_pygame__.event.set_allowed(self.mod_pygame__.MOUSEMOTION)
                    
                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.font_color,
                        rect,
                        width=1,
                        border_radius=10)
                    
                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.font_color,
                        circle_pos,
                        radius=10)
                    
                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.background_color,
                        circle_pos,
                        radius=6)

            else:
                self.mod_pygame__.draw.rect(
                    self.display,
                    self.shape_color,
                    rect,
                    width=1,
                    border_radius=10)
                
                self.mod_pygame__.draw.circle(
                    self.display,
                    self.shape_color,
                    circle_pos,
                    radius=10)
                
                self.mod_pygame__.draw.circle(
                    self.display,
                    self.background_color,
                    circle_pos,
                    radius=6)

            return height + 20, hovering, mouse_over

        def draw_toggle(self, toggle_pos, value_0, value_1, value, argument_variable, hovering, mouse_over):
            position = [0, toggle_pos]
            height = 10
            
            rect = self.mod_pygame__.Rect(
                position[0],
                position[1],
                36,
                height)
            
            self.mod_pygame__.draw.rect(
                self.display,
                self.shape_color,
                rect,
                border_radius=10)
            
            self.mod_pygame__.draw.rect(
                self.display,
                self.background_color,
                rect,
                width=3,
                border_radius=10)

            if value == value_0:
                toggle_value = 30
            if value == value_1:
                toggle_value = 10
                
            circle_pos_x = toggle_value
            circle_pos_y = position[1] + height/2
            circle_pos = (circle_pos_x, circle_pos_y)

            if self.music is False:
                self.mod_pygame__.mixer.music.fadeout(500)

            if (self.mouse_x > position[0] and
                    self.mouse_x < 36 + 20 and
                    self.mouse_y > position[1] - 15 and
                    self.mouse_y < position[1] + height + 15):

                hovering = True
                mouse_over = True

                if self.mouse_button_down:
                    self.mouse_button_down = False

                    self.__dict__[argument_variable] = not self.__dict__[argument_variable]

                    if self.use_mouse_input is False:
                        self.mouse_x += 36
                    
                    if self.sound:
                        self.mod_sound_utils__.play_sound.play_click_sound(
                            self)
                    
                else:
                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.font_color,
                        rect,
                        width=1,
                        border_radius=10)
                    
                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.font_color,
                        circle_pos,
                        radius=10)
                    
                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.background_color,
                        circle_pos,
                        radius=6)

            else:
                if value:
                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.accent_color,
                        rect,
                        width=1,
                        border_radius=10)
                    
                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.accent_color,
                        circle_pos,
                        radius=10)
                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.background_color,
                        circle_pos,
                        radius=6)
                    
                else:
                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        rect,
                        width=1,
                        border_radius=10)
                    
                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.shape_color,
                        circle_pos,
                        radius=10)
                    
                    self.mod_pygame__.draw.circle(
                        self.display,
                        self.background_color,
                        circle_pos,
                        radius=6)

            return height + 20, hovering, mouse_over

        def Settings(self):
            try:
                self.mod_caption_utils__.generate_captions.get_normal_caption(
                    self,
                    "Settings")

                if self.platform == "Linux":
                    subtitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 35)

                    button_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    general_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")), 15)
                    
                else:
                    subtitle_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 35)

                    button_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    general_font = self.mod_pygame__.font.Font(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")), 15)

                title_font = self.title_font.render(
                    "Pycraft",
                    self.aa,
                    self.font_color)

                title_width = title_font.get_width()

                settings_font = subtitle_font.render(
                    "Settings",
                    self.aa,
                    self.secondary_font_color)

                button_offset = 0

                current_menu = "General"
                hover_menu = None

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2

                if self.platform == "Linux":
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files//settings_config.json")), "r") as openFile:

                        settings_structure = self.mod_json__.load(openFile)

                    selector = self.mod_pygame__.image.load(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            (f"resources//general resources//selectorICON{self.theme}.jpg")))
                    selector.convert()

                else:
                    with open(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            ("data files\\settings_config.json")), "r") as openFile:

                        settings_structure = self.mod_json__.load(openFile)

                    selector = self.mod_pygame__.image.load(
                        self.mod_OS__.path.join(
                            self.base_folder,
                            (f"resources\\general resources\\selectorICON{self.theme}.jpg")))
                    selector.convert()

                selector_width = selector.get_width()

                initial_theme = self.theme

                hovering = False
                max_x = 0
                info_offset = 0

                while True:
                    start_time = self.mod_time__.perf_counter()

                    self.mod_display_utils__.display_functionality.core_display_functions(
                        self)

                    self.mod_caption_utils__.generate_captions.get_normal_caption(
                        self,
                        "Settings")

                    self.display.fill(self.background_color)

                    cover_Rect = self.mod_pygame__.Rect(
                        0,
                        0,
                        self.real_window_width,
                        90)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.background_color,
                        cover_Rect)

                    self.display.blit(
                        title_font,
                        ((self.real_window_width-title_width)/2, 0))

                    self.display.blit(
                        settings_font,
                        (((self.real_window_width-title_width)/2)+55, 50))

                    if initial_theme != self.theme:
                        title_font = self.title_font.render(
                            "Pycraft",
                            self.aa,
                            self.font_color)

                        title_width = title_font.get_width()

                        settings_font = subtitle_font.render(
                            "Settings",
                            self.aa,
                            self.secondary_font_color)
                
                        initial_theme = self.theme
                        if self.platform == "Linux":
                            selector = self.mod_pygame__.image.load(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    (f"resources//general resources//selectorICON{self.theme}.jpg")))
                            selector.convert()

                        else:
                            selector = self.mod_pygame__.image.load(
                                self.mod_OS__.path.join(
                                    self.base_folder,
                                    (f"resources\\general resources\\selectorICON{self.theme}.jpg")))
                            selector.convert()

                        selector_width = selector.get_width()

                    button_y_position = 0
                    button_id = 0
                    for key in settings_structure:
                        if (key == "Developer options" and
                                self.devmode != 10):
                            
                            font_color = self.shape_color
                            button_font.set_underline(False)
                            
                        else:
                            if key == hover_menu:
                                button_font.set_underline(True)

                            else:
                                button_font.set_underline(False)

                            
                            font_color = self.font_color
                            
                        button = button_font.render(
                            key,
                            self.aa,
                            font_color).convert_alpha()
                        button_width = button.get_width()
                        button_height = button.get_height()

                        if button_width > max_x:
                            max_x = button_width
                        
                        button_height += 50 - button_height

                        button_blit_y = (button_y_position * self.y_scale_factor) + button_offset
                        button_blit_x = (self.real_window_width-button_width)-2

                        if key == hover_menu:
                            if not (key == "Developer options" and self.devmode != 10):
                        
                                self.display.blit(
                                    selector,
                                    (self.real_window_width-(button_width+selector_width)-2,
                                        button_blit_y))
                            
                        self.display.blit(
                            button,
                            (button_blit_x,
                                button_blit_y))

                        if ((self.mouse_x > button_blit_x and
                                    self.mouse_x < self.real_window_width and
                                    self.mouse_y > button_blit_y and
                                    self.mouse_y < button_blit_y + button_height) and
                                not (key == "Developer options" and 
                                    self.devmode != 10)):
                            
                            hover_menu = key
                            hovering = True

                            if (self.mouse_button_down and
                                    current_menu != key):
                                
                                current_menu = key
                                self.mouse_button_down = False
                                
                                if self.sound:
                                    self.mod_sound_utils__.play_sound.play_click_sound(
                                        self)
                                    
                        else:
                            if hover_menu == key:
                                hover_menu = None

                        button_y_position += button_height

                        sub_menu = settings_structure[current_menu]

                        general_y_position = 100

                        if sub_menu[0] is not None:
                            for item in range(len(sub_menu)):
                                data = []
                                mouse_over = False
                                    
                                for entry in range(3, len(sub_menu[item])):
                                    if str(sub_menu[item][entry]) == "aFPS":
                                        argument = int(self.aFPS/self.iteration)
                                        
                                    else:
                                        if str(sub_menu[item][entry]) == "use_mouse_input":
                                            argument = not self.__dict__[sub_menu[item][entry]]
                                        else:
                                            argument = self.__dict__[sub_menu[item][entry]]
                                            
                                        if "float" in str(type(argument)):
                                            argument = int(argument)
                                            
                                        if argument is True:
                                            argument = "Enabled"
                                            
                                        if argument is False:
                                            argument = "Disabled"
                                        
                                    data.append(argument)

                                if (sub_menu[item][3] == "music_volume" and
                                        self.music is False):
                                    
                                    font_color = self.shape_color
                                    
                                elif (sub_menu[item][3] == "sound_volume" and
                                        self.sound is False):
                                    
                                    font_color = self.shape_color
                                    
                                else:
                                    font_color = self.font_color
                                    
                                text = general_font.render(
                                    str(sub_menu[item][0]).format(*data),
                                    self.aa,
                                    font_color).convert_alpha()
                                text_height = text.get_height()
                                
                                self.display.blit(
                                    text,
                                    (0, general_y_position))
                                            
                                argument_variable = sub_menu[item][3]
                                saved_y_position = general_y_position
                                
                                name = str(sub_menu[item][entry])
                                if name == "use_mouse_input":
                                    value = not self.__dict__[argument_variable]
                                    
                                else:
                                    value = self.__dict__[argument_variable]
                                    
                                if list(sub_menu[item][2].keys())[0] == "button":
                                    button_pos = general_y_position + text_height + 10
                                    button_text_array = sub_menu[item][2]["button"]
                                    
                                    button_height, hovering, mouse_over = GenerateSettings.draw_buttons(
                                        self,
                                        button_pos,
                                        button_text_array,
                                        general_font,
                                        value,
                                        argument_variable,
                                        hovering,
                                        mouse_over)
                                    
                                    general_y_position += button_height

                                if list(sub_menu[item][2].keys())[0] == "slider":
                                    slider_pos = general_y_position + text_height + 10
                                    slider_array = sub_menu[item][2]["slider"]
                                    minimum = slider_array[0]
                                    maximum = slider_array[1]
                                    
                                    slider_height, hovering, mouse_over = GenerateSettings.draw_slider(
                                        self,
                                        slider_pos,
                                        minimum,
                                        maximum,
                                        value,
                                        argument_variable,
                                        hovering,
                                        mouse_over)
                                    
                                    general_y_position += slider_height

                                if list(sub_menu[item][2].keys())[0] == "toggle":
                                    toggle_pos = general_y_position + text_height + 10
                                    slider_array = sub_menu[item][2]["toggle"]
                                    value_0 = slider_array[0]
                                    value_1 = slider_array[1]
                                    
                                    toggle_height, hovering, mouse_over = GenerateSettings.draw_toggle(
                                        self,
                                        toggle_pos,
                                        value_0,
                                        value_1,
                                        value,
                                        argument_variable,
                                        hovering,
                                        mouse_over)
                                    
                                    general_y_position += toggle_height

                                if mouse_over:
                                    info_offset = GenerateSettings.create_information_message(
                                        self,
                                        general_font,
                                        sub_menu[item][1],
                                        saved_y_position,
                                        max_x,
                                        info_offset)
                                    
                                general_y_position += text_height

                        button_id += 1
                        
                    button_y_position *= self.y_scale_factor

                    button_offset = (self.real_window_height - button_y_position) / 2

                    self.mod_drawing_utils__.generate_graph.create_devmode_graph(
                        self,
                        general_font)

                    if self.go_to is None:
                        self.mod_display_utils__.display_animations.fade_in(
                            self)
                    else:
                        self.mod_display_utils__.display_animations.fade_out(
                            self)

                    if not self.startup_animation and (self.go_to is not None):
                        return None

                    if hovering:
                        hovering = False
                        self.mod_pygame__.mouse.set_cursor(
                                self.mod_pygame__.cursors.Cursor(
                                    self.mod_pygame__.SYSTEM_CURSOR_HAND))
                    else:
                        self.mod_pygame__.mouse.set_cursor(
                            self.mod_pygame__.cursors.Cursor(
                                self.mod_pygame__.SYSTEM_CURSOR_ARROW))
                        
                    self.mod_pygame__.display.flip()
                    self.clock.tick(
                        self.mod_display_utils__.display_utils.get_play_status(self))

                    if self.error_message is not None:
                        self.error_message = "".join(
                            ("Settings > GenerateSettings > Settings: ",
                             str(self.error_message)))

                        return

                    self.run_timer += self.mod_time__.perf_counter()-start_time
            except Exception as Message:
                self.error_message = (
                    f"Settings > GenerateSettings > Settings: {str(Message)}")

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)

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
