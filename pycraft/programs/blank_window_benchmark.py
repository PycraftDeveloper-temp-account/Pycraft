if __name__ != "__main__":
    try:
        import pygame
        
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
            
    class run_blank_window_benchmark:
        """
        This class is in charge of the blank window benchmark seen in the benchmark
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
                set_fps_length,
                set_fps,
                fps_counter,
                max_iteration,
                display):
            """
            This subroutine is used to render the blank window benchmark, accessible when run
            through the benchmark section of Pycraft. This test is one of three designed to stress
            your system. This one is usually considered the 'baseline' as it is the easiest to run.
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                - iteration (int): In the benchmarking process, iteration is used to keep track of
                    how long the benchmark has been running 
                - set_fps_length (int): This is the length of the 'set_fps' array, we use this instead
                    of specifying an integer in order to allow us to make changes later on in Pycraft's
                    development about how many targets to use for the benchmark section.
                - set_fps (array): This is an array of integers that stores FPS targets for the benchmark
                    section of Pycraft, with each element being a different FPS to try to reach, getting
                    progressively harder. The FPS from this array is updated every 500 iterations of the
                    benchmark.
                - fps_counter (int): This is used to store the index used to calculate the next element in the
                    'set_fps' array, this is used so Pycraft know's what to set the FPS to next, and what to set
                    the caption to so that it displays the current FPS being tested.
                - max_iteration (int): This is used to calculate after how many iterations we move onto the next
                    targeted FPS, currently this is set to increase the FPS every 500 'iteration's.
                - display (Pygame Surface): The display object is used throughout Pycraft. This is the identifier
                    we use when we want to interact with/draw to/update Pycraft's gui. Pygame is the main windowing
                    engine used in Pycraft.
                    
            - Keyword Args:
                - None

            - Output:
                - fps_list_X (array): Used to store the iteration of the benchmark. This correlates to a point, with this
                    making up the X coordinate and 'fps_list_Y' making up the Y coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
                - fps_list_Y (array): Used to store the FPS at a given iteration of the benchmark. This correlates to a point, with this
                    making up the Y coordinate and 'fps_list_X' making up the X coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
            """
            fps_list_X = []
            fps_list_Y = []
            while iteration < (500*set_fps_length):
                pygame.display.set_caption(
                    "".join((f"Pycraft: v{self.version}: benchmark | ",
                                f"Running Blank Window benchmark @ {set_fps[fps_counter]} fps")))

                while iteration != max_iteration:
                    if not self.clock.get_fps() == 0:
                        fps_list_X.append(iteration)
                        fps_list_Y.append(self.clock.get_fps())

                    display.fill(self.background_color)

                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT or
                            (event.type == pygame.KEYDOWN and
                                (not event.key == pygame.K_SPACE))):

                            benchmark_utils.close_benchmark.Exitbenchmark(self)

                    pygame.display.flip()
                    iteration += 1
                    self.clock.tick(set_fps[fps_counter])
                    
                fps_counter += 1
                max_iteration += 500

            return fps_list_X, fps_list_Y
        
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
