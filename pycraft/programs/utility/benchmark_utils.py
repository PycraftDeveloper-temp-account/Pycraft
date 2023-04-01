if __name__ != "__main__":
    try:
        import pygame
        import moderngl
        import moderngl_window
        import pyautogui

        from registry_utils import Registry
        
        import pycraft_main
        
        import display_utils
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in benchmark_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class close_benchmark(Registry):
        def exit_benchmark():
            pygame.display.quit()
            pygame.display.init()
            Registry.command = "Undefined"
            Registry.data_average_fps = []
            Registry.data_CPU_usage = []
            Registry.data_current_fps = []
            Registry.data_memory_usage = []

            Registry.timer = 0

            Registry.data_average_fps_Max = 1
            Registry.data_CPU_usage_Max = 1
            Registry.data_current_fps_Max = 1
            Registry.data_memory_usage_Max = 1

            fullscreen_x = pyautogui.size()[0]
            fullscreen_y = pyautogui.size()[1]

            (Registry.display,
                Registry.saved_window_width,
                Registry.saved_window_height) = display_utils.display_utils.set_display(
                    Registry.fullscreen,
                    Registry.vsync,
                    Registry.saved_window_width,
                    Registry.saved_window_height,
                    Registry.window_icon,
                    Registry.logging_dictionary,
                    Registry.output_log,
                    Registry.platform,
                    Registry.base_folder,
                    fullscreen_x,
                    fullscreen_y)
                
            pycraft_main.Initialize.menu_selector()

    class start_benchmark(Registry):
        def generate_benchmark(create_display=True):
            set_fps = [15,
                        30,
                        45,
                        60,
                        75,
                        90,
                        105,
                        120,
                        135,
                        150,
                        200,
                        250,
                        300,
                        350,
                        500]

            set_fps_length = len(set_fps)

            if create_display:
                if pygame.display.get_init():
                    pygame.display.quit()
                    pygame.display.init()

                display = pygame.display.set_mode((1280, 720))

            else:
                display = None

            iteration = 0
            fps_counter = 0
            max_iteration = 500

            return set_fps, set_fps_length, display, iteration, fps_counter, max_iteration

        def generate_opengl_benchmark():
            if pygame.display.get_init():
                pygame.display.quit()
                pygame.display.init()

            display = pygame.display.set_mode(
                (1280, 720),
                pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                vsync=0)

            ctx = moderngl.create_context(standalone=False)

            wnd = moderngl_window.get_local_window_cls("pygame2")

            moderngl_window.activate_context(wnd, ctx)

            return display, ctx, wnd

    class clear_benchmark(Registry):
        def run_spacer(
                self,
                display,
                background_color,
                clock):

            iteration = 0

            while iteration != 60:
                display.fill(background_color)

                for event in pygame.event.get():
                    if (event.type == pygame.QUIT or
                        (event.type == pygame.KEYDOWN and
                            (not event.key == pygame.K_SPACE))):

                        close_benchmark.exit_benchmark(self)

                pygame.display.flip()
                iteration += 1
                clock.tick(60)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
