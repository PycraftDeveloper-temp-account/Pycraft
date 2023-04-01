if __name__ != "__main__":
    try:
        import pygame
        
        from registry_utils import Registry
        
        import benchmark_utils
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in blank_window_benchmark"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class run_blank_window_benchmark(Registry):
        def start(
                iteration,
                set_fps_length,
                set_fps,
                fps_counter,
                max_iteration):
            
            fps_list_X = []
            fps_list_Y = []
            while iteration < (500*set_fps_length):
                pygame.display.set_caption(
                    "".join((f"Pycraft: v{Registry.version}: benchmark | ",
                                f"Running Blank Window benchmark @ {set_fps[fps_counter]} fps")))

                while iteration != max_iteration:
                    if not Registry.clock.get_fps() == 0:
                        fps_list_X.append(iteration)
                        fps_list_Y.append(Registry.clock.get_fps())

                    display.fill(Registry.background_color)

                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT or
                            (event.type == pygame.KEYDOWN and
                                (not event.key == pygame.K_SPACE))):

                            benchmark_utils.close_benchmark.exit_benchmark()

                    pygame.display.flip()
                    iteration += 1
                    Registry.clock.tick(set_fps[fps_counter])
                    
                fps_counter += 1
                max_iteration += 500

            return fps_list_X, fps_list_Y
        
else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()
