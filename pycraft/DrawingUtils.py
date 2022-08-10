if __name__ != "__main__":
    print("Started <Pycraft_DrawingUtils>")

    class DrawRose:
        def __init__(self):
            pass

        def CreateRose(self, xScaleFact, yScaleFact, coloursARRAY):
            try:
                if coloursARRAY is False:
                    coloursARRAY = []
                    for i in range(32):
                        coloursARRAY.append(self.shape_color)

                defLargeOctagon = [(205*xScaleFact, 142*yScaleFact),
                                   (51*xScaleFact, 295*yScaleFact),
                                   (51*xScaleFact, 512*yScaleFact),
                                   (205*xScaleFact, 666*yScaleFact),
                                   (422*xScaleFact, 666*yScaleFact),
                                   (575*xScaleFact, 512*yScaleFact),
                                   (575*xScaleFact, 295*yScaleFact),
                                   (422*xScaleFact, 142*yScaleFact)]

                self.mod_pygame__.draw.polygon(
                    self.display,
                    self.shape_color,
                    defLargeOctagon,
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[0],
                    (205*xScaleFact,142*yScaleFact),
                    (51*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[1],
                    (205*xScaleFact, 142*yScaleFact),
                    (205*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[2],
                    (205*xScaleFact, 142*yScaleFact),
                    (422*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[3],
                    (205*xScaleFact, 142*yScaleFact),
                    (575*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[4],
                    (205*xScaleFact, 142*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[5],
                    (51*xScaleFact, 295*yScaleFact),
                    (51*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[6],
                    (51*xScaleFact, 295*yScaleFact),
                    (205*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[7],
                    (51*xScaleFact, 295*yScaleFact),
                    (422*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[8],
                    (51*xScaleFact, 295*yScaleFact),
                    (575*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[9],
                    (51*xScaleFact, 295*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[10],
                    (51*xScaleFact, 295*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[11],
                    (51*xScaleFact, 512*yScaleFact),
                    (51*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[12],
                    (51*xScaleFact, 512*yScaleFact),
                    (205*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[13],
                    (51*xScaleFact, 512*yScaleFact),
                    (422*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[14],
                    (51*xScaleFact, 512*yScaleFact),
                    (575*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[15],
                    (51*xScaleFact, 512*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[16],
                    (51*xScaleFact, 512*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[17],
                    (205*xScaleFact, 666*yScaleFact),
                    (51*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[18],
                    (205*xScaleFact, 666*yScaleFact),
                    (51*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[19],
                    (205*xScaleFact, 666*yScaleFact),
                    (422*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[20],
                    (205*xScaleFact, 666*yScaleFact),
                    (575*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[21],
                    (205*xScaleFact, 666*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[22],
                    (205*xScaleFact, 666*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[23],
                    (51*xScaleFact, 295*yScaleFact),
                    (51*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[24],
                    (51*xScaleFact, 295*yScaleFact),
                    (205*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[25],
                    (51*xScaleFact, 295*yScaleFact),
                    (422*xScaleFact, 666*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[25],
                    (51*xScaleFact, 295*yScaleFact),
                    (575*xScaleFact, 512*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[27],
                    (51*xScaleFact, 295*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[28],
                    (51*xScaleFact, 295*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[29],
                    (422*xScaleFact, 666*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[30],
                    (422*xScaleFact, 666*yScaleFact),
                    (575*xScaleFact, 295*yScaleFact),
                    width=2)

                self.mod_pygame__.draw.line(
                    self.display,
                    coloursARRAY[31],
                    (575*xScaleFact, 512*yScaleFact),
                    (422*xScaleFact, 142*yScaleFact),
                    width=2)

            except Exception as Message:
                self.error_message = "DrawingUtils > DrawRose > CreateRose: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

    class GenerateGraph:
        def __init__(self):
            pass

        def create_devmode_graph(self, DataFont):
            if self.devmode == 10:
                try:
                    if ((self.real_window_width/2)+100)+self.timer >= self.real_window_width:
                        self.data_aFPS = []
                        self.data_CPU_usage = []
                        self.data_eFPS = []
                        self.data_memory_usage = []

                        self.timer = 0

                        self.data_aFPS_Max = 1
                        self.data_CPU_usage_Max = 1
                        self.data_eFPS_Max = 1
                        self.data_memory_usage_Max = 50
                        self.data_CPU_usage_Max = 50

                    BackingRect = self.mod_pygame__.Rect(
                        (self.real_window_width/2)+100,
                        0,
                        self.real_window_width,
                        200)

                    self.mod_pygame__.draw.rect(
                        self.display,
                        self.shape_color,
                        BackingRect)

                    SwapMemory = self.mod_psutil__.swap_memory()
                    VirtualMemory = self.mod_psutil__.virtual_memory()

                    TotalMemory = SwapMemory.total+VirtualMemory.total
                    UsedMemory = SwapMemory.used+VirtualMemory.used

                    self.current_memory_usage = (100/TotalMemory)*(UsedMemory)

                    if self.timer >= 2:
                        self.data_aFPS.append(
                            [((self.real_window_width/2)+100)+self.timer,
                             200-(100/self.data_aFPS_Max)*(self.aFPS/(self.iteration))])

                        try:
                            self.data_eFPS.append(
                                [((self.real_window_width/2)+100)+self.timer,
                                 200-(100/self.data_eFPS_Max)*int(self.eFPS)])

                        except:
                            self.data_eFPS.append(
                                [((self.real_window_width/2)+100)+self.timer,
                                 200-(100/self.data_eFPS_Max)*int(2000)])

                        self.data_memory_usage.append(
                            [((self.real_window_width/2)+100)+self.timer,
                             200-(2)*self.current_memory_usage])

                    if self.FPS_overclock:
                        self.data_aFPS_Max = 2000
                    elif (self.aFPS/(self.iteration)) > self.data_aFPS_Max:
                        self.data_aFPS_Max = (self.aFPS/(self.iteration))

                    if self.eFPS > self.data_eFPS_Max:
                        self.data_eFPS_Max = self.eFPS

                    if self.current_memory_usage > self.data_memory_usage_Max:
                        self.data_memory_usage_Max = self.current_memory_usage

                    self.timer += 0.2
                    if self.timer >= 5:
                        self.mod_pygame__.draw.lines(
                            self.display,
                            (255, 0, 0),
                            False,
                            self.data_aFPS)

                        self.mod_pygame__.draw.lines(
                            self.display,
                            (0, 255, 0),
                            False,
                            self.data_eFPS)

                        self.mod_pygame__.draw.lines(
                            self.display,
                            (0, 0, 255),
                            False,
                            self.data_memory_usage)

                    if len(self.data_CPU_usage) >= 2:
                        self.mod_pygame__.draw.lines(
                            self.display,
                            (255, 0, 255),
                            False,
                            self.data_CPU_usage)

                    if self.FPS_overclock:
                        try:
                            runFont = DataFont.render(
                                "".join((f"MemUsE: {int(self.current_memory_usage)}% | ",
                                         f"CPUUsE: {self.mod_psutil__.cpu_percent()}% | ",
                                         f"FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: ",
                                         f"N/A iteration: {self.iteration}")),
                                self.aa,
                                (255, 255, 255))

                        except:
                            runFont = DataFont.render(
                                "".join((f"MemUsE: {int(self.current_memory_usage)}% | ",
                                         f"CPUUsE: {self.mod_psutil__.cpu_percent()}% | ",
                                         f"FPS: {self.FPS} eFPS: NaN* aFPS: ",
                                         f"N/A iteration: {self.iteration}")),
                                self.aa,
                                (255, 255, 255))
                    else:
                        runFont = DataFont.render(
                            "".join((f"MemUsE: {int(self.current_memory_usage)}% | ",
                                     f"CPUUsE: {self.mod_psutil__.cpu_percent()}% | ",
                                     f"FPS: {self.FPS} eFPS: {int(self.eFPS)} aFPS: ",
                                     f"{int(self.aFPS/self.iteration)} ",
                                     f"iteration: {self.iteration}")),
                            self.aa,
                            (255, 255, 255))

                    self.display.blit(
                        runFont,
                        ((self.real_window_width/2)+105, 0))

                except Exception as Message:
                    self.error_message = "".join(("DrawingUtils > GenerateGraph ",
                                                 f"> create_devmode_graph: {str(Message)}"))
                    self.error_message_detailed = "".join(
                        self.mod_traceback__.format_exception(
                            None,
                            Message,
                            Message.__traceback__))

                    self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

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
