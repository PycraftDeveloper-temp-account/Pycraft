if __name__ != "__main__":
    try:
        import pygame
        import psutil
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
            
    class draw_rose:
        def __init__(self):
            pass

        def create_rose(
                coloursARRAY,
                shape_color,
                x_pos,
                y_pos,
                width,
                height,
                display):

            x_scale_factor = width/524
            y_scale_factor = height/524

            x_pos = x_pos-(51*x_scale_factor)
            y_pos = y_pos-(142*y_scale_factor)
            
            if coloursARRAY is False:
                coloursARRAY = []
                for _ in range(32):
                    coloursARRAY.append(shape_color)

            octagon = [((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                                ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                                ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                                ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                                ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos)]

            pygame.draw.polygon(
                display,
                shape_color,
                octagon,
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[0],
                ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[1],
                ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[2],
                ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[3],
                ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[4],
                ((205*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                width=2)
            
            pygame.draw.line(
                display,
                coloursARRAY[5],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[6],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[7],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[8],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[9],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[10],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[11],
                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[12],
                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[13],
                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[14],
                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[15],
                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[16],
                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[17],
                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[18],
                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[19],
                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[20],
                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[21],
                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[22],
                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[23],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((51*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[24],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((205*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[25],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[25],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[27],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[28],
                ((51*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[29],
                ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[30],
                ((422*x_scale_factor)+x_pos, (666*y_scale_factor)+y_pos),
                ((575*x_scale_factor)+x_pos, (295*y_scale_factor)+y_pos),
                width=2)

            pygame.draw.line(
                display,
                coloursARRAY[31],
                ((575*x_scale_factor)+x_pos, (512*y_scale_factor)+y_pos),
                ((422*x_scale_factor)+x_pos, (142*y_scale_factor)+y_pos),
                width=2)

    class generate_graph:
        def __init__(self):
            pass

        def create_devmode_graph(
                devmode_information_font,
                draw_devmode_graph,
                real_window_width,
                data_average_fps,
                data_CPU_usage,
                data_current_fps,
                data_memory_usage,
                timer,
                data_average_fps_Max,
                data_CPU_usage_Max,
                data_current_fps_Max,
                data_memory_usage_Max,
                display,
                shape_color,
                average_fps,
                iteration,
                current_fps,
                fps_overclock,
                aa,
                fps,
                current_memory_usage):
            
            if draw_devmode_graph:
                if ((real_window_width/2)+100)+timer >= real_window_width:
                    data_average_fps = []
                    data_CPU_usage = []
                    data_current_fps = []
                    data_memory_usage = []

                    timer = 0

                    data_average_fps_Max = 1
                    data_current_fps_Max = 1
                    data_memory_usage_Max = 50
                    data_CPU_usage_Max = 50

                BackingRect = pygame.Rect(
                    (real_window_width/2)+100,
                    0,
                    real_window_width,
                    200)

                pygame.draw.rect(
                    display,
                    shape_color,
                    BackingRect)

                SwapMemory = psutil.swap_memory()
                VirtualMemory = psutil.virtual_memory()

                TotalMemory = SwapMemory.total+VirtualMemory.total
                UsedMemory = SwapMemory.used+VirtualMemory.used

                current_memory_usage = (100/TotalMemory)*(UsedMemory)

                if timer >= 2:
                    data_average_fps.append(
                        [((real_window_width/2)+100)+timer,
                            200-(100/data_average_fps_Max)*(average_fps/(iteration))])

                    try:
                        data_current_fps.append(
                            [((real_window_width/2)+100)+timer,
                                200-(100/data_current_fps_Max)*int(current_fps)])

                    except:
                        data_current_fps.append(
                            [((real_window_width/2)+100)+timer,
                                200-(100/data_current_fps_Max)*int(2000)])

                    data_memory_usage.append(
                        [((real_window_width/2)+100)+timer,
                            200-(2)*current_memory_usage])

                if fps_overclock:
                    data_average_fps_Max = 2000
                elif (average_fps/(iteration)) > data_average_fps_Max:
                    data_average_fps_Max = (average_fps/(iteration))

                if current_fps > data_current_fps_Max:
                    data_current_fps_Max = current_fps

                if current_memory_usage > data_memory_usage_Max:
                    data_memory_usage_Max = current_memory_usage

                timer += 0.2
                if timer >= 5:
                    pygame.draw.lines(
                        display,
                        (255, 0, 0),
                        False,
                        data_average_fps)

                    pygame.draw.lines(
                        display,
                        (0, 255, 0),
                        False,
                        data_current_fps)

                    pygame.draw.lines(
                        display,
                        (0, 0, 255),
                        False,
                        data_memory_usage)

                if len(data_CPU_usage) >= 2:
                    pygame.draw.lines(
                        display,
                        (255, 0, 255),
                        False,
                        data_CPU_usage)

                if fps_overclock:
                    try:
                        runFont = devmode_information_font.render(
                            "".join((f"MemUsE: {int(current_memory_usage)}% | ",
                                        f"CPUUsE: {psutil.cpu_percent()}% | ",
                                        f"fps: {fps} current_fps: {int(current_fps)} average_fps: ",
                                        f"N/A iteration: {iteration}")),
                            aa,
                            (255, 255, 255))

                    except:
                        runFont = devmode_information_font.render(
                            "".join((f"MemUsE: {int(current_memory_usage)}% | ",
                                        f"CPUUsE: {psutil.cpu_percent()}% | ",
                                        f"fps: {fps} current_fps: NaN* average_fps: ",
                                        f"N/A iteration: {iteration}")),
                            aa,
                            (255, 255, 255))
                else:
                    runFont = devmode_information_font.render(
                        "".join((f"MemUsE: {int(current_memory_usage)}% | ",
                                    f"CPUUsE: {psutil.cpu_percent()}% | ",
                                    f"fps: {fps} current_fps: {int(current_fps)} average_fps: ",
                                    f"{int(average_fps/iteration)} ",
                                    f"iteration: {iteration}")),
                        aa,
                        (255, 255, 255))

                display.blit(
                    runFont,
                    ((real_window_width/2)+105, 0))

            return (data_average_fps,
                        data_CPU_usage,
                        data_current_fps,
                        data_memory_usage,
                        timer,
                        data_average_fps_Max,
                        data_CPU_usage_Max,
                        data_current_fps_Max,
                        data_memory_usage_Max,
                        current_memory_usage)

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
