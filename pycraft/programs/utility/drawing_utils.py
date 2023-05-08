if __name__ != "__main__":
    try:
        import pygame
        import psutil
        
        from registry_utils import Registry
    except ModuleNotFoundError as message:
        from tkinter import messagebox
        error_message = f"{message} in drawing_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class draw_rose(Registry):
        def create_rose(
                colorsARRAY,
                x_pos,
                y_pos,
                width,
                height):

            x_scale_factor = width/524
            y_scale_factor = height/524

            x_pos = x_pos-(51*x_scale_factor)
            y_pos = y_pos-(142*y_scale_factor)
            
            if colorsARRAY is False:
                colorsARRAY = []
                for _ in range(32):
                    colorsARRAY.append(Registry.shape_color)

            octagon = [((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                                ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                                ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                                ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                                ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos)]

            pygame.draw.polygon(
                Registry.display,
                Registry.shape_color,
                octagon,
                width=2)

            if Registry.aa:
                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[0],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[1],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[2],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[3],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[4],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))
                
                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[5],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[6],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[7],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[8],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[9],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[10],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[11],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[12],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[13],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[14],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[15],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[16],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[17],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[18],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[19],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[20],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[21],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[22],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[23],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[24],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[25],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[25],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[27],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[28],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[29],
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[30],
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos))

                pygame.draw.aaline(
                    Registry.display,
                    colorsARRAY[31],
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos))
                
            else:
                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[0],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[1],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[2],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[3],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[4],
                    ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)
                
                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[5],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[6],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[7],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[8],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[9],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[10],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[11],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[12],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[13],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[14],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[15],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[16],
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[17],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[18],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[19],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[20],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[21],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[22],
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[23],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[24],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[25],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[25],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[27],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[28],
                    ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[29],
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[30],
                    ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                    ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                    width=2)

                pygame.draw.line(
                    Registry.display,
                    colorsARRAY[31],
                    ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                    ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                    width=2)

    class generate_graph(Registry):
        def __init__(self) -> None:
            self.pos_x = (Registry.real_window_width/2)+100
            self.pos_y = 0
            self.x_size = Registry.real_window_width-self.pos_x
            self.y_size = 200
            
        def plotter(self, argument, color) -> None:
            if not max(argument) == 0:
                arr = []
                x_pos = self.pos_x
                pointer_spacing = self.x_size/len(argument)
                for element in argument:
                    x_point = x_pos
                    y_point = (200/max(argument))*element
                    arr.append([x_point, 200-y_point])
                    x_pos += pointer_spacing
                
                print(arr[-1], color)
                
                if len(arr) > 2:
                    if Registry.aa:
                        pygame.draw.aalines(Registry.display, color, False, arr)
                    else:
                        pygame.draw.lines(Registry.display, color, False, arr)
        
        def draw_developer_graph(self) -> None:
            if Registry.draw_devmode_graph or True:
                rect = pygame.Rect(
                    self.pos_x,
                    self.pos_y,
                    self.x_size,
                    self.y_size+1)
                
                pygame.draw.rect(
                    Registry.display,
                    Registry.shape_color,
                    rect)
                
                self.plotter(Registry.memory_usage, (0, 255, 0))
                self.plotter(Registry.fps_history, (255, 0, 0))
                        
                self.plotter(Registry.cpu_history, (0, 0, 255))
                        
                runFont = Registry.small_content_font.render(
                        "".join((f"mem: {int((Registry.memory_usage[-1]/1000000))} mb | ",
                                    f"cpu: {psutil.Process(Registry.process_id).cpu_percent()}% | ",
                                    f"fps: {Registry.fps} fps | ",
                                    f"current: {int(Registry.fps_history[-1])} fps | ",
                                    f"average: {int(Registry.average_fps)} fps")),
                        Registry.aa,
                        (255, 255, 255))

                Registry.display.blit(
                    runFont,
                    ((Registry.real_window_width/2)+105, 0))

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
