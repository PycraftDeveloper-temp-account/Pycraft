if __name__ != "__main__":
    try:
        import os
        import time
        
        import pygame
        import numpy
        import moderngl
        import moderngl_window
        import pyrr
        
        import benchmark_utils
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
            
    class run_opengl_window_benchmark:
        """
        This class is in charge of the OpenGL window benchmark seen in the benchmark
        section of Pycraft.
        
        - Args:
            - None
                
        - Keyword Args:
            - None
        """
        
        def __init__(self):
            pass

        def setup(
                self,
                wnd):
            """
            This subroutine is in charge of loading the resources required by the OpenGL
            benchmark, including:
            1x Texture
            1x 3D Scene
            1x GLSL Shader
            And also sets the window parameters so that the OpenGL benchmark sets up in the
            same way on all devices for consistency.
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                - wnd (BaseWindow): This is used by ModernGL_window as the display object to
                    use for rendering and additional resource loading.
                    
            - Keyword Args:
                - None

            - Output:
                - texture (ModernGL_window Texture): This texture is rendered to the scene to
                    add additional complexity.
                - mvp (ModernGL_window Shader Attribute): This matrix is used to render the
                    position and rotation of the scene.
                - light (ModernGL_window Shader Attribute): This attribute is used to shade
                    the scene based on the position of the camera.
                - vao (ModernGL VertexArray): This is the scene we render (a cube).
                - timer (float): This is used to keep track of how long this section of the
                    benchmark has been running for, and is used in calculating the rotation
                    of our scene.
                - aspect_ratio (float): This float represents the aspect ratio we want our display
                    to be rendering at.
            """
            wnd.vsync = False
            wnd.samples = 1
            wnd.size = 1280, 720

            if self.platform == "Linux":
                prog = moderngl_window.WindowConfig.load_program(
                    wnd,
                    os.path.join(
                        self.base_folder,
                        ("shaders//benchmark.glsl")))

                scene = moderngl_window.WindowConfig.load_scene(
                    wnd,
                    os.path.join(
                        self.base_folder,
                        ("resources//benchmark resources//Crate.obj")))

                texture = moderngl_window.WindowConfig.load_texture_2d(
                    wnd,
                    os.path.join(
                        self.base_folder,
                        ("resources//benchmark resources//Crate.png")))

            else:
                prog = moderngl_window.WindowConfig.load_program(
                    wnd,
                    os.path.join(
                        self.base_folder,
                        ("shaders\\benchmark.glsl")))

                scene = moderngl_window.WindowConfig.load_scene(
                    wnd,
                    os.path.join(
                        self.base_folder,
                        ("resources\\benchmark resources\\Crate.obj")))

                texture = moderngl_window.WindowConfig.load_texture_2d(
                    wnd,
                    os.path.join(
                        self.base_folder,
                        ("resources\\benchmark resources\\Crate.png")))

            mvp = prog["Mvp"]
            light = prog["Light"]
            vao = scene.root_nodes[0].mesh.vao.instance(prog)

            timer = 0
            aspect_ratio = 16/9
            
            return texture, mvp, light, vao, timer, aspect_ratio

        def start(
                self,
                iteration,
                Setfpslength,
                Setfps,
                fpscounter,
                Maxiteration,
                ctx,
                texture,
                mvp,
                light,
                vao,
                timer,
                aspect_ratio):
            """
            This subroutine is used to render the OpenGL window benchmark, accessible when run
            through the benchmark section of Pycraft. This test is the final of 3 tests designed
            to test different aspects of your hardware. This stresses your GPU as well as your CPU
            and this is often the most difficult benchmark to run. 
            
            - Args:
                - self (dict): This is used by Pycraft as a way of storing it's current
                    configuration and behaviour and is required by most GUIs. Its use should be
                    reduced where possible for readability reasons.
                - iteration (int): In the benchmarking process, iteration is used to keep track of
                    how long the benchmark has been running 
                - Setfpslength (int): This is the length of the 'Setfps' array, we use this instead
                    of specifying an integer in order to allow us to make changes later on in Pycraft's
                    development about how many targets to use for the benchmark section.
                - Setfps (array): This is an array of integers that stores FPS targets for the benchmark
                    section of Pycraft, with each element being a different FPS to try to reach, getting
                    progressively harder. The FPS from this array is updated every 500 iterations of the
                    benchmark.
                - fpscounter (int): This is used to store the index used to calculate the next element in the
                    'Setfps' array, this is used so Pycraft know's what to set the FPS to next, and what to set
                    the caption to so that it displays the current FPS being tested.
                - Maxiteration (int): This is used to calculate after how many iterations we move onto the next
                    targeted FPS, currently this is set to increase the FPS every 500 'iteration's.
                - ctx (Context object): This is used by ModernGL for loading OpenGL resources
                    and enabling access to OpenGL features.
                - texture (ModernGL_window Texture): This texture is rendered to the scene to
                    add additional complexity.
                - mvp (ModernGL_window Shader Attribute): This matrix is used to render the
                    position and rotation of the scene.
                - light (ModernGL_window Shader Attribute): This attribute is used to shade
                    the scene based on the position of the camera.
                - vao (ModernGL VertexArray): This is the scene we render (a cube).
                - timer (float): This is used to keep track of how long this section of the
                    benchmark has been running for, and is used in calculating the rotation
                    of our scene.
                - aspect_ratio (float): This float represents the aspect ratio we want our display
                    to be rendering at.
                    
            - Keyword Args:
                - None

            - Output:
                - fpslistX (array): Used to store the iteration of the benchmark. This correlates to a point, with this
                    making up the X coordinate and 'fpslistY' making up the Y coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
                - fpslistY (array): Used to store the FPS at a given iteration of the benchmark. This correlates to a point, with this
                    making up the Y coordinate and 'fpslistX' making up the X coordinate. These points are later plotted
                    (after a bit of processing) in the benchmark results screen on a line graph.
            """
            fpslistX = []
            fpslistY = []
            start_time = time.perf_counter()
            while iteration < 500*Setfpslength:
                pygame.display.set_caption("".join((f"Pycraft: v{self.version}: ",
                    "benchmark | Running OpenGL benchmark ",
                     f"@ {Setfps[fpscounter]} fps")))
                
                while iteration != Maxiteration:
                    if not self.clock.get_fps() == 0:
                        fpslistX.append(iteration)
                        fpslistY.append(self.clock.get_fps())
                        

                    angle = timer
                    ctx.clear(
                        0.0,
                        0.0,
                        0.0)

                    ctx.enable(moderngl.DEPTH_TEST)

                    camera_pos = (
                        numpy.cos(angle) * 3.0,
                        numpy.sin(angle) * 3.0,
                        2.0)

                    proj = pyrr.Matrix44.perspective_projection(
                        45.0,
                        aspect_ratio,
                        0.1,
                        100.0)

                    lookat = pyrr.Matrix44.look_at(
                        camera_pos,
                        (0.0, 0.0, 0.5),
                        (0.0, 0.0, 1.0),
                    )

                    mvp.write((proj * lookat).astype("f4"))
                    light.value = camera_pos
                    texture.use()
                    vao.render()

                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT or
                            (event.type == pygame.KEYDOWN and
                                (not event.key == pygame.K_SPACE))):

                            benchmark_utils.close_benchmark.Exitbenchmark(self)

                    pygame.display.flip()
                    iteration += 1
                    self.clock.tick(Setfps[fpscounter])

                    timer = time.perf_counter()-start_time
                    
                fpscounter += 1
                Maxiteration += 500
                
            return fpslistX, fpslistY

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