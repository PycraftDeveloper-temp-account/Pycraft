if __name__ != "__main__":
    try:
        import time
        import traceback
        
        import psutil
        import GPUtil

        from registry_utils import Registry
        import metrics_utils
        import logging_utils
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in threading_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()

    class pycraft_core_threads(Registry):
        def general_threading_utility():
            try:
                while True:
                    metrics_utils.Metrics().get_memory_metrics()
                    if (Registry.fps < 15 or
                            Registry.fps > 500):
                        
                        information_message = "".join(("ThreadingUtil > ThreadingUtils > ",
                                        "general_threading_utility: 'Registry.fps' ",
                                        "variable contained an invalid value, ",
                                        f"this has been reset to 60 from {Registry.fps} previously"))

                        logging_utils.create_log_message.update_log_information(
                            information_message)
                        
                        Registry.fps = 60

                    else:
                        if Registry.fps_overclock is False:
                            Registry.fps = int(Registry.fps)

                    if Registry.fps_overclock is False:
                        Registry.current_fps = int(Registry.current_fps)

                    else:
                        if Registry.average_fps == float("inf"):
                            Registry.average_fps = 1
                    time.sleep(1/30)
            except Exception as message:
                Registry.error_message = "".join(("ThreadingUtils > ThreadingUtils ",
                                             f"> general_threading_utility: {str(message)}"))

                Registry.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        message,
                        message.__traceback__))
                
            logging_utils.create_log_message.update_log_information(
                "'thread_pycraft_general' has stopped")

        def adaptive_mode():
            try:
                while True:
                    if Registry.settings_preset == "adaptive":
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

                        except Exception as message:
                            log_message = "ThreadingUtils > ThreadingUtils > adaptive_mode: "+str(message)

                            logging_utils.create_log_message.update_log_information(
                                log_message)
                            
                            GPUPercent = CPUPercent

                        if CPUPercent > 75 and Registry.fps > 25:
                            Registry.fps -= 1
                            if CPUPercent > 90 and Registry.fps > 25:
                                Registry.fps -= 9

                        elif ProcessPercent > 50 and Registry.fps > 25:
                            Registry.fps -= 1
                            if ProcessPercent > 75 and Registry.fps > 25:
                                Registry.fps -= 9

                        else:
                            if GPUPercent > 50 and Registry.fps > 25:
                                Registry.fps -= 1
                                if GPUPercent > 75 and Registry.fps > 25:
                                    Registry.fps -= 9

                            else:
                                if Registry.fps < 500:
                                    Registry.fps += 1
                    else:
                        time.sleep(1)
                        
            except Exception as message:
                Registry.error_message = "ThreadingUtils > ThreadingUtils > adaptive_mode: "+str(message)

                Registry.error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        message,
                        message.__traceback__))

            logging_utils.create_log_message.update_log_information(
                "'thread_adaptive_mode' has stopped")

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
