if __name__ != "__main__":
    try:
        import threading
        
        import pygame
        import psutil
        
        from registry_utils import Registry
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in caption_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class generate_captions(Registry): 
        def get_loading_caption(
                version,
                num):

            if num == 0:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (-)")
            elif num == 1:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (\)")
            elif num == 2:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (|)")
            elif num == 3:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading (/)")
            else:
                pygame.display.set_caption(f"Pycraft: v{version}: Loading")
                
        def set_caption(
                location="Playing"):
            if Registry.detailed_captions:
                hours = int((Registry.play_time/60)/60)
                minutes = int(Registry.play_time/60)
                seconds = int(Registry.play_time)

                position = [
                    round(Registry.x, 2),
                    round(Registry.y, 2),
                    round(Registry.z, 2)]
                
                velocity = [
                    round(Registry.total_move_x, 2),
                    round(Registry.total_move_y, 2),
                    round(Registry.total_move_z, 2)]
                
                fps = [
                    round(Registry.fps, 2),
                    round(Registry.fps_history[-1], 2),
                    round(Registry.average_fps, 2)]

                time = f"{hours} : {minutes} : {seconds}"
                
                memory_usage = round(Registry.current_memory_usage, 2)
                cpu_usage = round(Registry.cpu_usage, 2)
                caption = f"Pycraft: v{Registry.version}: {location} | "
                caption += f"Play time: {time} | "
                caption += f"Position: {position} | "
                caption += f"Velocity: {velocity} | "
                caption += f"Frame-rates: {fps} | "
                caption += f"Efficiency: {Registry.efficiency}%  "
                caption += f"Memory usage: {memory_usage}% | "
                caption += f"CPU usage: {cpu_usage}% | "
                caption += f"Weather: {Registry.weather} | "
                caption += f"Thread count: {threading.active_count()}"
                
                pygame.display.set_caption(caption)
            
            else:
                pygame.display.set_caption(
                    f"Pycraft: v{Registry.version}: {location}")

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
