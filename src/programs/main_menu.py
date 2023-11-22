if __name__ != "__main__":
    try:
        import time
        import math

        import pygame

        from registry_utils import Registry

        import path_utils
        import sound_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (pycraft_main.py).\nMore Details: {error}")

    class Home(Registry):
        def __init__(self):
            sound_utils.play_sound.play_inventory_sound()
            logo_path = f"{Registry.base_path}/src/resources"
            logo_path = f"{logo_path}/general"
            logo_path = f"{logo_path}/pycraft_logo.png"
            self.logo_path = path_utils.Path(logo_path).path
            self.logo = pygame.image.load(self.logo_path).convert_alpha()
            self.start = time.perf_counter()
            self.alpha = 0

        def draw(self):
            Registry.hud.canvas.fill([255, 0, 255, 0])

            if Registry.in_hud: # temp
                rect = pygame.Rect(25, 25, Registry.display_size[0]-50, Registry.display_size[1]-50)
                pygame.draw.rect(Registry.hud.canvas, (30, 30, 30, 100), rect, border_radius=10)
                pygame.draw.rect(Registry.hud.canvas, (80, 80, 80, 100), rect, width=1, border_radius=10)

                self.logo.set_alpha(self.alpha)
                Registry.hud.canvas.blit(self.logo, ((Registry.display_size[0]-self.logo.get_width())/2, (Registry.display_size[1]-self.logo.get_height())/2))

        def main(self):
            run = True
            Registry.displays.set_caption("")
            initial_run = True
            Registry.spin = True
            Registry.in_hud = True
            while run:
                r = int((255/2)*(1+math.sin(time.perf_counter()-self.start)))
                if int(r) != self.alpha:
                    self.alpha = r
                    Registry.update_graphics = True

                (_, run) = Registry.events.handle()
                Registry.hud.update(self.draw, 255)

                if initial_run:
                    initial_run = False
                    Registry.splash_process.terminate()

                pygame.display.flip()
                Registry.clock.tick(Registry.fps)

else:
    MESSAGE = "You need to run this as part of Pycraft, please run the 'main.py' file"
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
