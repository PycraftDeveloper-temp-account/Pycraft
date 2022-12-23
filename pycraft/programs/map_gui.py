if __name__ != "__main__":
    try:
        import sys
        import os
        import traceback
        
        import pygame
        from PIL import Image
        import pyautogui

        import sound_utils
        import display_utils
        import caption_utils
        import error_utils
        import file_utils
        import tkinter_utils
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

    class generate_map_gui:
        """
        This class is in charge of setting up, managing, loading and running the
        map GUI. This GUI gets loaded as a separate process at the start
        of the game engine and runs only when the game engine sends a command.
        This is run in parallel (process).
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(
                self,
                dictionary):
            """
            This class is in charge of turning the dictionary the user enters as
            a parameter (that contains all the data required to properly display
            the map GUI) into a 'generate_map_gui' object in a similar
            style to the 'pycraft_main' program. This also initializes the
            map's required modules.
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                - dictionary (dict): This parameter holds all the data that is stored 
                    as 'self' in the game engine. This includes the configuration and
                    user defined settings. Note that the input to this variable must
                    be sorted first to remove any modules or module specific objects.
                    For example a (Pygame Surface) type object as that will cause errors
                    when creating the new process.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            for key in dictionary:
                setattr(self,key,dictionary[key])

            pygame.init()

        def get_map_pos(in_x, in_z):
            """
            This maths based subroutine is used to calculate the position the map
            should be rendered onscreen.
            
            - Args:
                - in_x (float): This parameter represents the user's position in game
                    on the X axis.
                - in_z (float): This parameter represents the user's position in game
                    on the Z axis.
                    
            - Keyword Args:
                - None

            - Output:
                - x (int): The X coordinate to render the map.
                - z (int): The Y coordinate to render the map. (In 2D space there is
                    no 'Z' or depth axis, therefore because we don't care about the
                    user's height position here, we use their Z position in 3D space to
                    represent their Y coordinate in 2D space.)
            """
            x = 0
            z = 0
            if in_x == 0:
                x = 640
            if in_z == 0:
                z = 360
            x -= 6
            z -= 19
            return (x,z)

        def map_gui(
                dictionary,
                start_map):
            """
            This subroutine is in charge of loading and running the map GUI. This
            GUI gets loaded as a separate process at the start of the game engine
            and runs only when the game engine sends a command. This is run in
            parallel (process).
            
            - Args:
                - dictionary (dict): This parameter holds all the data that is stored 
                    as 'self' in the game engine. This includes the configuration and
                    user defined settings. Note that the input to this variable must
                    be sorted first to remove any modules or module specific objects.
                    For example a (Pygame Surface) type object as that will cause errors
                    when creating the new process.
                - start_inventory (Multiprocessing Event object): This parameter is an
                    event object used to tell the inventory when the game engine wants
                    to have the inventory displayed. When this event is not set the
                    map will wait.
                    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            self = generate_map_gui(dictionary)
            try:
                self.input_key = file_utils.pycraft_config_utils.read_input_key(
                    self.platform,
                    self.base_folder)
                
                if self.platform == "Linux":
                    self.title_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")),60)

                    self.window_icon = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            ("resources//general resources//Icon.png")))

                else:
                    self.window_icon = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            ("resources\\general resources\\Icon.png")))

                    self.title_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")),60)

                self.clock = pygame.time.Clock()

                if self.platform == "Linux":
                    title_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts//Book Antiqua.ttf")),60)

                else:
                    title_font = pygame.font.Font(
                        os.path.join(
                            self.base_folder,
                            ("fonts\\Book Antiqua.ttf")),60)
                    
                if self.platform == "Linux":
                    MapPIL =  Image.open(
                        os.path.join(
                            self.base_folder,
                            ("resources//map resources//Full_Map.png")))

                else:
                    MapPIL =  Image.open(
                        os.path.join(
                            self.base_folder,
                            ("resources\\map resources\\Full_Map.png")))

                Map0 = pygame.image.fromstring(
                    MapPIL.tobytes(),
                    MapPIL.size,
                    MapPIL.mode)

                if self.platform == "Linux":
                    MapIcon = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            ("resources//map resources//Marker.png")))

                else:
                    MapIcon = pygame.image.load(
                        os.path.join(
                            self.base_folder,
                            ("resources\\map resources\\Marker.png")))

                zoom = 0

                X,Y = 0,0
                key = ""

                if self.platform == "Linux":
                    MapPIL0 =  Image.open(
                        os.path.join(
                            self.base_folder,
                            ("resources//map resources//Full_Map.png"))).resize(
                                (self.real_window_width,
                                 self.real_window_height),
                                Image.ANTIALIAS)

                else:
                    MapPIL0 =  Image.open(
                        os.path.join(
                            self.base_folder,
                            ("resources\\map resources\\Full_Map.png"))).resize(
                                (self.real_window_width,
                                 self.real_window_height),
                                Image.ANTIALIAS)

                Map0 = pygame.image.fromstring(
                    MapPIL0.tobytes(),
                    MapPIL0.size,
                    MapPIL0.mode)

                if self.platform == "Linux":
                    MapPIL1 =  Image.open(
                        os.path.join(
                            self.base_folder,
                            ("resources//map resources//Full_Map.png"))).resize(
                                (int(self.real_window_width*1.75),
                                 int(self.real_window_height*1.75)),
                                Image.ANTIALIAS)

                else:
                    MapPIL1 =  Image.open(
                        os.path.join(
                            self.base_folder,
                            ("resources\\map resources\\Full_Map.png"))).resize(
                                (int(self.real_window_width*1.75),
                                 int(self.real_window_height*1.75)),
                                Image.ANTIALIAS)

                Map1 = pygame.image.fromstring(
                    MapPIL1.tobytes(),
                    MapPIL1.size,
                    MapPIL1.mode)

                if self.platform == "Linux":
                    MapPIL2 =  Image.open(
                        os.path.join(
                            self.base_folder,
                            ("resources//map resources//Full_Map.png"))).resize(
                                (int(self.real_window_width*2),
                                 int(self.real_window_height*2)),
                                Image.ANTIALIAS)

                else:
                    MapPIL2 =  Image.open(
                        os.path.join(
                            self.base_folder,
                            ("resources\\map resources\\Full_Map.png"))).resize(
                                (int(self.real_window_width*2),
                                 int(self.real_window_height*2)),
                                Image.ANTIALIAS)

                Map2 = pygame.image.fromstring(
                    MapPIL2.tobytes(),
                    MapPIL2.size,
                    MapPIL2.mode)

                while True:
                    start_map.wait()
                    
                    pygame.display.init()
                    self.data_average_fps = []
                    self.data_CPU_usage = []
                    self.data_current_fps = []
                    self.data_memory_usage = []

                    self.timer = 0

                    self.data_average_fps_Max = 1
                    self.data_CPU_usage_Max = 1
                    self.data_current_fps_Max = 1
                    self.data_memory_usage_Max = 1

                    fullscreen_x = pyautogui.size()[0]
                    fullscreen_y = pyautogui.size()[1]

                    (self.display,
                        self.saved_window_width,
                        self.saved_window_height) = display_utils.display_utils.set_display(
                            self.fullscreen,
                            self.vsync,
                            self.saved_window_width,
                            self.saved_window_height,
                            self.window_icon,
                            self.logging_dictionary,
                            self.output_log,
                            self.platform,
                            self.base_folder,
                            fullscreen_x,
                            fullscreen_y)

                    Map0.convert()
                    Map1.convert()
                    Map2.convert()
                    MapIcon.convert_alpha()
                    while True:
                        caption_utils.generate_captions.get_normal_caption(
                            "Map",
                            self.detailed_captions,
                            self.play_time,
                            self.x,
                            self.y,
                            self.z,
                            self.total_move_x,
                            self.total_move_y,
                            self.total_move_z,
                            self.fps_overclock,
                            self.current_fps,
                            self.iteration,
                            self.version,
                            self.current_memory_usage,
                            self.theme,
                            self.fps,
                            self.average_fps)

                        self.display.fill(self.background_color)

                        (_,
                            self.display,
                            self.mouse_button_down,
                            self.go_to,
                            self.startup_animation,
                            self.run_timer,
                            self.current_fps,
                            self.average_fps,
                            self.iteration,
                            self.saved_window_width,
                            self.saved_window_height,
                            self.window_in_focus,
                            self.joystick_exit,
                            self.x_scale_factor,
                            self.y_scale_factor,
                            self.real_window_width,
                            self.real_window_height,
                            self.mouse_x,
                            self.mouse_y,
                            self.data_average_fps,
                            self.data_CPU_usage,
                            self.data_current_fps,
                            self.data_memory_usage,
                            self.timer,
                            self.data_average_fps_Max,
                            self.data_CPU_usage_Max,
                            self.data_current_fps_Max,
                            self.data_memory_usage_Max,
                            self.joystick_zoom,
                            self.clock,
                            self.joystick_hat_pressed,
                            self.fullscreen,
                            self.joystick_connected) = display_utils.display_functionality.core_display_functions(
                                self.platform,
                                self.base_folder,
                                self.display,
                                self.use_mouse_input,
                                self.average_fps,
                                self.iteration,
                                self.mouse_x,
                                self.mouse_y,
                                self.x_scale_factor,
                                self.y_scale_factor,
                                self.go_to,
                                self.joystick_exit,
                                self.joystick_hat_pressed,
                                self.window_in_focus,
                                self.saved_window_width,
                                self.saved_window_height,
                                self.clock,
                                self.sound,
                                self.input_key,
                                self.input_configuration,
                                self.extended_developer_options,
                                self.logging_dictionary,
                                self.output_log,
                                self.vsync,
                                self.window_icon,
                                self.sound_volume,
                                self,
                                self.version,
                                self.background_color,
                                self.font_color,
                                self.fullscreen,
                                self.startup_animation,
                                self.run_timer,
                                self.data_average_fps,
                                self.data_CPU_usage,
                                self.data_current_fps,
                                self.data_memory_usage,
                                self.timer,
                                self.data_average_fps_Max,
                                self.data_CPU_usage_Max,
                                self.data_current_fps_Max,
                                self.data_memory_usage_Max,
                                self.joystick_zoom,
                                self.mouse_button_down,
                                self.error_message,
                                self.error_message_detailed,
                                checkEvents=False)

                        for event in pygame.event.get():
                            if (event.type == pygame.QUIT or
                                    (event.type == pygame.KEYDOWN and
                                        event.key == self.input_key[
                                            self.input_configuration["keyboard"]["Back"]][0])):

                                start_map.clear()

                            if start_map.is_set():
                                if event.type == pygame.WINDOWSIZECHANGED:
                                    if self.platform == "Linux":
                                        MapPIL0 =  Image.open(
                                            os.path.join(
                                                self.base_folder,
                                                ("resources//map resources//Full_Map.png"))).resize(
                                                    (self.real_window_width,
                                                    self.real_window_height),
                                                    Image.ANTIALIAS)

                                    else:
                                        MapPIL0 =  Image.open(
                                            os.path.join(
                                                self.base_folder,
                                                ("resources\\map resources\\Full_Map.png"))).resize(
                                                    (self.real_window_width,
                                                    self.real_window_height),
                                                    Image.ANTIALIAS)

                                    Map0 = pygame.image.fromstring(
                                        MapPIL0.tobytes(),
                                        MapPIL0.size,
                                        MapPIL0.mode).convert()

                                    if self.platform == "Linux":
                                        MapPIL1 =  Image.open(
                                            os.path.join(
                                                self.base_folder,
                                                ("resources//map resources//Full_Map.png"))).resize(
                                                    (int(self.real_window_width*1.75),
                                                    int(self.real_window_height*1.75)),
                                                    Image.ANTIALIAS)

                                    else:
                                        MapPIL1 =  Image.open(
                                            os.path.join(
                                                self.base_folder,
                                                ("resources\\map resources\\Full_Map.png"))).resize(
                                                    (int(self.real_window_width*1.75),
                                                    int(self.real_window_height*1.75)),
                                                    Image.ANTIALIAS)

                                    Map1 = pygame.image.fromstring(
                                        MapPIL1.tobytes(),
                                        MapPIL1.size,
                                        MapPIL1.mode).convert()

                                    if self.platform == "Linux":
                                        MapPIL2 =  Image.open(
                                            os.path.join(
                                                self.base_folder,
                                                ("resources//map resources//Full_Map.png"))).resize(
                                                    (int(self.real_window_width*2),
                                                    int(self.real_window_height*2)),
                                                    Image.ANTIALIAS)

                                    else:
                                        MapPIL2 =  Image.open(
                                            os.path.join(
                                                self.base_folder,
                                                ("resources\\map resources\\Full_Map.png"))).resize(
                                                    (int(self.real_window_width*2),
                                                    int(self.real_window_height*2)),
                                                    Image.ANTIALIAS)

                                    Map2 = pygame.image.fromstring(
                                        MapPIL2.tobytes(),
                                        MapPIL2.size,
                                        MapPIL2.mode).convert()

                                if event.type == pygame.KEYDOWN:
                                    if (event.key == self.input_key[
                                                self.input_configuration["keyboard"]["List variables"]][0] and
                                            self.extended_developer_options):

                                        tkinter_utils.tkinter_info.create_tkinter_window(
                                            self,
                                            self.version,
                                            self.background_color,
                                            self.font_color)
                                
                                    if event.key == self.input_key[
                                            self.input_configuration["keyboard"]["Jump"]][0]:
                                        
                                        zoom = 0

                                    if event.key == self.input_key[
                                            self.input_configuration["keyboard"]["Walk forwards"]][0]:
                                        
                                        key = "w"

                                    if event.key == self.input_key[
                                            self.input_configuration["keyboard"]["Walk backwards"]][0]:
                                        
                                        key = "s"

                                    if event.key == self.input_key[
                                            self.input_configuration["keyboard"]["Walk right"]][0]:
                                        
                                        key = "d"

                                    if event.key == self.input_key[
                                            self.input_configuration["keyboard"]["Walk left"]][0]:
                                        
                                        key = "a"

                                    if event.key == self.input_key[
                                            self.input_configuration["keyboard"]["Toggle full-screen"]][0]:
                                        
                                        self.data_average_fps = []
                                        self.data_CPU_usage = []
                                        self.data_current_fps = []
                                        self.data_memory_usage = []

                                        self.timer = 0

                                        self.data_average_fps_Max = 1
                                        self.data_CPU_usage_Max = 1
                                        self.data_current_fps_Max = 1
                                        self.data_memory_usage_Max = 1

                                        fullscreen_x = pyautogui.size()[0]
                                        fullscreen_y = pyautogui.size()[1]
                                        
                                        (self.display,
                                            self.saved_window_width,
                                            self.saved_window_height,
                                            self.fullscreen) = display_utils.display_utils.update_display(
                                                self.window_icon,
                                                self.fullscreen,
                                                self.vsync,
                                                self.saved_window_width,
                                                self.saved_window_height,
                                                self.logging_dictionary,
                                                self.output_log,
                                                self.platform,
                                                self.base_folder,
                                                fullscreen_x,
                                                fullscreen_y)

                                if event.type == pygame.KEYUP:
                                    key = ""

                                if event.type == pygame.MOUSEWHEEL:
                                    if str(event.y)[0] == "-":
                                        zoom -= 1
                                    else:
                                        zoom += 1

                        if not start_map.is_set():
                            break
                            
                        if self.use_mouse_input is False:
                            if self.joystick_zoom == "-":
                                zoom -= 1
                                self.joystick_zoom = None

                            elif self.joystick_zoom == "+":
                                zoom += 1
                                self.joystick_zoom = None

                            joystick_mouse = pygame.mouse.get_rel()

                            if joystick_mouse[0] > 0:
                                key = "a"

                            elif joystick_mouse[0] < 0:
                                key = "d"

                            elif joystick_mouse[1] > 0:
                                key = "w"

                            elif joystick_mouse[1] < 0:
                                key = "s"

                            else:
                                key = ""

                            if self.joystick_exit:
                                self.joystick_exit = False

                                if self.sound:
                                    sound_utils.play_sound.play_click_sound(
                                        self.platform,
                                        self.base_folder,
                                        self.sound_volume)
                                break

                        if zoom >= 2:
                            zoom = 2
                        if zoom <= 0:
                            zoom = 0

                        if key == "w":
                            if zoom == 1:
                                Y -= 5
                            elif zoom == 2:
                                Y -= 10
                        if key == "s":
                            if zoom == 1:
                                Y += 5
                            elif zoom == 2:
                                Y += 10
                        if key == "d":
                            if zoom == 1:
                                X += 5
                            elif zoom == 2:
                                X += 10
                        if key == "a":
                            if zoom == 1:
                                X -= 5
                            elif zoom == 2:
                                X -= 10

                        if zoom == 1:
                            self.display.blit(
                                Map1,
                                (X,Y))

                            self.display.blit(
                                MapIcon,
                                generate_map_gui.get_map_pos(self.x, self.z))

                            if X <= -955:
                                X = -955
                            if Y <= -535:
                                Y = -535
                            if X >= -5:
                                X = -5
                            if Y >= -5:
                                Y = -5
                        elif zoom == 2:
                            self.display.blit(
                                Map2,
                                (X,Y))

                            self.display.blit(
                                MapIcon,
                                generate_map_gui.get_map_pos(self.x, self.z))

                            if X <= -1590:
                                X = -1590
                            if Y <= -890:
                                Y = -890
                            if X >= -10:
                                X = -10
                            if Y >= -10:
                                Y = -10
                        else:
                            self.display.blit(
                                Map0,
                                (0,0))

                            self.display.blit(
                                MapIcon,
                                generate_map_gui.get_map_pos(self.x, self.z))

                        pygame.display.flip()
                        (tempfps,
                            self.project_sleeping) = display_utils.display_utils.get_play_status(
                                self.platform,
                                self.vsync,
                                self.vsync_fps,
                                self.fps,
                                self.project_sleeping,
                                self.command,
                                self.music,
                                self.fps_overclock,
                                self.base_folder,
                                self.music_volume)
                            
                        self.clock.tick(tempfps)

                    pygame.display.quit()
            except Exception as Message:
                error_message = "map_gui > generate_map_gui > map_gui: "+str(Message)

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                error_utils.generate_error_screen.error_screen(
                    self.logging_dictionary,
                    self.output_log,
                    self.detailed_error_messages,
                    error_message,
                    error_message_detailed,
                    self.platform,
                    self.base_folder)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Fail",
        "You need to run this as part of Pycraft,please run the 'main.py' file")
    quit()
