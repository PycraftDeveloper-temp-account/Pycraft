if __name__ != "__main__":
    try:
        import pygame
        
        from registry_utils import Registry
        
        import drawing_utils
        import benchmark_utils
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in drawing_window_benchmark"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class run_drawing_window_benchmark(Registry):
        def start(
                iteration,
                Setfpslength,
                Setfps,
                fpscounter,
                Maxiteration):
            
            fpslistX = []
            fpslistY = []
            while iteration < (500*Setfpslength):
                pygame.display.set_caption(
                    "".join((f"Pycraft: v{Registry.version}: benchmark | ",
                                f"Running Animated Window benchmark @ {Setfps[fpscounter]} fps")))

                while not iteration == Maxiteration:
                    if not Registry.clock.get_fps() == 0:
                        fpslistX.append(iteration)
                        fpslistY.append(Registry.clock.get_fps())

                    display.fill(Registry.background_color)

                    for _ in range(10):
                        drawing_utils.draw_rose.create_rose(
                            False,
                            51,
                            142,
                            524*Registry.x_scale_factor,
                            524*Registry.y_scale_factor,
                            True)

                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT or
                            (event.type == pygame.KEYDOWN and
                                (not event.key == pygame.K_SPACE))):

                            benchmark_utils.close_benchmark.exit_benchmark(self)

                    pygame.display.flip()
                    iteration += 1
                    Registry.clock.tick(Setfps[fpscounter])
                    
                fpscounter += 1
                Maxiteration += 500

            return fpslistX, fpslistY
        
else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
