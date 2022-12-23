if __name__ != "__main__":
    try:
        import sys
        import ctypes
        
        import pygame
        import pyautogui

        import sound_utils
        import logging_utils
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
            
    class display_functionality:
        """
        This class is in charge of handling calls to subroutines, as well as enabling
        basic GUI functionality to Pycraft, this is called by many GUIs and is heavily
        customisable. This is designed to simplify GUI design and make it easier to roll
        out some changes to every GUI in Pycraft.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        def __init__(self):
            pass

        def core_display_functions(
                platform,
                base_folder,
                display,
                use_mouse_input,
                average_fps,
                iteration,
                mouse_x,
                mouse_y,
                x_scale_factor,
                y_scale_factor,
                go_to,
                joystick_exit,
                joystick_hat_pressed,
                window_in_focus,
                saved_window_width,
                saved_window_height,
                clock,
                sound,
                input_key,
                input_configuration,
                extended_developer_options,
                logging_dictionary,
                output_log,
                vsync,
                window_icon,
                sound_volume,
                variable_data,
                version,
                background_color,
                font_color,
                fullscreen,
                startup_animation,
                run_timer,
                data_average_fps,
                data_CPU_usage,
                data_current_fps,
                data_memory_usage,
                timer,
                data_average_fps_Max,
                data_CPU_usage_Max,
                data_current_fps_Max,
                data_memory_usage_Max,
                joystick_zoom,
                mouse_button_down,
                error_message,
                error_message_detailed,
                location="home",
                checkEvents=True,
                resize=True,
                return_events=False,
                disable_events=False):
            """
            This subroutine is in charge of the basic functionality you would expect from
            Pycraft's GUIs, it handles events, mouse and controller positions, as well as
            allowing for great customisability, meaning its designed to be called by most
            GUI's and be flexible enough to be functional.
            
            - Args:
                - platform (str): This string tells the subroutine which operating
                    system we are using. This is needed for OS specific operations.
                - base_folder (str): This string is a file path to the resources
                    for Pycraft on your device.
                - display (Pygame Surface): The display object is used throughout Pycraft. This is the identifier
                    we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing
                    engine used in Pycraft.
                - use_mouse_input (bool): 
                - average_fps (float): 
                - iteration (int): 
                - mouse_x (int): 
                - mouse_y (int): 
                - x_scale_factor (float): 
                - y_scale_factor (float): 
                - go_to (str): 
                - joystick_exit (bool): 
                - joystick_hat_pressed (bool): 
                - window_in_focus (bool): 
                - saved_window_width (int): 
                - saved_window_height (int): 
                - clock (Pygame Clock): 
                - sound (bool): 
                - input_key (dict): 
                - input_configuration (dict): 
                - extended_developer_options (bool): 
                - logging_dictionary (dict): This dictionary is used to tell this
                    subroutine if information messages are to be logged, this can be
                    adjusted in settings.
                - output_log (bool): This option tells the subroutine if logged
                    messages should also be outputted to the console.
                - vsync (bool): 
                - window_icon (Pygame Surface): This is the icon we use in the caption (and
                    in the taskbar on some supported OS') for Pycraft.
                - sound_volume (float): 
                - variable_data (dict): 
                - version (str) - Pycraft's current version.
                - background_color (tuple): 
                - font_color (tuple): 
                - fullscreen (bool): 
                - startup_animation (bool): 
                - run_timer (float): 
                - data_average_fps (arr): 
                - data_CPU_usage (arr): 
                - data_current_fps (arr): 
                - data_memory_usage (arr): 
                - timer (float): 
                - data_average_fps_Max (float): 
                - data_CPU_usage_Max (float): 
                - data_current_fps_Max (float): 
                - data_memory_usage_Max (float): 
                - joystick_zoom (str): 
                - mouse_button_down (bool): 
                - error_message (str): 
                - error_message_detailed (str): 
                    
            - Keyword Args:
                - location="home" (str): 
                - checkEvents=True (bool): 
                - resize=True (bool): 
                - return_events=False (bool): 
                - disable_events=False (bool): 

            - Output:
                - displayEvents (arr): 
                - display (Pygame Surface): The display object is used throughout Pycraft. This is the identifier
                       we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing
                       engine used in Pycraft.
                - mouse_button_down (bool): 
                - go_to (str): 
                - startup_animation (bool): 
                - run_timer (float): 
                - current_fps (float): 
                - average_fps (float): 
                - iteration (int): 
                - saved_window_width (int): 
                - saved_window_height (int): 
                - window_in_focus (bool): 
                - joystick_exit (bool): 
                - x_scale_factor (float): 
                - y_scale_factor (float): 
                - real_window_width (int): 
                - real_window_height (int): 
                - mouse_x (int): 
                - mouse_y (int): 
                - data_average_fps (arr):
                - data_CPU_usage (arr):
                - data_current_fps (arr):
                - data_memory_usage (arr):
                - timer (float): 
                - data_average_fps_Max (float): 
                - data_CPU_usage_Max (float): 
                - data_current_fps_Max (float): 
                - data_memory_usage_Max (float): 
                - joystick_zoom (str): 
                - clock (Pygame Clock): 
                - joystick_hat_pressed (bool): 
                - fullscreen (bool): 
                - joystick_connected (bool):
            """
            if not (error_message_detailed is None):
                raise Exception(error_message_detailed)

            if not (error_message is None):
                raise Exception(error_message)

            pygame.joystick.init()
            joystick_count = pygame.joystick.get_count()
            if joystick_count > 0:
                joystick_connected = True
            else:
                joystick_connected = False
            
            if use_mouse_input is False:
                for i in range(joystick_count):
                    joystick = pygame.joystick.Joystick(i)
                    axes = joystick.get_numaxes()
                    
                    for j in range(axes):
                        multiplier = ((60 * 4) / (average_fps / iteration))
                        axis = round(joystick.get_axis(j), 6) * multiplier

                        if j == 0:
                            mouse_x += axis * x_scale_factor
                        if j == 1:
                            mouse_y += axis * y_scale_factor

                    buttons = joystick.get_numbuttons()

                    for j in range(buttons):
                        button = joystick.get_button(j)

                        if j == 1:
                            if (button == 1 and
                                    go_to is None):
                                mouse_button_down = True
                            
                            else:
                                mouse_button_down = False

                        if j == 0:
                            if (button == 1 and go_to is None):
                                joystick_exit = True

                            else:
                                joystick_exit = False

                    hats = joystick.get_numhats()
                    
                    for j in range(hats):
                        hat = joystick.get_hat(j)
                        for k in range(len(hat)):
                            if int(hat[k]) == 1:
                                if joystick_hat_pressed is False:
                                    joystick_hat_pressed = True

                            if k == 0:
                                if int(hat[k]) == 1:
                                    joystick_zoom = "+"
                                if int(hat[k]) == -1:
                                    joystick_zoom = "-"

                if window_in_focus:
                    pygame.mouse.set_pos(
                        mouse_x,
                        mouse_y)
            else:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]

            real_window_width = pygame.display.get_window_size()[0]
            real_window_height = pygame.display.get_window_size()[1]

            if saved_window_width < 1280:
                display = display_utils.generate_min_display(
                    vsync, window_icon, 
                    1280,
                    saved_window_height)

            if saved_window_height < 720:
                display = display_utils.generate_min_display(
                    vsync, window_icon,
                    saved_window_width,
                    720)

            fullscreen_x = pyautogui.size()[0]
            fullscreen_y = pyautogui.size()[1]

            if saved_window_width == fullscreen_x:
                saved_window_width = 1280

            if saved_window_height == fullscreen_y:
                saved_window_height = 720

            if not (real_window_width == fullscreen_x or
                    real_window_height == fullscreen_y):
                
                saved_window_width = pygame.display.get_window_size()[0]
                saved_window_height = pygame.display.get_window_size()[1]

            if iteration > 1000:
                average_fps = (average_fps/iteration)
                iteration = 1
                
            current_fps = clock.get_fps()
            average_fps += current_fps
            iteration += 1

            y_scale_factor = real_window_height/720
            x_scale_factor = real_window_width/1280

            if use_mouse_input is False:
                if joystick_exit:
                    joystick_exit = False
                    if sound:
                        sound_utils.play_sound.play_click_sound(
                            platform,
                            base_folder,
                            sound_volume)

                    if location == "exit":
                        pygame.quit()
                        sys.exit()

                    else:
                        startup_animation = True
                        run_timer = 0
                        go_to = location

            if checkEvents:
                try:
                    displayEvents = pygame.event.get()
                    
                except Exception as Message:
                    joystick_fix = "<built-in function get> returned a result with an exception set"
                    if str(Message) == joystick_fix:
                        displayEvents = []
                    else:
                        logging_utils.create_log_message.update_log_warning(
                            logging_dictionary,
                            Message,
                            output_log,
                            platform,
                            base_folder)
                        
                for event in displayEvents:
                    if (((event.type == pygame.QUIT
                            or (event.type == pygame.KEYDOWN
                                    and event.key == input_key[input_configuration["keyboard"]["Back"]][0])) and
                            go_to is None and
                            disable_events is False)):

                        joystick_exit = False

                        if sound:
                            sound_utils.play_sound.play_click_sound(
                                platform,
                                base_folder,
                                sound_volume)

                        if location == "exit":
                            pygame.quit()
                            sys.exit()
                            
                        else:
                            startup_animation = True
                            run_timer = 0
                            go_to = location

                    if event.type == pygame.WINDOWFOCUSLOST:
                        window_in_focus = False
                    elif event.type == pygame.WINDOWFOCUSGAINED:
                        window_in_focus = True

                    if use_mouse_input:
                        if (((event.type == pygame.MOUSEBUTTONDOWN or
                                    pygame.mouse.get_pressed()[0]) and
                                (not event.type == pygame.MOUSEMOTION)) and
                                go_to is None and
                                    (not mouse_button_down)):

                            mouse_button_down = True

                        else:
                            mouse_button_down = False
                            
                        if (event.type == pygame.KEYDOWN and
                                disable_events is False):
                            
                            if (event.key == input_key[input_configuration["keyboard"]["List variables"]][0] and
                                    extended_developer_options):

                                tkinter_utils.tkinter_info.create_tkinter_window(
                                    variable_data,
                                    version,
                                    background_color,
                                    font_color)
                                
                            if (event.key == input_key[input_configuration["keyboard"]["Toggle full-screen"]][0] and
                                    resize):

                                data_average_fps = []
                                data_CPU_usage = []
                                data_current_fps = []
                                data_memory_usage = []

                                timer = 0

                                data_average_fps_Max = 1
                                data_CPU_usage_Max = 1
                                data_current_fps_Max = 1
                                data_memory_usage_Max = 1

                                fullscreen_x = pyautogui.size()[0]
                                fullscreen_y = pyautogui.size()[1]
                                
                                (display,
                                    saved_window_width,
                                    saved_window_height,
                                    fullscreen) = display_utils.update_display(
                                        window_icon,
                                        fullscreen,
                                        vsync,
                                        saved_window_width,
                                        saved_window_height,
                                        logging_dictionary,
                                        output_log,
                                        platform,
                                        base_folder,
                                        fullscreen_x,
                                        fullscreen_y,)

                            if event.key == input_key[input_configuration["keyboard"]["Confirm"]][0]:
                                mouse_button_down = True

                if return_events:
                    return (displayEvents,
                        display,
                        mouse_button_down,
                        go_to,
                        startup_animation,
                        run_timer,
                        current_fps,
                        average_fps,
                        iteration,
                        saved_window_width,
                        saved_window_height,
                        window_in_focus,
                        joystick_exit,
                        x_scale_factor,
                        y_scale_factor,
                        real_window_width,
                        real_window_height,
                        mouse_x,
                        mouse_y,
                        data_average_fps,
                        data_CPU_usage,
                        data_current_fps,
                        data_memory_usage,
                        timer,
                        data_average_fps_Max,
                        data_CPU_usage_Max,
                        data_current_fps_Max,
                        data_memory_usage_Max,
                        joystick_zoom,
                        clock,
                        joystick_hat_pressed,
                        fullscreen,
                        joystick_connected)

            return (None,
                display,
                mouse_button_down,
                go_to,
                startup_animation,
                run_timer,
                current_fps,
                average_fps,
                iteration,
                saved_window_width,
                saved_window_height,
                window_in_focus,
                joystick_exit,
                x_scale_factor,
                y_scale_factor,
                real_window_width,
                real_window_height,
                mouse_x,
                mouse_y,
                data_average_fps,
                data_CPU_usage,
                data_current_fps,
                data_memory_usage,
                timer,
                data_average_fps_Max,
                data_CPU_usage_Max,
                data_current_fps_Max,
                data_memory_usage_Max,
                joystick_zoom,
                clock,
                joystick_hat_pressed,
                fullscreen,
                joystick_connected)
                    
    class display_utils:
        def __init__(self):
            pass

        def update_display(
                window_icon,
                fullscreen,
                vsync,
                saved_window_width,
                saved_window_height,
                logging_dictionary,
                output_log,
                platform,
                base_folder,
                fullscreen_x,
                fullscreen_y,
                opengl=False): # add args
            
            try:
                pygame.display.set_icon(window_icon)

                if fullscreen is False:
                    fullscreen = True
                    if opengl:
                        if vsync:
                            display = pygame.display.set_mode(
                                (saved_window_width,
                                    saved_window_height),
                                pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                                vsync=1)
                            
                        else:
                            display = pygame.display.set_mode(
                                (saved_window_width,
                                    saved_window_height),
                                pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                                vsync=0)

                    else:
                        display = pygame.display.set_mode(
                            (saved_window_width,
                                saved_window_height),
                            pygame.RESIZABLE)

                elif fullscreen:
                    fullscreen = False
                    if opengl:
                        if vsync:
                            display = pygame.display.set_mode(
                                (fullscreen_x,
                                    fullscreen_y),
                                pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF,
                                vsync=1)

                        else:
                            display = pygame.display.set_mode(
                                (fullscreen_x,
                                    fullscreen_y),
                                pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF,
                                vsync=0)

                    else:
                        display = pygame.display.set_mode(
                            (fullscreen_x,
                                fullscreen_y),
                            pygame.FULLSCREEN)

                return display, saved_window_width, saved_window_height, fullscreen

            except Exception as Message:
                log_message = "display_utils > display_utils > update_display: "+ str(Message)
                
                logging_utils.create_log_message.update_log_warning(
                    logging_dictionary,
                    log_message,
                    output_log,
                    platform,
                    base_folder)
                
                fullscreen = True
                saved_window_width = 1280
                saved_window_height = 720
                pygame.display.quit()
                pygame.init()
                pygame.display.set_icon(window_icon)
                
                display = pygame.display.set_mode(
                    (saved_window_width, saved_window_height))

                return display, saved_window_width, saved_window_height

        def set_display(
                fullscreen,
                vsync,
                saved_window_width,
                saved_window_height,
                window_icon,
                logging_dictionary,
                output_log,
                platform,
                base_folder,
                fullscreen_x,
                fullscreen_y,
                opengl=False,
                hidden=False):
            
            try:
                pygame.display.set_icon(window_icon)

                if hidden:
                    display = pygame.display.set_mode(
                        (saved_window_width,
                            saved_window_height),
                        pygame.HIDDEN)

                else:
                    if fullscreen:
                        if opengl:
                            if vsync:
                                display = pygame.display.set_mode(
                                    (saved_window_width,
                                        saved_window_height),
                                    pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=1)
                                
                            else:
                                display = pygame.display.set_mode(
                                    (saved_window_width,
                                        saved_window_height),
                                    pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=0)
                        else:
                            display = pygame.display.set_mode(
                                (saved_window_width,
                                    saved_window_height),
                                pygame.RESIZABLE)
                            
                    elif fullscreen is False:
                        if opengl:
                            if vsync:
                                display = pygame.display.set_mode(
                                    (fullscreen_x,
                                        fullscreen_y),
                                    pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=0)
                                
                            else:
                                display = pygame.display.set_mode(
                                    (fullscreen_x,
                                        fullscreen_y),
                                    pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=1)
                        else:
                            display = pygame.display.set_mode(
                                (fullscreen_x,
                                    fullscreen_y),
                                pygame.FULLSCREEN)

                return display, saved_window_width, saved_window_height

            except Exception as Message:
                log_message = "display_utils > display_utils > set_display:", Message
                
                logging_utils.create_log_message.update_log_warning(
                    logging_dictionary,
                    log_message,
                    output_log,
                    platform,
                    base_folder)
                
                saved_window_width = 1280
                saved_window_height = 720
                
                pygame.display.quit()
                pygame.init()
                
                display = pygame.display.set_mode(
                    (saved_window_width, saved_window_height))

                pygame.display.set_icon(window_icon)

                return display, saved_window_width, saved_window_height

        def generate_min_display(vsync, window_icon, width, height):
            pygame.display.set_icon(window_icon)
            
            if vsync:
                display = pygame.display.set_mode(
                    (width, height),
                    pygame.RESIZABLE,
                    vsync=1)
                
            else:
                display = pygame.display.set_mode(
                    (width, height),
                    pygame.RESIZABLE,
                    vsync=0)

            return display

        def get_display_location():
            hwnd = pygame.display.get_wm_info()["window"]

            prototype = ctypes.WINFUNCTYPE(
                ctypes.wintypes.BOOL,
                ctypes.wintypes.HWND,
                ctypes.POINTER(
                    ctypes.wintypes.RECT))

            paramflags = (1, "hwnd"), (2, "lprect")

            GetWindowRect = prototype(
                ("GetWindowRect", ctypes.windll.user32),
                paramflags)

            rect = GetWindowRect(hwnd)
            return rect.left+8, rect.top+31


        def get_play_status(
                platform,
                vsync,
                vsync_fps,
                fps,
                project_sleeping,
                command,
                music,
                fps_overclock,
                base_folder,
                music_volume):
            
            if pygame.display.get_active():
                if platform == "Windows" and vsync:
                    tempfps = vsync_fps
                    
                else:
                    tempfps = fps
                    
                project_sleeping = False
                if not (command == "Play" or
                            command == "benchmark"):
                    
                    if music:
                        pygame.mixer.music.unpause()
                        if pygame.mixer.music.get_busy() == 0:
                            sound_utils.play_sound.play_inventory_sound(
                                platform,
                                base_folder,
                                music_volume)
            else:
                tempfps = 5
                project_sleeping = True
                pygame.mixer.music.fadeout(500)

            if fps_overclock:
                tempfps = 2000

            return tempfps, project_sleeping

    class display_animations:
        def __init__(self):
            pass


        def fade_in(
                startup_animation,
                real_window_width,
                real_window_height,
                run_timer,
                background_color,
                display,
                size="full"):
            
            if startup_animation:
                if size == "full":
                    HideSurface = pygame.Surface(
                        (real_window_width, real_window_height))
                else:
                    HideSurface = pygame.Surface(
                        (real_window_width, real_window_height-40))

                SurfaceAlpha = 255-(run_timer*1000)
                HideSurface.set_alpha(SurfaceAlpha)
                HideSurface.fill(background_color)
                display.blit(
                    HideSurface,
                    (0, 100))

                if SurfaceAlpha <= 0:
                    startup_animation = False

            return startup_animation

        def fade_out(
                startup_animation,
                real_window_width,
                real_window_height,
                run_timer,
                background_color,
                display,
                go_to,
                size="full"):
            
            if startup_animation:
                if size == "full":
                    HideSurface = pygame.Surface(
                        (real_window_width, real_window_height-100))
                else:
                    HideSurface = pygame.Surface(
                        (real_window_width, real_window_height-140))

                SurfaceAlpha = 255-(run_timer*1000)
                HideSurface.set_alpha(255-SurfaceAlpha)
                HideSurface.fill(background_color)

                if go_to == "credits":
                    display.blit(
                        HideSurface,
                        (0, 0))
                else:
                    display.blit(
                        HideSurface,
                        (0, 100))

                if SurfaceAlpha <= 0:
                    startup_animation = False

            return startup_animation
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
