if not __name__ == "__main__":
    print("Started <Pycraft_ThreadingUtils>")
    class ThreadingUtils:
        def __init__(self):
            pass

        def StartVariableChecking(self):
            while True:
                if self.Iteration > 1000:
                    self.aFPS = (self.aFPS/self.Iteration)
                    self.Iteration = 1
                self.FPS = int(self.FPS)
                self.eFPS = int(self.eFPS)

                self.mod_Time__.sleep(1)

                if self.Stop_Thread_Event.is_set():
                    break
        
        def StartCPUlogging(self):
            while True:
                if self.Devmode == 10:
                    if self.Timer >= 2:
                        CPUPercent = self.mod_Psutil__.cpu_percent(0.2)
                        if CPUPercent > self.Data_CPUUsE_Max:
                            self.Data_CPUUsE_Max = CPUPercent
                        elif CPUPercent < self.Data_CPUUsE_Min:
                            self.Data_CPUUsE_Min = CPUPercent

                        self.Data_CPUUsE.append([((self.realWidth/2)+100)+(self.Timer-2), 200-(100/self.Data_CPUUsE_Max)*CPUPercent])
                    else:
                        self.mod_Time__.sleep(0.2)
                else:
                    self.mod_Time__.sleep(1)

                if self.Stop_Thread_Event.is_set():
                    break

        def AdaptiveMode(self):
            while True:
                if self.Stop_Thread_Event.is_set():
                    break
                
                if self.SettingsPreference == "Adaptive":
                    CPUPercent = self.mod_Psutil__.cpu_percent()
                    CoreCount = self.mod_Psutil__.cpu_count()

                    try:
                        gpus = self.mod_GPUtil__.getGPUs()

                        GPUPercent = 0
                        NumOfGPUs = 0

                        for gpu in gpus:
                            NumOfGPUs += 1
                            GPUPercent += gpu.load*100

                        GPUPercent = GPUPercent/NumOfGPUs
                    
                    except:
                        GPUPercent = CPUPercent

                    if (CPUPercent >= (100/CoreCount)) and (GPUPercent >= (100/CoreCount)):
                        self.FPS -= 10
                    else:
                        if self.FPS < self.RecommendedFPS:
                            self.FPS += 10
                        else:
                            if not (self.FPS == self.RecommendedFPS):
                                self.FPS -= 1
                    
                    self.mod_Time__.sleep(0.2)
                else:
                    self.mod_Time__.sleep(1)
                    
    class GetData:
        def __init__(self):
            pass
        
        def LoadMapData(self):
            try:
                self.Load_Progress = 0
                    
                self.Map = self.mod_Pywavefront__.Wavefront(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\Map\\map.obj")), create_materials=True, collect_faces=True) 
                self.MapVerts = self.mod_Numpy__.array(self.Map.vertices)
                self.Map_box = (self.MapVerts[0], self.MapVerts[0])
                
                for self.vertex in self.MapVerts:
                    self.Load_Progress += 1
                    self.mod_ModelMathsUtil__.ComputeOBJPoints.LoadingMapData(self)
                    
                Map_size = [self.Map_box[1][i]-self.Map_box[0][i] for i in range(3)]
                max_Map_size = max(Map_size)
                Map_size = self.G3Dscale
                self.Map_scale = [Map_size/max_Map_size for i in range(3)]
                self.Map_trans = [-(self.Map_box[1][i]+self.Map_box[0][i])/2 for i in range(3)]

                self.map_vertices = []
                for mesh in self.Map.mesh_list:
                    for face in mesh.faces:
                        for vertex_i in face:
                            Data = self.Map.vertices[vertex_i]
                            for k in range(len(Data)):
                                self.Load_Progress += 1
                                self.map_vertices.append(Data[k])
                                                            
                self.ThreadStatus = "Finished"
            except Exception as Error:
                print(Error)
                print(''.join(self.mod_Traceback__.format_exception(None, Error, Error.__traceback__)))
                
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()