if __name__ != "__main__":
    class create_game_engine:
        def __init__():
            pass

        def game_engine(self):
            try:
                StartLoading = self.mod_time__.perf_counter()
                import moderngl
                import moderngl_window as mlgw
                from moderngl_window.scene.camera import KeyboardCamera
                from moderngl_window import geometry

                self.mod_display_utils__.display_utils.set_display(
                    self, opengl=True)

                def start():
                    ctx = moderngl.create_context(standalone=False)

                    wnd = mlgw.get_local_window_cls("pygame2")

                    mlgw.activate_context(wnd, ctx)

                    return ctx, wnd

                ctx, wnd = start()

                wnd.vsync = False

                converted_theme_col_r = (1/255)*self.background_color[0]
                converted_theme_col_g = (1/255)*self.background_color[1]
                converted_theme_col_b = (
                    1/255)*self.background_color[2]

                ctx.clear(converted_theme_col_r,
                        converted_theme_col_g,
                        converted_theme_col_b)

                self.mod_pygame__.display.flip()

                GameLoadProgressPercent = 10

                if self.aa:
                    samples = int(
                        str(self.aa_quality).split("x")[0])

                else:
                    samples = 1

                wnd.samples = samples

                skybox_distance = 1600

                self.real_window_width = self.mod_pygame__.display.get_window_size()[
                    0]
                self.real_window_height = self.mod_pygame__.display.get_window_size()[
                    1]

                aspect_ratio = self.real_window_width / self.real_window_height

                camera = KeyboardCamera(
                    wnd.keys,
                    aspect_ratio=aspect_ratio,
                    far=2000.0,
                    near=0.1)

                camera_enabled = True

                camera.projection.update(
                    near=1,
                    far=skybox_distance,
                    fov=70)

                wnd.mouse_exclusivity = True

                GameLoadProgressPercent = 20

                # Offscreen buffer
                offscreen_size = 1024, 1024
                offscreen_depth = ctx.depth_texture(offscreen_size)
                offscreen_depth.compare_func = ""
                offscreen_depth.repeat_x = False
                offscreen_depth.repeat_y = False
                # Less ugly by default with linear. May need to be NEAREST for some techniques
                offscreen_depth.filter = (moderngl.LINEAR,
                                          moderngl.LINEAR)

                sun_radius = 50

                sun = geometry.sphere(
                    radius=sun_radius)

                moon = geometry.sphere(
                    radius=80)

                GameLoadProgressPercent = 30

                SkySphere = geometry.sphere(
                    radius=skybox_distance)

                objects: self.mod_typing__.Dict[
                    str,
                    moderngl.VertexArray] = {}

                objects_shadow: self.mod_typing__.Dict[
                    str,
                    moderngl.VertexArray] = {}

                if self.platform == "Linux":
                    # Use 'u' to do things with UVs that this really needs
                    scene: mlgw.scene.Scene = mlgw.WindowConfig.load_scene(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//game engine resources//map//map2.obj")),
                        cache=True)
                else:
                    scene: mlgw.scene.Scene = mlgw.WindowConfig.load_scene(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\game engine resources\\map\\map.obj")),
                        cache=True)

                GameLoadProgressPercent = 40

                if self.platform == "Linux":
                    SkyBox_texture_Sun = mlgw.WindowConfig.load_texture_array(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//game engine resources//skysphere//ClearSkyTransition.gif")),
                        anisotropy=samples)

                else:
                    SkyBox_texture_Sun = mlgw.WindowConfig.load_texture_array(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\game engine resources\\skysphere\\ClearSkyTransition.gif")),
                        anisotropy=samples)

                GameLoadProgressPercent = 50

                # Programs
                CloudsProgram, depth_prog, shadowmap, sun_prog, moon_prog, skysphere_prog, particles_screen = self.mod_game_engine_utils__.LoadPrograms.LoadProgramFiles(
                    self, wnd)

                particles_transform, gpu_emitter_particles = self.mod_game_engine_utils__.LoadPrograms.LoadProgramText(
                    self, ctx)
                
                GameLoadProgressPercent = 60

                vao = scene.root_nodes[0].mesh.vao
                objects["map"] = vao.instance(shadowmap)
                objects_shadow["map"] = vao.instance(depth_prog)

                skysphere_prog["texture0"].value = 0
                skysphere_prog["num_layers"].value = 41.0

                # affects the velocity of the particles over time
                # grav?
                particles_transform["gravity"].value = -.005
                ctx.point_size = 2  # point size

                if self.fancy_particles:
                    N = 5_000  # particle count

                else:
                    N = 2_500

                # Initial / current number of active particles
                active_particles = N // 100
                # Maximum number of particles to emit per frame
                max_emit_count = N // 100
                stride = 28  # byte stride for each vertex
                floats = 7
                # Note that passing dynamic=True probably doesn't mean
                # anything to most drivers today
                try:
                    vbo1 = ctx.buffer(
                        reserve=N * stride)
                    vbo2 = ctx.buffer(
                        reserve=N * stride)

                except Exception as Message:
                    log_message = "GameEngine > GameEngine > __init__: " + \
                        str(Message)

                    self.mod_logging_utils__.create_log_message.update_log_warning(
                        self,
                        log_message)

                    vbo1 = self.ctx.buffer(
                        reserve=N * stride, dynamic=True)
                    vbo2 = self.ctx.buffer(
                        reserve=N * stride, dynamic=True)

                # Write some initial particles
                vbo1.write(
                    self.mod_numpy__.fromiter(
                        self.mod_game_engine_utils__.Particles.gen_particles(
                            self,
                            active_particles),

                        count=active_particles * floats, dtype="f4"))

                # Transform vaos. We transform data back and forth to avoid buffer copy
                transform_vao1 = ctx.vertex_array(
                    particles_transform,
                    [(vbo1, "2f 2f 3f", "in_pos", "in_vel", "in_color")],
                )
                transform_vao2 = ctx.vertex_array(
                    particles_transform,
                    [(vbo2, "2f 2f 3f", "in_pos", "in_vel", "in_color")],
                )

                # Render vaos. The render to screen version of the tranform vaos above
                render_vao1 = ctx.vertex_array(
                    particles_screen,
                    [(vbo1, "2f 2x4 3f", "in_pos", "in_color")],
                )
                render_vao2 = ctx.vertex_array(
                    particles_screen,
                    [(vbo2, "2f 2x4 3f", "in_pos", "in_color")],
                )

                # The emit buffer size is only max_emit_count.
                emit_buffer_elements = max_emit_count

                gpu_emitter_vao = ctx._vertex_array(
                    gpu_emitter_particles, [])

                # Query object to inspect render calls
                query = ctx.query(primitives=True)

                # Cycle emit methods per frame
                particles_screen["projection"].write(
                    self.mod_pyrr_matrix44_.create_orthogonal_projection(
                        -aspect_ratio, aspect_ratio,
                        -1, 1,
                        -1, 100,
                        dtype='f4',)
                )

                shadowmap["u_sampler_shadow"].value = 0
                shadowmap["grass_color"].value = 1
                shadowmap["rock_color"].value = 2

                shadowmap["light_level"] = 0.5

                mvp = (shadowmap["projection_matrix"], shadowmap["matrix"])
                mvp_depth = (shadowmap["bias_matrix"], shadowmap["mvp_light"])

                light = shadowmap["u_light"]
                color = shadowmap["u_color"]

                mvp_shadow = depth_prog["u_mvp"]

                sun_prog["color"].value = (1.0, 1.0, 0.0, 1.0)
                moon_prog["color"].value = (1.0, 1.0, 1.0, 1.0)

                color.value = (1.0, 1.0, 1.0)

                GameLoadProgressPercent = 70

                if self.platform == "Linux":
                    tex1 = mlgw.WindowConfig.load_texture_2d(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//game engine resources//map//GrassTexture.png")),
                        mipmap=True,
                        anisotropy=samples)

                    tex2 = mlgw.WindowConfig.load_texture_2d(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//game engine resources//map//RockTexture.png")),
                        mipmap=True,
                        anisotropy=samples)

                else:
                    tex1 = mlgw.WindowConfig.load_texture_2d(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\game engine resources\\map\\GrassTexture.png")),
                        mipmap=True,
                        anisotropy=samples)

                    tex2 = mlgw.WindowConfig.load_texture_2d(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\game engine resources\\map\\RockTexture.png")),
                        mipmap=True,
                        anisotropy=samples)

                tex1.use(location=1)
                tex2.use(location=2)

                SHADOW_SIZE: self.mod_typing_Final[int] = 2 << 7

                shadow_size = (SHADOW_SIZE,
                               SHADOW_SIZE,)

                GameLoadProgressPercent = 80

                tex_depth = ctx.depth_texture(shadow_size)

                sampler_depth = ctx.sampler(
                    filter=(self.mod_ModernGL__.LINEAR,
                            self.mod_ModernGL__.LINEAR),
                    compare_func=">=",
                    repeat_x=False,
                    repeat_y=False,)

                z = 1000
                size = (z, z)

                CloudData = self.mod_game_engine_utils__.ComputeWeather.ComputeCloudNoise(
                    self,
                    size)

                range = self.mod_numpy__.max(
                    CloudData) - self.mod_numpy__.min(CloudData)

                CloudsProgram["CloudHeight"] = 500.0
                CloudsProgram["height_max"] = range
                CloudsProgram["render_fog"] = self.render_fog

                shadowmap["render_fog"] = self.render_fog

                vertices, index = self.mod_game_engine_utils__.ComputeWeather.ComputeCloudModel(
                    self,
                    size[0])

                vbo = ctx.buffer(vertices.astype("f4"))
                ibo = ctx.buffer(index.astype("i4"))

                cloud_vao_content = [(
                    vbo,
                    "2f",
                    "in_vert"), ]

                vao = ctx.vertex_array(
                    CloudsProgram,
                    cloud_vao_content,
                    ibo)

                if self.platform == "Linux":
                    cloud_texture = mlgw.WindowConfig.load_texture_2d(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources//game engine resources//clouds//Rnd_noise.png")),
                        anisotropy=samples)

                else:
                    cloud_texture = mlgw.WindowConfig.load_texture_2d(
                        wnd,
                        path=self.mod_OS__.path.join(
                            self.base_folder,
                            ("resources\\game engine resources\\clouds\\Rnd_noise.png")),
                        anisotropy=samples)

                GameLoadProgressPercent = 90

                OnStart = True

                frametime = 1

                Inventory = False
                Map = False

                Time_Percent = 0

                day = 1

                total_move_x = 0
                total_move_y = 0
                total_move_z = 0

                timer = 0

                GameTime = 0

                play_time = 0

                WeatherDelta = 1
                DefaultSkyCol = 1.0

                LengthenStorm, weather, CloudHeightMultiplier, skysphere_prog_Transparency = self.mod_game_engine_utils__.ComputeWeather.ComputeWeather(
                    self,
                    color,
                    shadowmap,
                    CloudsProgram,
                    skysphere_prog,
                    Time_Percent)

                weather_change = True

                WeatherTime = 0
                Thundertimer = 0
                Lightningtimer = 0
                show_strobe_effects = False

                Thundertimer_Target = self.mod_random__.randint(
                    15, 30)

                switchWeather = self.mod_random__.randint(60, 120)

                Flashtimer = 0
                ShowFlash = False
                LengthenStorm = False
                PreviousWeather = weather

                target = self.mod_numpy__.array((0, 0, 0), dtype="f4")

                up = self.mod_numpy__.array((0, 0, 1), dtype="f4")

                camera_up = self.mod_numpy__.array((0, 1, 0), dtype="f4")

                scene_pos = self.mod_numpy__.array((0, -5, -32), dtype="f4")

                scene_translation = self.mod_pyrr_Matrix44_.from_translation(
                    (0.0, 0.0, 0.0),
                    dtype="f4")

                bias_matrix = (
                    self.mod_pyrr_Matrix44_.from_translation(
                        (0.5, 0.5, 0.5),
                        dtype="f4")
                    *
                    self.mod_pyrr_Matrix44_.from_scale(
                        (0.5, 0.5, 0.5),
                        dtype="f4")
                )

                orthogonal_perspective = self.mod_pyrr_matrix44_.create_orthogonal_projection(
                    -aspect_ratio, aspect_ratio,
                    -1, 1,
                    -1, 100,
                    dtype='f4',)

                Previous_Fog_Distance_Min = shadowmap["w_min"].value
                Previous_Fog_Distance_Max = shadowmap["w_max"].value

                Previous_color = color.value[0]

                Previous_CloudsProgram_Alpha = CloudsProgram["WeatherAlpha"].value
                Previous_CloudsProgram_CloudColor = CloudsProgram["CloudColor"].value

                Previous_multiplier = CloudsProgram["CloudHeightMultiplier"].value

                Previous_prog_transparency = skysphere_prog["transparency"].value

                if self.music:
                    if self.mod_pygame__.mixer.music.get_busy():
                        self.mod_pygame__.mixer.music.pause()

                GameLoadProgressPercent = 100

                camera_enabled = True

                self.display.set_alpha(False)

                # Direction Definitions
                RIGHT = 1
                LEFT = 2
                FORWARD = 3
                BACKWARD = 4
                UP = 5
                DOWN = 6

                # Movement Definitions
                STILL = 0
                POSITIVE = 1
                NEGATIVE = 2

                direction_args = (RIGHT, LEFT, FORWARD, BACKWARD, UP, DOWN)
                movement_args = (STILL, POSITIVE, NEGATIVE)

                jump = False
                start_jumping = False
                collision = False
                increased_speed = False
                modifier = 20
                increase_speed = False
                base_camera_velocity = camera.velocity

                projection = self.mod_game_engine_utils__.compiled_math_functions.perspective_fov(
                    70, aspect_ratio, 1, skybox_distance)

                game_starts_running = self.mod_time__.perf_counter()
                        
                while True:
                    # 250 is base FPS w/ shadowmapping
                    # 205 is avg w/ shadowmapping + dynamic skybox

                    matrix, position = self.mod_game_engine_utils__.compute_camera.get_camera_values(
                        self, camera, camera_up, *movement_args)

                    '''if Inventory or Map:
                        self.mod_game_engine_utils__.AccessOtherGUIs.AccessGUI(
                            self, Inventory, Map)'''
                        
                    ctx.clear(DefaultSkyCol, DefaultSkyCol, DefaultSkyCol)
                    dx, dy = self.mod_pygame__.mouse.get_rel()

                    if camera_enabled:
                        camera.rot_state(
                            -dx,
                            -dy)

                    self.real_window_width = self.mod_pygame__.display.get_window_size()[0]
                    self.real_window_height = self.mod_pygame__.display.get_window_size()[1]

                    aspect_ratio = self.real_window_width / self.real_window_height

                    for event in self.mod_pygame__.event.get():
                        if (event.type == self.mod_pygame__.QUIT or
                                (event.type == self.mod_pygame__.KEYDOWN and
                                    event.key == self.input_key[self.input_configuration["keyboard"]["Back"]][0])):

                            self.mod_pygame__.event.set_grab(False)
                            self.mod_pygame__.mouse.set_visible(True)

                            return

                        if event.type == self.mod_pygame__.KEYDOWN:
                            if event.key == self.input_key[self.input_configuration["keyboard"]["Walk forwards"]][0]:
                                self.mod_game_engine_utils__.compute_camera.camera_move_state(
                                    camera,
                                    FORWARD,
                                    True,
                                    *direction_args,
                                    *movement_args)
                                
                            if event.key == self.input_key[self.input_configuration["keyboard"]["Walk backwards"]][0]:
                                self.mod_game_engine_utils__.compute_camera.camera_move_state(
                                    camera,
                                    BACKWARD,
                                    True,
                                    *direction_args,
                                    *movement_args)
                                
                            if event.key == self.input_key[self.input_configuration["keyboard"]["Walk left"]][0]:
                                self.mod_game_engine_utils__.compute_camera.camera_move_state(
                                    camera,
                                    LEFT,
                                    True,
                                    *direction_args,
                                    *movement_args)
                                
                            if event.key == self.input_key[self.input_configuration["keyboard"]["Walk right"]][0]:
                                self.mod_game_engine_utils__.compute_camera.camera_move_state(
                                    camera,
                                    RIGHT,
                                    True,
                                    *direction_args,
                                    *movement_args)
                            
                            if event.key == self.input_key[self.input_configuration["keyboard"]["Unlock mouse"]][0]:
                                self.mod_pygame__.event.set_grab(not self.mod_pygame__.event.get_grab())
                                self.mod_pygame__.mouse.set_visible(not self.mod_pygame__.event.get_grab())

                                camera_enabled = not camera_enabled

                            if event.key == self.input_key[self.input_configuration["keyboard"]["Toggle full-screen"]][0]:
                                self.mod_display_utils__.display_utils.update_display(self, opengl=True)

                                ctx.viewport = (0, 0, *self.mod_pygame__.display.get_window_size())

                            if event.key == self.input_key[self.input_configuration["keyboard"]["Jump"]][0] and jump is False:
                                start_jumping = True

                            if event.key == self.input_key[self.input_configuration["keyboard"]["Skip time"]][0] and self.skip_time:
                                timer += 30
                                GameTime += 30
                                WeatherTime += 30

                            if event.key == self.input_key[self.input_configuration["keyboard"]["List variables"]][0] and self.extended_developer_options:
                                self.mod_tkinter_utils__.TkinterInfo.CreateTkinterWindow(
                                    self)

                            if event.key == self.input_key[self.input_configuration["keyboard"]["Increase speed"]][0] and self.increased_speed:
                                increase_speed = True

                            if event.key == self.input_key[self.input_configuration["keyboard"]["Open inventory"]][0]:
                                Inventory = True

                            if event.key == self.input_key[self.input_configuration["keyboard"]["Open map"]][0]:
                                Map = True

                        elif event.type == self.mod_pygame__.KEYUP:
                            if event.key == self.input_key[self.input_configuration["keyboard"]["Walk forwards"]][0]:
                                self.mod_game_engine_utils__.compute_camera.camera_move_state(
                                    camera,
                                    FORWARD,
                                    False,
                                    *direction_args,
                                    *movement_args)
                                
                            if event.key == self.input_key[self.input_configuration["keyboard"]["Walk backwards"]][0]:
                                self.mod_game_engine_utils__.compute_camera.camera_move_state(
                                    camera,
                                    BACKWARD,
                                    False,
                                    *direction_args,
                                    *movement_args)
                                
                            if event.key == self.input_key[self.input_configuration["keyboard"]["Walk left"]][0]:
                                self.mod_game_engine_utils__.compute_camera.camera_move_state(
                                    camera,
                                    LEFT,
                                    False,
                                    *direction_args,
                                    *movement_args)
                                
                            if event.key == self.input_key[self.input_configuration["keyboard"]["Walk right"]][0]:
                                self.mod_game_engine_utils__.compute_camera.camera_move_state(
                                    camera,
                                    RIGHT,
                                    False, 
                                    *direction_args,
                                    *movement_args)

                            if event.key == self.input_key[self.input_configuration["keyboard"]["Jump"]][0]:
                                start_jumping = False

                            if event.key == self.input_key[self.input_configuration["keyboard"]["Increase speed"]][0]:
                                increase_speed = False

                    if increase_speed:
                        camera.velocity = base_camera_velocity * modifier

                    else:
                        base_camera_velocity

                    if start_jumping and jump is False:
                        jump = True
                        jump_timer = self.mod_time__.perf_counter()
                        jump_starting_y_pos = camera.position.y

                    if jump:
                        current_time = self.mod_time__.perf_counter()
                        delta = current_time - jump_timer
                        offset = delta*180
                        offset_radians = self.mod_math__.radians(offset)

                        if increased_speed:
                            calculation = jump_starting_y_pos + (self.mod_math__.sin(
                                offset_radians) / (2 / modifier))

                        else:
                            calculation = jump_starting_y_pos + (self.mod_math__.sin(
                                offset_radians) / 2)

                        camera.position.y = calculation
                        if delta > 1:
                            jump = False
                            if collision == False:
                                camera.position.y = jump_starting_y_pos

                    if WeatherTime >= switchWeather:
                        switchWeather = self.mod_random__.randint(
                            60, 120)
                        WeatherTime = 0
                        WeatherDelta += 1
                        weather_change = True

                        Previous_Fog_Distance_Min = shadowmap["w_min"].value
                        Previous_Fog_Distance_Max = shadowmap["w_max"].value

                        Previous_color = color.value[0]

                        Previous_CloudsProgram_Alpha = CloudsProgram["WeatherAlpha"].value
                        Previous_CloudsProgram_CloudColor = CloudsProgram["CloudColor"].value

                        Previous_multiplier = CloudsProgram["CloudHeightMultiplier"].value

                        Previous_prog_transparency = skysphere_prog["transparency"].value

                        LengthenStorm, weather, CloudHeightMultiplier, skysphere_prog_Transparency = self.mod_game_engine_utils__.ComputeWeather.ComputeWeather(
                            self,
                            color,
                            shadowmap,
                            CloudsProgram,
                            skysphere_prog,
                            Time_Percent)

                    if weather_change and OnStart is False:
                        weather_change = False
                        if weather != "sunny":
                            self.mod_pygame__.mixer.Channel(4).unpause()
                            if weather == "rain.light":
                                RandomiseVolumeReduction = self.mod_random__.randint(
                                    2, 5)

                                self.mod_pygame__.mixer.Channel(2).set_volume(
                                    (self.sound_volume/100)/RandomiseVolumeReduction)

                                self.mod_pygame__.mixer.Channel(4).set_volume(
                                    (((self.sound_volume/100)*10)/100))

                            else:
                                self.mod_pygame__.mixer.Channel(2).pause()
                                if weather == "rain.heavy.thundery":
                                    self.mod_pygame__.mixer.Channel(4).set_volume(
                                        (((self.sound_volume/100)*30)/100)
                                    )

                                else:
                                    self.mod_pygame__.mixer.Channel(4).set_volume(
                                        (((self.sound_volume/100)*20)/200)
                                    )

                        else:
                            self.mod_pygame__.mixer.Channel(4).pause()
                            self.mod_pygame__.mixer.Channel(2).set_volume(
                                self.sound_volume/100)

                            self.mod_pygame__.mixer.Channel(2).unpause()

                    self.eFPS = self.clock.get_fps()
                    self.aFPS += self.eFPS
                    self.iteration += 1

                    if self.detailed_captions:
                        self.mod_caption_utils__.generate_captions.setOpenGLCaption(
                            self,
                            play_time,
                            Time_Percent,
                            day,
                            total_move_x,
                            total_move_y,
                            total_move_z,
                            weather)

                    total_move_x = 0
                    total_move_y = 0
                    total_move_z = 0

                    try:
                        if (self.mod_pygame__.mixer.Channel(2).get_busy() is False and
                                self.sound and
                                OnStart is False):

                            self.mod_sound_utils__.play_sound.play_ambient_sound(
                                self)

                    except Exception as Message:
                        self.error_message = "".join(("GameEngine > GameEngine ",
                                                      f"> __init__: {str(Message)}"))

                        self.error_message_detailed = "".join(
                            self.mod_traceback__.format_exception(
                                None,
                                Message,
                                Message.__traceback__))

                        self.mod_error_utils__.generate_error_screen.error_screen(
                            self)

                    try:
                        if (self.mod_pygame__.mixer.Channel(4).get_busy() is False and
                                self.sound and
                                weather != "sunny" and
                                OnStart is False):

                            self.mod_sound_utils__.play_sound.play_rain_sound(
                                self)

                    except Exception as Message:
                        self.error_message = "".join(("GameEngine > GameEngine ",
                                                      f"> __init__: {str(Message)}"))

                        self.error_message_detailed = "".join(
                            self.mod_traceback__.format_exception(
                                None,
                                Message,
                                Message.__traceback__))

                        self.mod_error_utils__.generate_error_screen.error_screen(
                            self)

                    Time_Percent = ((100/1056)*(GameTime))

                    GameTime, day, sun_lightpos, moon_lightpos = self.mod_game_engine_utils__.ShadowmappingMathematics.ComputeCelestialEntities(
                        self,
                        skybox_distance,
                        sun_radius,
                        GameTime,
                        day,
                        sun_prog,
                        moon_prog,
                        scene_pos,
                        projection,
                        matrix,
                        position)  # slow

                    ctx.enable(
                        self.mod_ModernGL__.DEPTH_TEST |
                        self.mod_ModernGL__.CULL_FACE)

                    self.mod_game_engine_utils__.ShadowmappingMathematics.ComputeShadows(
                        self,
                        mvp,
                        light,
                        sun_lightpos,
                        aspect_ratio,
                        mvp_depth,
                        mvp_shadow,
                        bias_matrix,
                        projection,
                        matrix,
                        target,
                        up)  # slowest

                    # --- PASS 2: Render scene to screen
                    cam = matrix
                    x = int(position.x*100)/100
                    y = int(position.y*100)/100
                    z = int(position.z*100)/100
                    cam[3][0] = 0
                    cam[3][1] = 0
                    cam[3][2] = 0
                    skysphere_prog["m_proj"].write(
                        projection)
                    skysphere_prog["m_model"].write(scene_translation)
                    skysphere_prog["m_camera"].write(cam)

                    particles_screen["projection"].write(
                        orthogonal_perspective)

                    if Time_Percent < 40:  # day
                        skysphere_prog["time"].value = 0
                        DefaultSkyCol = 1.0

                    elif Time_Percent < 50:  # sunset
                        DefaultSkyCol = 1 - \
                            ((0.7/10)*(Time_Percent-40))
                        skysphere_prog["time"].value = (
                            (19/10)*(Time_Percent-40))+1

                    elif Time_Percent < 90:  # night
                        skysphere_prog["time"].value = 21
                        DefaultSkyCol = 0.3

                    else:  # sunrise
                        DefaultSkyCol = 1 - \
                            ((0.7/10)*(100-Time_Percent))
                        skysphere_prog["time"].value = 21 - \
                            (((21/10)*(Time_Percent-90)))

                    CloudsProgram["DefaultSkyCol"] = DefaultSkyCol

                    ctx.front_face = "cw"

                    self.mod_game_engine_utils__.ComputeWeather.BlendWeather(
                        self,
                        weather,
                        PreviousWeather,
                        WeatherTime,
                        shadowmap,
                        Previous_Fog_Distance_Min,
                        Previous_Fog_Distance_Max,
                        Previous_color,
                        color,
                        CloudsProgram,
                        Previous_CloudsProgram_Alpha,
                        Previous_CloudsProgram_CloudColor,
                        Previous_multiplier,
                        CloudHeightMultiplier,
                        skysphere_prog,
                        Previous_prog_transparency,
                        skysphere_prog_Transparency)

                    if Thundertimer > Thundertimer_Target and OnStart is False:
                        Thundertimer_Target = self.mod_random__.randint(
                            5, 30)
                        Thundertimer = 0
                        Flashtimer = 0
                        Lightningtimer = 0

                        if show_strobe_effects:
                            color.value = (1.0, 1.0, 1.0)

                        show_strobe_effects = True
                        ShowFlash = True
                        if self.sound:
                            self.mod_sound_utils__.play_sound.play_thunder_sound(
                                self)

                    if weather == "rain.heavy.thundery":
                        LightningDelay = self.mod_random__.randint(
                            30, 75)/100

                        if (Lightningtimer > LightningDelay and
                                show_strobe_effects):

                            Flashtimer = 0
                            DefaultSkyCol = 1
                            Lightningtimer = 0
                            show_strobe_effects = False
                            ShowFlash = True

                    if ShowFlash:
                        if Flashtimer <= 1/60:
                            DefaultSkyCol = 1
                            if show_strobe_effects:
                                color.value = (1.0, 1.0, 1.0)
                        else:
                            ShowFlash = False

                    if weather != "sunny":
                        ctx.enable(self.mod_ModernGL__.BLEND)

                    SkyBox_texture_Sun.use(location=0)
                    SkySphere.render(skysphere_prog)

                    if weather != "sunny":
                        ctx.disable(self.mod_ModernGL__.BLEND)

                    ctx.front_face = "ccw"

                    # pass 5: Render the sun position
                    moon.render(moon_prog)
                    sun.render(sun_prog)

                    ctx.front_face = "cw"

                    if weather != "sunny":
                        particles_transform["ft"].value = frametime

                        active_particles = self.mod_game_engine_utils__.Particles.emit_gpu(
                            self,
                            query,
                            transform_vao1,
                            vbo2,
                            N,
                            emit_buffer_elements,
                            max_emit_count,
                            gpu_emitter_particles,
                            weather,
                            timer,
                            gpu_emitter_vao,
                            stride,
                            render_vao2,
                            active_particles)

                    CloudPos = self.mod_pyrr_Vector3_(
                        (position.x,
                            0,
                            position.z),
                        dtype="f4")

                    CloudsProgram["m_proj"].write(
                        projection)

                    CloudsProgram["m_camera"].write(matrix)

                    CloudsProgram["m_model"].write(
                        self.mod_pyrr_Matrix44_.from_translation(
                            CloudPos,
                            dtype="f4"))

                    # shadows, variable rendering maybe
                    CloudsProgram["X_Offset"] = self.mod_math__.sin(
                        timer/50)/10
                    CloudsProgram["Y_Offset"] = self.mod_math__.cos(
                        timer/50)/10

                    cloud_texture.use(location=0)

                    ctx.enable(self.mod_ModernGL__.BLEND)

                    vao.render(
                        mode=self.mod_ModernGL__.TRIANGLE_STRIP)

                    ctx.blend_func = self.mod_ModernGL__.DEFAULT_BLENDING

                    # pass 2: render the scene and retro project depth shadow-map
                    # counter clock wise -> render front faces

                    sampler_depth.use(location=0)
                    tex_depth.use(location=0)
                    cloud_texture.use(location=0)

                    ctx.front_face = "ccw"

                    # pass 4: render textured scene with shadow

                    objects["map"].render()
                    ctx.disable(self.mod_ModernGL__.BLEND)

                    if weather == "rain.heavy.thundery" and LengthenStorm and weather_change:
                        switchWeather = switchWeather * (self.mod_random__.randint(
                            15,
                            30)/10)
                        LengthenStorm = False

                    if OnStart:
                        OnStart = False

                        self.mod_pygame__.event.set_grab(True)
                        self.mod_pygame__.mouse.set_visible(False)

                        GameEngine_Initialisation = False

                        Currentload_time = self.mod_time__.perf_counter()-StartLoading
                        self.load_time = [
                            self.load_time[0] + Currentload_time,
                            self.load_time[1] + 1]

                    # Swap around objects for next frame
                    self.mod_pygame__.display.flip()
                    self.clock.tick(75)

                    if weather != "sunny":
                        transform_vao1, transform_vao2 = transform_vao2, transform_vao1
                        render_vao1, render_vao2 = render_vao2, render_vao1
                        vbo1, vbo2 = vbo2, vbo1

                    frametime = self.clock.get_time() / 1000
                    timer = self.mod_time__.perf_counter() - game_starts_running
                    GameTime += frametime
                    WeatherTime += frametime

                    if weather == "rain.heavy.thundery":
                        if self.mod_pygame__.mixer.Channel(3).get_busy() is False:
                            Thundertimer += frametime

                        Lightningtimer += frametime
                        Flashtimer += frametime

                    play_time = timer

            except Exception as Message:
                print(Message)
                self.error_message = (
                    f"pygame_game > create_game_engine > game_engine: {str(Message)}")

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.generate_error_screen.error_screen(self)