if __name__ != "__main__":
    try:
        import time
        
        import pygame
        import numpy
        import moderngl
        import moderngl_window
        import pyrr
        
        from registry_utils import Registry
        
        import benchmark_utils
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in OpenGL_window_benchmark"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class run_opengl_window_benchmark(Registry):

        def setup(
                wnd):
            wnd.vsync = False
            wnd.samples = 1
            wnd.size = 1280, 720

            benchmark_shader_path = Registry.base_folder / "shaders" / "benchmark.glsl"
            benchmark_scene_path = Registry.base_folder / "resources" / "benchmark resources" / "Crate.obj"
            benchmark_texture_path = Registry.base_folder / "resources" / "benchmark resources" / "Crate.png"

            prog = moderngl_window.WindowConfig.load_program(
                wnd,
                benchmark_shader_path)

            scene = moderngl_window.WindowConfig.load_scene(
                wnd,
                benchmark_scene_path)

            texture = moderngl_window.WindowConfig.load_texture_2d(
                wnd,
                benchmark_texture_path)

            mvp = prog["Mvp"]
            light = prog["Light"]
            vao = scene.root_nodes[0].mesh.vao.instance(prog)

            timer = 0
            aspect_ratio = 16/9
            
            return texture, mvp, light, vao, timer, aspect_ratio

        def start(
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
            
            fpslistX = []
            fpslistY = []
            start_time = time.perf_counter()
            while iteration < 500*Setfpslength:
                pygame.display.set_caption("".join((f"Pycraft: v{Registry.version}: ",
                    "benchmark | Running OpenGL benchmark ",
                     f"@ {Setfps[fpscounter]} fps")))
                
                while iteration != Maxiteration:
                    if not Registry.clock.get_fps() == 0:
                        fpslistX.append(iteration)
                        fpslistY.append(Registry.clock.get_fps())
                        

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

                            benchmark_utils.close_benchmark.exit_benchmark()

                    pygame.display.flip()
                    iteration += 1
                    Registry.clock.tick(Setfps[fpscounter])

                    timer = time.perf_counter()-start_time
                    
                fpscounter += 1
                Maxiteration += 500
                
            return fpslistX, fpslistY

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()