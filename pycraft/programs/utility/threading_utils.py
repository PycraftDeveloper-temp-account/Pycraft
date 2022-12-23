if __name__ != "__main__":
    try:
        import time
        import traceback
        
        import psutil
        import GPUtil

        import logging_utils
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
            
    class pycraft_core_threads:
        def __init__(self):
            pass

        def general_threading_utility(self):
            try:
                while True:
                    if self.draw_devmode_graph:
                        if self.timer >= 2:
                            CPUPercent = psutil.cpu_percent(0.5)
                            if CPUPercent > self.data_CPU_usage_Max:
                                self.data_CPU_usage_Max = CPUPercent

                            self.data_CPU_usage.append([
                                ((self.real_window_width/2)+100)+(self.timer),
                                200-(2)*CPUPercent])

                        time.sleep(0.5)

                    else:
                        time.sleep(1)

                    if self.iteration > 1000:
                        self.average_fps = (self.average_fps/self.iteration)
                        self.iteration = 1

                    if (self.fps < 15 or
                            self.fps > 500):
                        
                        information_message = "".join(("ThreadingUtil > ThreadingUtils > ",
                                        "general_threading_utility: 'self.fps' ",
                                        "variable contained an invalid value, ",
                                        f"this has been reset to 60 from {self.fps} previously"))

                        logging_utils.create_log_message.update_log_information(
                            self.logging_dictionary,
                            information_message,
                            self.output_log,
                            self.platform,
                            self.base_folder)
                        
                        self.fps = 60

                    else:
                        if self.fps_overclock is False:
                            self.fps = int(self.fps)

                    if self.fps_overclock is False:
                        self.current_fps = int(self.current_fps)

                    else:
                        if self.average_fps == float("inf"):
                            self.average_fps = 1
                            self.iteration = 1
                            
            except Exception as Message:
                self.error_message = "".join(("ThreadingUtils > ThreadingUtils ",
                                             f"> general_threading_utility: {str(Message)}"))

                self.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))
                
            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "'thread_pycraft_general' has stopped",
                self.output_log,
                self.platform,
                self.base_folder)

        def AdaptiveMode(self):
            try:
                while True:
                    if self.settings_preset == "adaptive":
                        ProcessPercent = psutil.Process().cpu_percent(0.1)
                        CPUPercent = psutil.cpu_percent(0.1)

                        try:
                            gpus = GPUtil.getGPUs()

                            GPUPercent = 0
                            NumOfGPUs = 0

                            for gpu in gpus:
                                NumOfGPUs += 1
                                GPUPercent += gpu.load*100

                            GPUPercent = GPUPercent/NumOfGPUs

                        except Exception as Message:
                            log_message = "ThreadingUtils > ThreadingUtils > AdaptiveMode: "+str(Message)

                            logging_utils.create_log_message.update_log_information(
                                self.logging_dictionary,
                                log_message,
                                self.output_log,
                                self.platform,
                                self.base_folder)
                            
                            GPUPercent = CPUPercent

                        if CPUPercent > 75 and self.fps > 25:
                            self.fps -= 1
                            if CPUPercent > 90 and self.fps > 25:
                                self.fps -= 9

                        elif ProcessPercent > 50 and self.fps > 25:
                            self.fps -= 1
                            if ProcessPercent > 75 and self.fps > 25:
                                self.fps -= 9

                        else:
                            if GPUPercent > 50 and self.fps > 25:
                                self.fps -= 1
                                if GPUPercent > 75 and self.fps > 25:
                                    self.fps -= 9

                            else:
                                if self.fps < 500:
                                    self.fps += 1
                    else:
                        time.sleep(1)
                        
            except Exception as Message:
                self.error_message = "ThreadingUtils > ThreadingUtils > AdaptiveMode: "+str(Message)

                self.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

            logging_utils.create_log_message.update_log_information(
                self.logging_dictionary,
                "'thread_adaptive_mode' has stopped",
                self.output_log,
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
