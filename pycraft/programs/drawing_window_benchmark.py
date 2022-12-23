if __name__ != "__main__":
    try:
        import pygame
        
        import drawing_utils
        import benchmark_utils
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
            
    class run_drawing_window_benchmark:
        """
        This class is in charge of the drawing window benchmark seen in the benchmark
        section of Pycraft.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(self):
            pass
        
        def start(
                self,
                iteration,
                Setfpslength,
                Setfps,
                fpscounter,
                Maxiteration,
                display):
            """
            This subroutine is used to render the drawing window benchmark, accessible when run
            through the benchmark section of Pycraft. This test is the second of three designed to stress
            your system. This one is usually used to measure the performance of CPU rendering with Pygame
            on your device.
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                - iteration (int): In the benchmarking process, iteration is used to keep track of
                    how long the benchmark has been running 
                - Setfpslength (int): This is the length of the 'Setfps' array, we use this instead
                    of specifying an integer in order to allow us to make changes later on in Pycraft's
                    development about how many targets to use for the benchmark section.
                - Setfps (array): This is an array of integers that stores FPS targets for the benchmark
                    section of Pycraft, with each element being a different FPS to try to reach, getting
                    progressively harder. The FPS from this array is updated every 500 iterations of the
                    benchmark.
                - fpscounter (int): This is used to store the index used to calculate the next element in the
                    'Setfps' array, this is used so Pycraft know's what to set the FPS to next, and what to set
                    the caption to so that it displays the current FPS being tested.
                - Maxiteration (int): This is used to calculate after how many iterations we move onto the next
                    targeted FPS, currently this is set to increase the FPS every 500 'iteration's.
                - display (Pygame Surface): The display object is used throughout Pycraft. This is the identifier
                    we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing
                    engine used in Pycraft.
                    
            - Keyword Args:
                - None

            - Output:
                - fpslistX (array): Used to store the iteration of the benchmark. This correlates to a point, with this
                    making up the X coordinate and 'fpslistY' making up the Y coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
                - fpslistY (array): Used to store the FPS at a given iteration of the benchmark. This correlates to a point, with this
                    making up the Y coordinate and 'fpslistX' making up the X coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
            """
            fpslistX = []
            fpslistY = []
            while iteration < (500*Setfpslength):
                pygame.display.set_caption(
                    "".join((f"Pycraft: v{self.version}: benchmark | ",
                                f"Running Animated Window benchmark @ {Setfps[fpscounter]} fps")))

                while not iteration == Maxiteration:
                    if not self.clock.get_fps() == 0:
                        fpslistX.append(iteration)
                        fpslistY.append(self.clock.get_fps())

                    display.fill(self.background_color)

                    for _ in range(10):
                        drawing_utils.draw_rose.create_rose(
                            False,
                            self.shape_color,
                            self.x_scale_factor,
                            self.y_scale_factor,
                            display)

                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT or
                            (event.type == pygame.KEYDOWN and
                                (not event.key == pygame.K_SPACE))):

                            benchmark_utils.close_benchmark.Exitbenchmark(self)

                    pygame.display.flip()
                    iteration += 1
                    self.clock.tick(Setfps[fpscounter])
                    
                fpscounter += 1
                Maxiteration += 500

            return fpslistX, fpslistY