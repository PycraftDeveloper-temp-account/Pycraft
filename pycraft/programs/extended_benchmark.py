if __name__ != "__main__":
    try:
        import traceback
        
        import pygame
        
        import blank_window_benchmark
        import drawing_window_benchmark
        import OpenGL_window_benchmark
        
        import benchmark_utils
        import error_utils
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
            
    class Loadbenchmark:
        """
        This class is in charge of loading and running the 3 window benchmarks in the correct order
        and returning the results of each run back to the benchmark GUI for processing.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(self):
            pass

        def run(self):
            """
            This subroutine is in charge of loading and running the 3 window benchmarks in the correct order
            and returning the results of each run back to the benchmark GUI for processing.
            
            - Args:
                - None
                    
            - Keyword Args:
                - None

            - Output:
                - fps_list_x_1 (array): Used to store the iteration of the benchmark. This correlates to a point, with this
                    making up the X coordinate and 'fps_list_y_1' making up the Y coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
                - fps_list_y_1 (array): Used to store the FPS at a given iteration of the benchmark. This correlates to a point, with this
                    making up the Y coordinate and 'fps_list_x_1' making up the X coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
                - fps_list_x_2 (array): Used to store the iteration of the benchmark. This correlates to a point, with this
                    making up the X coordinate and 'fps_list_y_2' making up the Y coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
                - fps_list_y_2 (array): Used to store the FPS at a given iteration of the benchmark. This correlates to a point, with this
                    making up the Y coordinate and 'fps_list_x_2' making up the X coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
                - fps_list_x_3 (array): Used to store the iteration of the benchmark. This correlates to a point, with this
                    making up the X coordinate and 'fps_list_y_1' making up the Y coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
                - fps_list_y_1 (array): Used to store the FPS at a given iteration of the benchmark. This correlates to a point, with this
                    making up the Y coordinate and 'fps_list_x_3' making up the X coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
            """
            try:
                (Setfps,
                    Setfpslength,
                    display,
                    iteration,
                    fpscounter,
                    Maxiteration) = benchmark_utils.start_benchmark.generate_benchmark()

                (fps_list_x_1,
                    fps_list_y_1) = blank_window_benchmark.run_blank_window_benchmark.start(
                    self,
                    iteration,
                    Setfpslength,
                    Setfps,
                    fpscounter,
                    Maxiteration,
                    display)

                pygame.display.set_caption(
                    "".join((f"Pycraft: v{self.version}: ",
                    "benchmark | Preparing Animated benchmark")))

                benchmark_utils.clear_benchmark.run_spacer(
                    self,
                    display,
                    self.background_color,
                    self.clock)

                (fps_list_x_2,
                    fps_list_y_2) = drawing_window_benchmark.run_drawing_window_benchmark.start(
                    self,
                    iteration,
                    Setfpslength,
                    Setfps,
                    fpscounter,
                    Maxiteration,
                    display)

                pygame.display.set_caption(
                "".join((f"Pycraft: v{self.version}: benchmark | ",
                            f"Preparing OpenGL benchmark")))
                
                benchmark_utils.clear_benchmark.run_spacer(
                    self,
                    display,
                    self.background_color,
                    self.clock)

                (display,
                    ctx,
                    wnd) = benchmark_utils.start_benchmark.generate_opengl_benchmark()

                (texture,
                    mvp,
                    light,
                    vao,
                    timer,
                    aspect_ratio) = OpenGL_window_benchmark.run_opengl_window_benchmark.setup(
                        self,
                        wnd)

                (fps_list_x_3,
                    fps_list_y_3) = OpenGL_window_benchmark.run_opengl_window_benchmark.start(
                    self,
                    iteration,
                    Setfpslength,
                    Setfps,
                    fpscounter,
                    Maxiteration,
                    ctx,
                    texture,
                    mvp,
                    light,
                    vao,
                    timer,
                    aspect_ratio)

                return (fps_list_x_1,
                            fps_list_y_1,
                            fps_list_x_2,
                            fps_list_y_2,
                            fps_list_x_3,
                            fps_list_y_3)
                
            except Exception as Message:
                error_message = "Extendedbenchmark > Loadbenchmark > run: "+str(Message)
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
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
