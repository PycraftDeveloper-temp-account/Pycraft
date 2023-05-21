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
            
            fps = Registry.clock.get_fps()
            if len(Registry.fps_history) < 2:
                Registry.fps_history.append(fps)
            else:
                if fps != Registry.fps_history[-1]:
                    Registry.fps_history.append(fps)
                
            Registry.average_fps = sum(Registry.fps_history)/len(Registry.fps_history)
            
            memory_usage = psutil.Process(pid=Registry.process_id).memory_full_info().uss
            if len(Registry.memory_usage) < 2:
                Registry.memory_usage.append(memory_usage)
            else:
                if memory_usage != Registry.memory_usage[-1]:
                    Registry.memory_usage.append(memory_usage)
                
            process = psutil.Process(pid=Registry.process_id)
            cpu_times = process.cpu_times()
            previous_total_cpu_process_time = Registry.cpu_time
            total_cpu_process_time = cpu_times.user + cpu_times.system
            delta_total_cpu_process_time = total_cpu_process_time - previous_total_cpu_process_time
            Registry.cpu_time = total_cpu_process_time
            Registry.cpu_usage = process.cpu_percent()
            
            if len(Registry.cpu_history) < 2:
                Registry.cpu_history.append(delta_total_cpu_process_time)
            else:
                if delta_total_cpu_process_time != Registry.cpu_history[-1]:
                    Registry.cpu_history.append(delta_total_cpu_process_time)
            
            if len(Registry.frame_efficiency) >= Registry.render_ratio:
                Registry.efficiency = round(100*(sum(Registry.frame_efficiency)/len(Registry.frame_efficiency)), 2)
                Registry.frame_efficiency = []
                Registry.forced_frame = True
                
            if Registry.forced_frame:
                Registry.frame_efficiency.append(0)
            else:
                Registry.frame_efficiency.append(1)
else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
