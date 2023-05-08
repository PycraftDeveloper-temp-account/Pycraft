if __name__ != "__main__":
    try:
        import psutil
        
        from registry_utils import Registry
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in credits"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
    
    
    class Metrics(Registry):
        def __init__(self):
            pass
        
        def get_metrics(self):
            if len(Registry.fps_history) > Registry.fps*3:
                del Registry.fps_history[0]
            if len(Registry.memory_usage) > Registry.fps*3:
                del Registry.memory_usage[0]
            if len(Registry.cpu_history) > Registry.fps*3:
                del Registry.cpu_history[0]
                
            Registry.fps_history.append(Registry.clock.get_fps())
            Registry.average_fps = sum(Registry.fps_history)/len(Registry.fps_history)
            Registry.memory_usage.append(psutil.Process(pid=Registry.process_id).memory_full_info().uss)
            cpu_times = psutil.Process(pid=Registry.process_id).cpu_times()
            previous_total_cpu_process_time = Registry.cpu_time
            total_cpu_process_time = cpu_times.user + cpu_times.system
            delta_total_cpu_process_time = total_cpu_process_time - previous_total_cpu_process_time
            Registry.cpu_time = total_cpu_process_time
            Registry.cpu_history.append(delta_total_cpu_process_time)
            
else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
