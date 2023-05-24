if __name__ != "__main__":
    try:
        import time
        import traceback
        import threading
        import random
        import pathlib

        import pygame
        import pyautogui
        
        from registry_utils import Registry
        
        import display_utils
        import error_utils
        import caption_utils
        import sound_utils
        import drawing_utils
        import text_utils
        import image_utils
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in home"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class generate_home(Registry):
        def __init__(self) -> None:
            self.show_message = None
            self.messageColor = Registry.font_color
            self.theme_path = self.get_theme_path()
            self.selector = pygame.image.load(self.theme_path)
            self.selector.convert()

            self.selector_width = self.selector.get_width()
            
            self.hover1 = False
            self.hover2 = False
            self.hover3 = False
            self.hover4 = False
            self.hover5 = False
            self.hover6 = False
            self.hover7 = False
            
            self.play_width = 0
            self.settings_width = 0
            self.char_designer_width = 0
            self.credits_width = 0
            self.achievements_width = 0
            self.benchmark_width = 0
            
            if Registry.linked_to_installer:
                self.installer_width = 0
                
            self.increment = False
            self.ColourDisplacement = 80
            
            self.oldTHEME = Registry.theme
            self.create_image_of_surface = False
            self.prev_joystick_connected = False
            
            self.special = [
                30,
                30,
                30]
            
            self.anim = False
            self.TargetARRAY = []
            
            self.banner_RenderedText = False
            self.banner_timer_start = 0
        
        def get_theme_path(self) -> pathlib.Path:
            return Registry.base_folder / "resources" / "general resources" / f"selectorICON{Registry.theme}.png"
        
        def compute(self) -> None:
            display_utils.display_functionality.core_display_functions(
                location="saveANDexit")

            caption_utils.generate_captions.set_caption(
                    
            if not self.oldTHEME == Registry.theme:
                self.theme_path = self.get_theme_path()
                selector = pygame.image.load(self.theme_path)
                selector.convert()

                self.selector_width = selector.get_width()
                self.oldTHEME = Registry.theme
                
            if Registry.go_to is None:
                if (Registry.mouse_y >= 202*Registry.y_scale_factor and
                        Registry.mouse_y <= 247*Registry.y_scale_factor and
                        Registry.mouse_x >= (Registry.real_window_width-(self.play_width+self.selector_width))-2):

                    if self.hover1 is False:
                        Registry.forced_frame = True
                    self.hover1 = True

                    if Registry.primary_mouse_button_down:
                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        if Registry.show_strobe_effects is None:
                            Registry.show_strobe_effects = messagebox.askquestion(
                                "Check Permission",
                                "".join(("Strobe effects and bright flashes of light can ",
                                            "cause discomfort, (for example lightning), you can choose here ",
                                            "whether to enable or disable those ",
                                            "strobe effects in Pycraft.\n\n",
                                            "Click 'yes' to allow for strobe effects, or 'no' ",
                                            "to turn them off. You can always adjust this in ",
                                            "Pycraft's settings, under 'Storage and permissions'.")))

                            if Registry.show_strobe_effects == "yes":
                                Registry.show_strobe_effects = True

                            else:
                                Registry.show_strobe_effects = False
                                
                        Registry.go_to = "level_selector"
                        #Registry.startup_animation = True
                        Registry.run_timer = 0
                        self.create_image_of_surface = True

                else:
                    self.hover1 = False

                if (Registry.mouse_y >= 252*Registry.y_scale_factor and
                        Registry.mouse_y <= 297*Registry.y_scale_factor and
                        Registry.mouse_x >= (Registry.real_window_width-(self.settings_width+self.selector_width))-2):

                    if self.hover2 is False:
                        Registry.forced_frame = True
                    self.hover2 = True

                    if Registry.primary_mouse_button_down:
                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        Registry.go_to = "settings"
                        Registry.startup_animation = True
                        Registry.run_timer = 0

                else:
                    self.hover2 = False

                if (Registry.mouse_y >= 302*Registry.y_scale_factor and
                        Registry.mouse_y <= 347*Registry.y_scale_factor and
                        Registry.mouse_x >= (Registry.real_window_width-(self.char_designer_width+self.selector_width)-2)):

                    if self.hover3 is False:
                        Registry.forced_frame = True
                    self.hover3 = True

                    if Registry.primary_mouse_button_down:
                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        Registry.go_to = "character_designer"
                        Registry.startup_animation = True
                        Registry.run_timer = 0

                else:
                    self.hover3 = False

                if (Registry.mouse_y >= 402*Registry.y_scale_factor and
                        Registry.mouse_y <= 447*Registry.y_scale_factor and
                        Registry.mouse_x >= (Registry.real_window_width-(self.achievements_width+self.selector_width)-2)):

                    if self.hover4 is False:
                        Registry.forced_frame = True
                    self.hover4 = True

                    if Registry.primary_mouse_button_down:
                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        Registry.go_to = "achievements"
                        Registry.startup_animation = True
                        Registry.run_timer = 0

                else:
                    self.hover4 = False

                if (Registry.mouse_y >= 352*Registry.y_scale_factor and
                        Registry.mouse_y <= 397*Registry.y_scale_factor and
                        Registry.mouse_x >= (Registry.real_window_width-(self.credits_width+self.selector_width)-2)):

                    if self.hover5 is False:
                        Registry.forced_frame = True
                    self.hover5 = True

                    if Registry.primary_mouse_button_down:
                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        Registry.go_to = "credits"
                        Registry.startup_animation = True
                        Registry.run_timer = 0

                else:
                    self.hover5 = False

                if (Registry.mouse_y >= 452*Registry.y_scale_factor and
                        Registry.mouse_y <= 497*Registry.y_scale_factor and
                        Registry.mouse_x >= (Registry.real_window_width-(self.benchmark_width+self.selector_width)-2)):

                    if self.hover6 is False:
                        Registry.forced_frame = True
                    self.hover6 = True

                    if Registry.primary_mouse_button_down:
                        if Registry.sound:
                            sound_utils.play_sound.play_click_sound()

                        Registry.go_to = "benchmark"
                        Registry.startup_animation = True
                        Registry.run_timer = 0

                else:
                    self.hover6 = False
                
                if Registry.linked_to_installer:
                    if (Registry.mouse_y >= 502*Registry.y_scale_factor and
                            Registry.mouse_y <= 547*Registry.y_scale_factor and
                            Registry.mouse_x >= (Registry.real_window_width-(self.installer_width+self.selector_width)-2)):

                        if self.hover7 is False:
                            Registry.forced_frame = True
                        self.hover7 = True

                        if Registry.primary_mouse_button_down:
                            if Registry.sound:
                                sound_utils.play_sound.play_click_sound()

                            Registry.go_to = "Installer"
                            Registry.startup_animation = True
                            Registry.run_timer = 0

                    else:
                        self.hover7 = False
                    
            if self.show_message is None:
                if Registry.installer_new_update:
                    Registry.installer_new_update = False
                    self.show_message = f"Successfully updated Pycraft to v{Registry.version}"
                    self.messageColor = (0, 255, 0)
                    Registry.forced_frame = True

                elif Registry.outdated and Registry.linked_to_installer:
                    Registry.installer_updatable = False
                    self.show_message = "There is an update available!"
                    self.messageColor = (0, 255, 0)
                    Registry.forced_frame = True

                elif not self.prev_joystick_connected == Registry.joystick_connected:
                    self.prev_joystick_connected = Registry.joystick_connected
                    Registry.forced_frame = True
                    Registry.device_connected_update = False
                    if Registry.joystick_connected:
                        self.show_message = "".join(("There is a new input device available! ",
                                            "You can change input modes in settings"))

                        self.messageColor = (0, 255, 0)

                    else:
                        if Registry.use_mouse_input:
                            self.show_message = "Terminated connection to an input device"
                            self.messageColor = (255, 0, 0)

                        else:
                            self.show_message = "".join(("Terminated connection to current ",
                                                "input device, returning to ",
                                                "default setting"))

                            self.messageColor = (255, 0, 0)
                            Registry.use_mouse_input = True
                    
            if self.hover1:
                if Registry.use_mouse_input:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            elif self.hover2:
                if Registry.use_mouse_input:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            elif self.hover3:
                if Registry.use_mouse_input:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            elif self.hover5:
                if Registry.use_mouse_input:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            elif self.hover4:
                if Registry.use_mouse_input:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            elif self.hover6:
                if Registry.use_mouse_input:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
            elif self.hover7 and Registry.linked_to_installer:
                if Registry.use_mouse_input:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
            else:
                if Registry.use_mouse_input:
                    if pygame.mouse.get_cursor() != pygame.SYSTEM_CURSOR_ARROW:
                        pygame.mouse.set_cursor(
                            pygame.SYSTEM_CURSOR_ARROW)
            
            if self.create_image_of_surface:
                if Registry.use_transparency_effects:
                    self.create_image_of_surface = False

                    image_utils.convert_image.surface_to_pil_image(Registry.display)
                        
        
        def render(self) -> None:
            Registry.forced_frame = False
            RenderRect = pygame.Rect(
                0,
                0,
                Registry.real_window_width,
                Registry.real_window_height-40)
            
            Registry.display.fill(Registry.background_color, RenderRect)
            
            if (Registry.fancy_graphics and
                    Registry.aa is False):
                
                Registry.forced_frame = True
                colorsARRAY = []
                if self.anim:
                    self.anim = False
                    self.TargetARRAY = []
                    for a in range(random.randint(0, 32)):
                        self.TargetARRAY.append(a)

                if len(self.TargetARRAY) == 0:
                    self.TargetARRAY = [33]

                for i in range(32):
                    for j in range(len(self.TargetARRAY)):
                        if i == self.TargetARRAY[j]:
                            colorsARRAY.append(self.special)

                        else:
                            colorsARRAY.append(Registry.shape_color)

                if self.increment is False:
                    RandomInt = random.randint(0, 10)
                    if Registry.average_fps == 0:
                        self.ColourDisplacement -= RandomInt/(Registry.fps/4)
                    else:
                        self.ColourDisplacement -= RandomInt/(Registry.average_fps/4)

                    self.special[0] = self.ColourDisplacement
                    self.special[1] = self.ColourDisplacement
                    self.special[2] = self.ColourDisplacement

                if self.increment:
                    RandomInt = random.randint(0, 10)
                    if Registry.average_fps == 0:
                        self.ColourDisplacement += RandomInt/(Registry.fps/4)

                    else:
                        self.ColourDisplacement += RandomInt/(Registry.average_fps/4)

                    self.special[0] = self.ColourDisplacement
                    self.special[1] = self.ColourDisplacement
                    self.special[2] = self.ColourDisplacement

                if self.special[0] <= 30:
                    self.increment = True
                    self.special[0] = 30
                    self.special[1] = 30
                    self.special[2] = 30

                if self.special[0] >= 80:
                    self.increment = False
                    self.anim = True
                    self.special[0] = 80
                    self.special[1] = 80
                    self.special[2] = 80
            else:
                colorsARRAY = False
                
            text_utils.text_formatter.format_text(
                "Pycraft",
                ("center", "top"),
                Registry.title_font,
                Registry.title_backup_font)

            returned_text = text_utils.text_formatter.format_text(
                "Play",
                ("right", 200*Registry.y_scale_factor),
                Registry.option_font,
                Registry.option_backup_font,
                underline=self.hover1)

            self.play_width = returned_text.get_width()

            returned_text = text_utils.text_formatter.format_text(
                "Settings",
                ("right", 250*Registry.y_scale_factor),
                Registry.option_font,
                Registry.option_backup_font,
                underline=self.hover2)

            self.settings_width = returned_text.get_width()

            returned_text = text_utils.text_formatter.format_text(
                "Character Designer",
                ("right", 300*Registry.y_scale_factor),
                Registry.option_font,
                Registry.option_backup_font,
                underline=self.hover3)

            self.char_designer_width = returned_text.get_width()

            returned_text = text_utils.text_formatter.format_text(
                "Credits",
                ("right", 350*Registry.y_scale_factor),
                Registry.option_font,
                Registry.option_backup_font,
                underline=self.hover5)

            self.credits_width = returned_text.get_width()

            returned_text = text_utils.text_formatter.format_text(
                "Achievements",
                ("right", 400*Registry.y_scale_factor),
                Registry.option_font,
                Registry.option_backup_font,
                underline=self.hover4)

            self.achievements_width = returned_text.get_width()

            returned_text = text_utils.text_formatter.format_text(
                "Benchmark",
                ("right", 450*Registry.y_scale_factor),
                Registry.option_font,
                Registry.option_backup_font,
                underline=self.hover6)

            self.benchmark_width = returned_text.get_width()
            
            if Registry.linked_to_installer:
                returned_text = text_utils.text_formatter.format_text(
                    "Installer",
                    ("right", 500*Registry.y_scale_factor),
                    Registry.option_font,
                    Registry.option_backup_font,
                    underline=self.hover7)

                self.installer_width = returned_text.get_width()

            if self.hover1:
                Registry.display.blit(
                    self.selector,
                    (Registry.real_window_width-(self.play_width+self.selector_width)-2,
                        200*Registry.y_scale_factor))

            elif self.hover2:
                Registry.display.blit(
                    self.selector,
                    (Registry.real_window_width-(self.settings_width+self.selector_width)-2,
                        250*Registry.y_scale_factor))

            elif self.hover3:
                Registry.display.blit(
                    self.selector,
                    (Registry.real_window_width-(self.char_designer_width+self.selector_width)-2,
                        300*Registry.y_scale_factor))

            elif self.hover5:
                Registry.display.blit(
                    self.selector,
                    (Registry.real_window_width-(self.credits_width+self.selector_width)-2,
                        350*Registry.y_scale_factor))

            elif self.hover4:
                Registry.display.blit(
                    self.selector,
                    (Registry.real_window_width-(self.achievements_width+self.selector_width)-2,
                        400*Registry.y_scale_factor))

            elif self.hover6:
                Registry.display.blit(
                    self.selector,
                    (Registry.real_window_width-(self.benchmark_width+self.selector_width)-2,
                        450*Registry.y_scale_factor))
            
            elif self.hover7 and Registry.linked_to_installer:
                Registry.display.blit(
                    self.selector,
                    (Registry.real_window_width-(self.installer_width+self.selector_width)-2,
                        500*Registry.y_scale_factor))
                    
            drawing_utils.generate_graph().draw_developer_graph()

            drawing_utils.draw_rose.create_rose(
                colorsARRAY,
                51,
                142,
                524*Registry.x_scale_factor,
                524*Registry.y_scale_factor)

            if Registry.go_to is None:
                display_utils.display_animations.fade_in(
                    size="limited")
                    
            else:
                display_utils.display_animations.fade_out(
                    size="limited")

            pygame.display.update(RenderRect)
        
        def render_banner(self):
            RenderRect = pygame.Rect(
                0,
                Registry.real_window_height-40,
                Registry.real_window_width,
                Registry.real_window_height)

            Registry.display.fill(
                Registry.background_color,
                RenderRect)
            
            if (self.show_message is not None and
                    self.messageColor is not None and
                    self.banner_RenderedText is False):
                
                self.banner_timer_start = time.perf_counter()
                self.banner_RenderedText = True
                
            if self.banner_RenderedText:
                if time.perf_counter()-self.banner_timer_start < 3:
                    text_utils.text_formatter.format_text(
                        self.show_message,
                        ("center", "bottom"),
                        Registry.large_content_font,
                        Registry.large_content_backup_font,
                        font_color=self.messageColor)

            else:
                if Registry.use_mouse_input is False:
                    messageText = "".join(("On the controller; use the D-pad to navigate the menu, ",
                                    "press 'B' to confirm or press 'Y' to exit"))

                    text_utils.text_formatter.format_text(
                        messageText,
                        ("center", "bottom"),
                        Registry.large_content_font,
                        Registry.large_content_backup_font)

            text_utils.text_formatter.format_text(
                "By PycraftDev",
                ("left", "bottom"),
                Registry.large_content_font,
                Registry.large_content_backup_font)

            text_utils.text_formatter.format_text(
                f"Version: {Registry.version}",
                ("right", "bottom"),
                Registry.large_content_font,
                Registry.large_content_backup_font)

            pygame.display.update(RenderRect)
                    
        def create_banner(self):
            try:
                while Registry.command == "Undefined":
                    if self.banner_RenderedText:
                        if time.perf_counter()-self.banner_timer_start > 3:
                            Registry.forced_frame = True
                            self.show_message = None
                            self.messageColor = None
                            self.banner_RenderedText = False
                            
                    if Registry.forced_frame:
                        generate_home.render_banner(self)

                    target_fps = display_utils.display_utils.get_play_status()

                    Registry.clock.tick(target_fps/2)
                    
            except Exception as message:
                if str(message) != "display Surface quit":
                    Registry.error_message = "".join(("homeScreen > generate_home > ",
                                                 f"create_banner (thread): {str(message)}"))

                    Registry.error_message_detailed = "".join(
                        traceback.format_exception(
                            None,
                            message,
                            message.__traceback__))

        def home_gui(self):
            try:
                BannerThread = threading.Thread(
                    target=generate_home.create_banner,
                    args=(self,))
                BannerThread.name = "[thread]: create_banner"
                BannerThread.daemon = True
                BannerThread.start()

                caption_utils.generate_captions.set_caption(
                    "Home")

                pygame.display.flip()

                Registry.currently_displaying_message = False

                Registry.mouse_x = Registry.real_window_width/2
                Registry.mouse_y = Registry.real_window_height/2
                while True:
                    start_time = time.perf_counter()
                    
                    if not (Registry.error_message is None or Registry.error_message_detailed is None):
                        error_utils.generate_error_screen.error_screen(
                            Registry.error_message,
                            Registry.error_message_detailed)
                    
                    generate_home.compute(self)
                    
                    if Registry.forced_frame:
                        generate_home.render(self)

                    if (Registry.startup_animation is False and
                            (Registry.go_to is not None)):
                        
                        return Registry.go_to
                        
                    target_fps = display_utils.display_utils.get_play_status()

                    Registry.clock.tick(target_fps/2)
                    Registry.run_timer += time.perf_counter()-start_time

                    if Registry.error_message is not None:
                        Registry.error_message = "homeScreen: "+str(Registry.error_message)
                        return

            except Exception as message:
                error_message = "homeScreen > generate_home > home_gui: "+ str(message)
                
                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        message,
                        message.__traceback__))

                error_utils.generate_error_screen.error_screen(
                    error_message,
                    error_message_detailed)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
