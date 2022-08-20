if __name__ != "__main__":
    print("Started <Pycraft_GameEngineUtils>")

    class Crash:
        def __init__(self):
            pass

        def CreateReport(self, Message):
            print(Message, "".join(
                self.shared_data.mod_traceback__.format_exception(
                    None,
                    Message,
                    Message.__traceback__)))

            try:
                self.wnd.close()
                self.shared_data.error_message = "".join(("GameEngine > GameEngine ",
                                                        f"> __init__: {str(Message)}"))

                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                    self.shared_data)

            except Exception as Message2:
                try:
                    self.shared_data.error_message = "".join(("GameEngine > GameEngine ",
                                                            f"> __init__: {str(Message2)}"))

                    self.shared_data.error_message_detailed = "".join(
                        self.shared_data.mod_traceback__.format_exception(
                            None,
                            Message2,
                            Message2.__traceback__))

                    self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                        self.shared_data)
                except:
                    print(Message)
                    print(Message2)

    class LoadPrograms:
        def __init__(self):
            pass

        def LoadProgramText(self):
            self.particles_transform = self.ctx.program(
                vertex_shader='''
                    #version 330

                    in vec2 in_pos;
                    in vec2 in_vel;
                    in vec3 in_color;

                    out vec2 vs_vel;
                    out vec3 vs_color;

                    void main() {
                        gl_Position = vec4(in_pos, 1.0, 1.0);
                        vs_vel = in_vel;
                        vs_color = in_color;
                    }
                    ''',
                geometry_shader='''
                    #version 330

                    layout(points) in;
                    layout(points, max_vertices = 1) out;

                    uniform float gravity;
                    uniform float ft;

                    in vec2 vs_vel[1];
                    in vec3 vs_color[1];

                    out vec2 out_pos;
                    out vec2 out_vel;
                    out vec3 out_color;

                    void main() {
                        vec2 pos = gl_in[0].gl_Position.xy;
                        vec2 velocity = vs_vel[0];

                        if (pos.y > -1.0) {
                            vec2 vel = velocity + vec2(0.0, gravity);
                            out_pos = pos + vel * ft;
                            out_vel = vel;
                            if (out_pos.x == 0.0) {
                                out_pos.y = -1.1;
                            }
                            out_color = vs_color[0];
                            EmitVertex();
                            EndPrimitive();
                        }
                    }
                    ''',
                varyings=['out_pos', 'out_vel', 'out_color'],
            )

            self.gpu_emitter_particles = self.ctx.program(
                vertex_shader='''
                    # version 330
                    #define M_PI 3.1415926535897932384626433832795
                    uniform vec2 mouse_pos;
                    uniform vec2 mouse_vel;
                    uniform float time;

                    out vec2 out_pos;
                    out vec2 out_vel;
                    out vec3 out_color;

                    float rand(float n){
                        return fract(sin(n) * 43758.5453123);
                        }

                    void main() {
                        float a = mod(time * gl_VertexID, M_PI * 2.0);
                        float r = clamp(rand(time + gl_VertexID), 0.1, 0.9);
                        out_pos = mouse_pos;
                        out_vel = vec2(sin(a), cos(a)) * r + mouse_vel;
                        out_color = vec3(0.0, 0.0, rand(time * 2.0 + gl_VertexID));
                    }
                    ''',
                varyings=['out_pos', 'out_vel', 'out_color'],
            )

        def LoadProgramFiles(self):
            if self.shared_data.platform == "Linux":
                self.CloudsProgram = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs//clouds.glsl")))

                self.depth_prog = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs//raw_depth.glsl")))

                self.shadowmap = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs//shadowmap.glsl")))

                self.sun_prog = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs//orbital_prog.glsl")))

                self.moon_prog = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs//orbital_prog.glsl")))

                self.skysphere_prog = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs//skysphere.glsl")))

                self.particles_screen = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs//particles_screen.glsl")))

            else:
                self.CloudsProgram = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs\\clouds.glsl")))

                self.depth_prog = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs\\raw_depth.glsl")))

                self.shadowmap = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs\\shadowmap.glsl")))

                self.sun_prog = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs\\orbital_prog.glsl")))

                self.moon_prog = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs\\orbital_prog.glsl")))

                self.skysphere_prog = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs\\skysphere.glsl")))

                self.particles_screen = self.load_program(
                    self.shared_data.mod_OS__.path.join(
                        self.shared_data.base_folder,
                        ("programs\\particles_screen.glsl")))

    class Particles:
        def __init__(self):
            pass

        def emit_gpu(self, time, frame_time):
            """
            Emit new particles using a shader.
            """
            # Transform all particles recoding how many elements were emitted by geometry shader
            with self.query:
                self.transform_vao1.transform(
                    self.vbo2,
                    self.shared_data.mod_ModernGL__.POINTS,
                    vertices=self.active_particles)

            emit_count = min(self.N - self.query.primitives,
                             self.emit_buffer_elements,
                             self.max_emit_count)

            if emit_count > 0:
                self.gpu_emitter_particles["mouse_pos"].value = (0, 2)

                if self.weather == "rain.light":
                    self.gpu_emitter_particles["mouse_vel"].value = (
                        0,
                        self.shared_data.mod_random__.randint(50, 100)/100)

                if self.weather == "rain.heavy":
                    self.gpu_emitter_particles["mouse_vel"].value = (
                        0,
                        self.shared_data.mod_random__.randint(75, 125)/100)

                if self.weather == "rain.heavy.thundery":
                    self.gpu_emitter_particles["mouse_vel"].value = (
                        0,
                        self.shared_data.mod_random__.randint(75, 150)/100)

                self.gpu_emitter_particles["time"].value = max(time, 0)
                self.gpu_emitter_vao.transform(
                    self.vbo2,
                    vertices=emit_count,
                    buffer_offset=self.query.primitives * self.stride)

            self.active_particles = self.query.primitives + emit_count
            self.render_vao2.render(
                self.shared_data.mod_ModernGL__.POINTS, vertices=self.active_particles)

        def gen_particles(self, n):
            for _ in range(n):
                # Current mouse position (2 floats)
                yield 0
                yield 2
                # Random velocity (2 floats)
                a = self.shared_data.mod_numpy__.random.uniform(
                    0.0, self.shared_data.mod_numpy__.pi * 2.0)
                r = self.shared_data.mod_numpy__.random.uniform(0.1, 0.9)
                yield self.shared_data.mod_numpy__.cos(a) * r + 0
                yield self.shared_data.mod_numpy__.sin(a) * r + 0
                # Random color (4 floats)
                yield 0.0
                yield 0.0
                yield self.shared_data.mod_numpy__.random.uniform(0.0, 1.0)
                #yield self.shared_data.mod_numpy__.random.uniform(0.0, 1.0)

        def projection(self):
            return self.shared_data.mod_pyrr_matrix44_.create_orthogonal_projection(
                -self.wnd.aspect_ratio, self.wnd.aspect_ratio,
                -1, 1,
                -1, 100,
                dtype='f4',
            )

    class ComputeWeather:
        # 0 = transparent
        # 1 = opaque
        def __init__(self):
            pass

        def ComputeCloudModel(self, size):
            try:
                vertices = self.shared_data.mod_numpy__.dstack(
                    self.shared_data.mod_numpy__.mgrid[0:size, 0:size][::-1]) / size

                temp = self.shared_data.mod_numpy__.dstack(
                    [self.shared_data.mod_numpy__.arange(0, size * size - size),
                    self.shared_data.mod_numpy__.arange(size, size * size)])

                index = self.shared_data.mod_numpy__.pad(
                    temp.reshape(size - 1, 2 * size),
                    [[0, 0], [0, 1]],
                    "constant",
                    constant_values=-1)

                return vertices, index
            except Exception as Message:
                self.shared_data.error_message = "".join(("GameEngineUtils > ComputeWeather ",
                                                        f"> ComputeCloudModel: {str(Message)}"))

                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                    self.shared_data)

        def generate_perlin_noise_2d(self, shape, res):
            def f(t):
                return 6*t**5 - 15*t**4 + 10*t**3

            delta = (res[0] / shape[0], res[1] / shape[1])
            d = (shape[0] // res[0], shape[1] // res[1])
            grid = self.shared_data.mod_numpy__.mgrid[0:res[0]:delta[0],0:res[1]:delta[1]].transpose(1, 2, 0) % 1
            # Gradients
            angles = 2*self.shared_data.mod_numpy__.pi*self.shared_data.mod_numpy__.random.rand(res[0]+1, res[1]+1)
            gradients = self.shared_data.mod_numpy__.dstack((self.shared_data.mod_numpy__.cos(angles), self.shared_data.mod_numpy__.sin(angles)))
            g00 = gradients[0:-1,0:-1].repeat(d[0], 0).repeat(d[1], 1)
            g10 = gradients[1:,0:-1].repeat(d[0], 0).repeat(d[1], 1)
            g01 = gradients[0:-1,1:].repeat(d[0], 0).repeat(d[1], 1)
            g11 = gradients[1:,1:].repeat(d[0], 0).repeat(d[1], 1)
            # Ramps
            n00 = self.shared_data.mod_numpy__.sum(grid * g00, 2)
            n10 = self.shared_data.mod_numpy__.sum(self.shared_data.mod_numpy__.dstack((grid[:,:,0]-1, grid[:,:,1])) * g10, 2)
            n01 = self.shared_data.mod_numpy__.sum(self.shared_data.mod_numpy__.dstack((grid[:,:,0], grid[:,:,1]-1)) * g01, 2)
            n11 = self.shared_data.mod_numpy__.sum(self.shared_data.mod_numpy__.dstack((grid[:,:,0]-1, grid[:,:,1]-1)) * g11, 2)
            # Interpolation
            t = f(grid)
            n0 = n00*(1-t[:,:,0]) + t[:,:,0]*n10
            n1 = n01*(1-t[:,:,0]) + t[:,:,0]*n11
            return self.shared_data.mod_numpy__.sqrt(2)*((1-t[:,:,1])*n0 + t[:,:,1]*n1)
    
        def ComputeCloudNoise(self, shape):
            try:
                world = ComputeWeather.generate_perlin_noise_2d(
                    self,
                    shape,
                    (25, 25)) # multiple of shape[0]

                CloudData = world


                image = self.shared_data.mod_PIL_Image_.fromarray(
                    self.shared_data.mod_numpy__.uint8(
                        self.shared_data.mod_matplotlib_cm_.gist_earth(world)*255))

                if self.shared_data.platform == "Linux":
                    try:
                        self.shared_data.mod_OS__.remove(
                            self.shared_data.mod_OS__.path.join(
                                self.shared_data.base_folder,
                                ("resources//game engine resources//clouds//Rnd_noise.png")))
                    except:
                        print("".join(("Unable to clear the previous Perlin-noise image, ",
                                            "attempting to overwrite instead")))

                    image.save(
                        self.shared_data.mod_OS__.path.join(
                            self.shared_data.base_folder,
                            ("resources//game engine resources//clouds//Rnd_noise.png")))

                else:
                    try:
                        self.shared_data.mod_OS__.remove(
                            self.shared_data.mod_OS__.path.join(
                                self.shared_data.base_folder,
                                ("resources\\game engine resources\\clouds\\Rnd_noise.png")))
                    except:
                        print("".join(("Unable to clear the previous Perlin-noise image, ",
                                            "attempting to overwrite instead")))

                    image.save(
                        self.shared_data.mod_OS__.path.join(
                            self.shared_data.base_folder,
                            ("resources\\game engine resources\\clouds\\Rnd_noise.png")))

                image.close()
                return CloudData
            except Exception as Message:
                self.shared_data.error_message = "".join(("GameEngineUtils > ComputeWeather ",
                                                        f"> ComputeCloudNoise: {str(Message)}"))

                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                    self.shared_data)

        def BlendWeather(self):
            def mix(start, end, time, duration):
                return (((end-start)/duration)*time)+start

            if self.weather != self.PreviousWeather and self.WeatherTime < 3:
                if self.weather == "sunny":
                    self.shadowmap["w_min"] = mix(
                        self.Previous_Fog_Distance_Min,
                        1200.0,
                        self.WeatherTime,
                        3)

                    self.shadowmap["w_max"] = mix(
                        self.Previous_Fog_Distance_Max,
                        1600.0,
                        self.WeatherTime,
                        3)

                    Temporary_color = mix(
                        self.Previous_color,
                        1.0,
                        self.WeatherTime,
                        3)

                    self.color.value = (
                        Temporary_color,
                        Temporary_color,
                        Temporary_color)

                    self.CloudsProgram["w_min"] = mix(
                        self.Previous_Fog_Distance_Min,
                        1200.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["w_max"] = mix(
                        self.Previous_Fog_Distance_Max,
                        1600.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["WeatherAlpha"] = mix(
                        self.Previous_CloudsProgram_Alpha,
                        0.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["CloudColor"] = mix(
                        self.Previous_CloudsProgram_CloudColor,
                        1.0,
                        self.WeatherTime,
                        3)

                    multiplier = mix(
                        self.Previous_multiplier,
                        self.CloudHeightMultiplier,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["CloudHeightMultiplier"] = multiplier
                    self.shadowmap["CloudHeightMultiplier"] = multiplier

                    self.skysphere_prog["transparency"] = mix(
                        self.Previous_prog_transparency,
                        1.0,
                        self.WeatherTime,
                        3)

                elif self.weather == "rain.light":
                    self.shadowmap["w_min"] = mix(
                        self.Previous_Fog_Distance_Min,
                        1000.0,
                        self.WeatherTime,
                        3)

                    self.shadowmap["w_max"] = mix(
                        self.Previous_Fog_Distance_Max,
                        1600.0,
                        self.WeatherTime,
                        3)

                    Temporary_color = mix(
                        self.Previous_color,
                        0.8,
                        self.WeatherTime,
                        3)

                    self.color.value = (
                        Temporary_color,
                        Temporary_color,
                        Temporary_color)

                    self.CloudsProgram["w_min"] = mix(
                        self.Previous_Fog_Distance_Min,
                        1200.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["w_max"] = mix(
                        self.Previous_Fog_Distance_Max,
                        1600.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["WeatherAlpha"] = mix(
                        self.Previous_CloudsProgram_Alpha,
                        0.75,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["CloudColor"] = mix(
                        self.Previous_CloudsProgram_CloudColor,
                        0.75,
                        self.WeatherTime,
                        3)

                    multiplier = mix(
                        self.Previous_multiplier,
                        self.CloudHeightMultiplier,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["CloudHeightMultiplier"] = multiplier
                    self.shadowmap["CloudHeightMultiplier"] = multiplier

                    self.skysphere_prog["transparency"] = mix(
                        self.Previous_prog_transparency,
                        self.skysphere_prog_Transparency,
                        self.WeatherTime,
                        3)

                elif self.weather == "rain.heavy":
                    self.shadowmap["w_min"] = mix(
                        self.Previous_Fog_Distance_Min,
                        1000.0,
                        self.WeatherTime,
                        3)

                    self.shadowmap["w_max"] = mix(
                        self.Previous_Fog_Distance_Max,
                        1600.0,
                        self.WeatherTime,
                        3)

                    Temporary_color = mix(
                        self.Previous_color,
                        0.7,
                        self.WeatherTime,
                        3)

                    self.color.value = (
                        Temporary_color,
                        Temporary_color,
                        Temporary_color)

                    self.CloudsProgram["w_min"] = mix(
                        self.Previous_Fog_Distance_Min,
                        800.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["w_max"] = mix(
                        self.Previous_Fog_Distance_Max,
                        1200.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["WeatherAlpha"] = mix(
                        self.Previous_CloudsProgram_Alpha,
                        1.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["CloudColor"] = mix(
                        self.Previous_CloudsProgram_CloudColor,
                        0.35,
                        self.WeatherTime,
                        3)

                    multiplier = mix(
                        self.Previous_multiplier,
                        self.CloudHeightMultiplier,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["CloudHeightMultiplier"] = multiplier
                    self.shadowmap["CloudHeightMultiplier"] = multiplier

                    self.skysphere_prog["transparency"] = mix(
                        self.Previous_prog_transparency,
                        self.skysphere_prog_Transparency,
                        self.WeatherTime,
                        3)

                else:
                    self.shadowmap["w_min"] = mix(
                        self.Previous_Fog_Distance_Min,
                        600.0,
                        self.WeatherTime,
                        3)

                    self.shadowmap["w_max"] = mix(
                        self.Previous_Fog_Distance_Max,
                        800.0,
                        self.WeatherTime,
                        3)

                    Temporary_color = mix(
                        self.Previous_color,
                        0.6,
                        self.WeatherTime,
                        3)

                    self.color.value = (
                        Temporary_color,
                        Temporary_color,
                        Temporary_color)

                    self.CloudsProgram["w_min"] = mix(
                        self.Previous_Fog_Distance_Min,
                        800.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["w_max"] = mix(
                        self.Previous_Fog_Distance_Max,
                        1200.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["WeatherAlpha"] = mix(
                        self.Previous_CloudsProgram_Alpha,
                        1.0,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["CloudColor"] = mix(
                        self.Previous_CloudsProgram_CloudColor,
                        0.25,
                        self.WeatherTime,
                        3)

                    multiplier = mix(
                        self.Previous_multiplier,
                        self.CloudHeightMultiplier,
                        self.WeatherTime,
                        3)

                    self.CloudsProgram["CloudHeightMultiplier"] = multiplier
                    self.shadowmap["CloudHeightMultiplier"] = multiplier

                    self.skysphere_prog["transparency"] = mix(
                        self.Previous_prog_transparency,
                        self.skysphere_prog_Transparency,
                        self.WeatherTime,
                        3)

            else:
                if self.weather == "sunny":
                    self.color.value = (1.0, 1.0, 1.0)

                elif self.weather == "rain.light":
                    self.color.value = (0.8, 0.8, 0.8)

                elif self.weather == "rain.heavy":
                    self.color.value = (0.7, 0.7, 0.7)

                else:
                    self.color.value = (0.6, 0.6, 0.6)

        def ComputeWeather(self):
            try:
                if self.shared_data.mod_random__.randint(0, 100) <= 65:
                    self.weather += "sunny"

                    self.color.value = (1.0, 1.0, 1.0)

                    self.shadowmap["w_min"] = 1200.0
                    self.shadowmap["w_max"] = 1600.0

                    self.CloudsProgram["w_min"] = 1200.0
                    self.CloudsProgram["w_max"] = 1600.0
                    self.CloudsProgram["WeatherAlpha"] = 0.0
                    self.CloudsProgram["CloudColor"] = 1.0

                    self.CloudHeightMultiplier = self.shared_data.mod_random__.randint(1, 500)
                    self.CloudsProgram["CloudHeightMultiplier"] = self.CloudHeightMultiplier
                    self.shadowmap["CloudHeightMultiplier"] = self.CloudHeightMultiplier

                    self.skysphere_prog["transparency"] = 1.0

                else:
                    self.weather += "rain"

                    if self.shared_data.mod_random__.randint(0, 100) <= 80:
                        self.weather += ".light"

                        self.color.value = (0.8, 0.8, 0.8)

                        self.shadowmap["w_min"] = 1000.0
                        self.shadowmap["w_max"] = 1600.0

                        self.CloudsProgram["w_min"] = 1000.0
                        self.CloudsProgram["w_max"] = 1600.0
                        self.CloudsProgram["WeatherAlpha"] = 0.75
                        self.CloudsProgram["CloudColor"] = 0.75

                        self.CloudHeightMultiplier = self.shared_data.mod_random__.randint(139, 500)
                        self.CloudsProgram["CloudHeightMultiplier"] = self.CloudHeightMultiplier
                        self.shadowmap["CloudHeightMultiplier"] = self.CloudHeightMultiplier

                        if self.Time_Percent > 50: # night
                            self.skysphere_prog_Transparency = self.shared_data.mod_random__.randint(35, 50)/100
                        else: # day
                            self.skysphere_prog_Transparency = self.shared_data.mod_random__.randint(25, 40)/100
                        self.skysphere_prog["transparency"] = self.skysphere_prog_Transparency

                    else:
                        self.weather += ".heavy"
                        self.CloudsProgram["WeatherAlpha"] = 1

                        if self.shared_data.mod_random__.randint(0, 100) <= 50:
                            self.weather += ".thundery"

                            self.color.value = (0.6, 0.6, 0.6)

                            self.LengthenStorm = True

                            self.shadowmap["w_min"] = 600.0
                            self.shadowmap["w_max"] = 800.0

                            self.CloudsProgram["w_min"] = 600.0
                            self.CloudsProgram["w_max"] = 800.0
                            self.CloudsProgram["CloudColor"] = 0.25

                            self.CloudHeightMultiplier = self.shared_data.mod_random__.randint(
                                278,
                                500)

                            self.CloudsProgram["CloudHeightMultiplier"] = self.CloudHeightMultiplier
                            self.shadowmap["CloudHeightMultiplier"] = self.CloudHeightMultiplier

                            self.skysphere_prog_Transparency = self.shared_data.mod_random__.randint(0, 25)/100
                            self.skysphere_prog["transparency"] = self.skysphere_prog_Transparency

                        else:
                            self.color.value = (0.7, 0.7, 0.7)

                            self.shadowmap["w_min"] = 800.0
                            self.shadowmap["w_max"] = 1200.0

                            self.CloudsProgram["w_min"] = 800.0
                            self.CloudsProgram["w_max"] = 1200.0
                            self.CloudsProgram["CloudColor"] = 0.35

                            self.CloudHeightMultiplier = self.shared_data.mod_random__.randint(
                                361,
                                500)

                            self.CloudsProgram["CloudHeightMultiplier"] = self.CloudHeightMultiplier
                            self.shadowmap["CloudHeightMultiplier"] = self.CloudHeightMultiplier

                            self.skysphere_prog_Transparency = self.shared_data.mod_random__.randint(10, 45)/100
                            self.skysphere_prog["transparency"] = self.skysphere_prog_Transparency
            except Exception as Message:
                self.shared_data.error_message = "".join(("GameEngineUtils > ComputeWeather ",
                                                        f"> ComputeWeather: {str(Message)}"))

                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(
                    self.shared_data)

    class AccessOtherGUIs:
        def __init__(self):
            pass

        def AccessGUI(self):
            try:
                fullscreen = self.wnd.fullscreen
                self.shared_data.fullscreen = not fullscreen
                WindowSize = self.wnd.width, self.wnd.height
                WindowPos = self.wnd.position
                
                self.wnd.position = (-WindowSize[0],
                                        -WindowSize[1])

                self.wnd.mouse_exclusivity = False
                
                self.shared_data.mod_pygame__.init()

                if self.Inventory:
                    if self.shared_data.platform == "Linux":
                        self.shared_data.mod_ModernGL_window_screenshot.create(
                            source=self.wnd.fbo,
                            name=self.shared_data.mod_OS__.path.join(
                                self.shared_data.base_folder,
                                ("resources//general resources//PauseIMG.png")))
                        
                    else:
                        self.shared_data.mod_ModernGL_window_screenshot.create(
                            source=self.wnd.fbo,
                            name=self.shared_data.mod_OS__.path.join(
                                self.shared_data.base_folder,
                                ("resources\\general resources\\PauseIMG.png")))

                    self.shared_data.command = "Inventory"
                    self.shared_data.mod_inventory__.GenerateInventory.Inventory(self.shared_data)
                    self.Inventory = False

                elif self.Map:
                    self.shared_data.command = "Map"
                    self.shared_data.mod_map_GUI__.GenerateMapGUI.MapGUI(self.shared_data)
                    self.Map = False

                self.wnd.mouse_exclusivity = self.camera_enabled
                self.wnd.position = WindowPos
                self.wnd.fullscreen = fullscreen
                self.shared_data.command = "Play"
            except Exception as Message:
                self.shared_data.error_message = "".join(("GameEngineUtils > AccessOtherGUIs ",
                                                        f"> AccessGUI: {str(Message)}"))

                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(self.shared_data)

    class ShadowmappingMathematics:
        def __init__(self):
            pass

        def ComputeCelestialEntities(self):
            scene_pos = self.shared_data.mod_pyrr_Vector3_(
                        (0, -5, -32),
                        dtype="f4")

            distance = (self.skybox_distance-self.sun_radius)/1.355

            if self.GameTime >= 1056:
                self.GameTime = 0
                self.day += 1

            sun_prepro_time = (self.GameTime/168)-1.5707975

            SunPos_YZ = self.shared_data.mod_math__.cos(
                sun_prepro_time) * distance

            SunPos_X = self.shared_data.mod_math__.sin(
                sun_prepro_time) * distance

            self.sun_lightpos = self.shared_data.mod_pyrr_Vector3_(
                (SunPos_X+self.camera.position.x,
                    SunPos_YZ+self.camera.position.y,
                    0),
                dtype="f4")

            moon_prepro_time = (self.GameTime/168)-4.7123925

            MoonPos_YZ = self.shared_data.mod_math__.cos(
                moon_prepro_time) * distance
            MoonPos_X = self.shared_data.mod_math__.sin(
                moon_prepro_time) * distance

            self.moon_lightpos = self.shared_data.mod_pyrr_Vector3_(
                (MoonPos_X+self.camera.position.x,
                    MoonPos_YZ+self.camera.position.y,
                    0),
                dtype="f4")


            self.sun_prog["m_proj"].write(self.camera.projection.matrix)
            self.sun_prog["m_camera"].write(self.camera.matrix)
            self.sun_prog["m_model"].write(
                self.shared_data.mod_pyrr_Matrix44_.from_translation(
                    self.sun_lightpos + scene_pos,
                    dtype="f4"))


            self.moon_prog["m_proj"].write(self.camera.projection.matrix)
            self.moon_prog["m_camera"].write(self.camera.matrix)
            self.moon_prog["m_model"].write(
                self.shared_data.mod_pyrr_Matrix44_.from_translation(
                    self.moon_lightpos + scene_pos,
                    dtype="f4"))

        def ComputeShadows(self):
            try:
                cam_proj = self.camera.projection.matrix
                cam_look_at = self.camera.matrix

                cam_mvp = cam_proj * cam_look_at
                self.mvp.write(cam_mvp.astype("f4").tobytes())

                # build light camera
                self.light.value = tuple(self.sun_lightpos)
                sun_light_look_at = self.shared_data.mod_pyrr_Matrix44_.look_at(
                    self.sun_lightpos,
                    target=(0, 0, 0),
                    up=(0.0, 0.0, 1.0),
                )

                # light projection matrix (scene dependant)
                light_proj = self.shared_data.mod_pyrr_Matrix44_.perspective_projection(
                    fovy=90.0 / 2,  # smaller value increase shadow precision 2000
                    aspect=self.wnd.aspect_ratio,
                    near=0.01,
                    far=2000.0
                )
                # light model view projection matrix
                mvp_light = light_proj * sun_light_look_at

                bias_matrix = (
                        self.shared_data.mod_pyrr_Matrix44_.from_translation(
                            (0.5, 0.5, 0.5),
                            dtype="f4")
                        *
                        self.shared_data.mod_pyrr_Matrix44_.from_scale(
                            (0.5, 0.5, 0.5),
                            dtype="f4")
                )

                mvp_depth_bias = bias_matrix * mvp_light

                # send uniforms to shaders
                self.mvp_depth.write(mvp_depth_bias.astype("f4").tobytes())
                self.mvp_shadow.write(mvp_light.astype("f4").tobytes())

                # pass 1: render shadow-map (depth framebuffer -> texture) from light view
                #self.fbo_depth.use()
                #self.fbo_depth.clear(
                    #1.0,
                    #1.0,
                    #1.0)

                # https://moderngl.readthedocs.io/en/stable/reference/context.html?highlight=culling#moderngl.Context.front_face
                # clock wise -> render back faces
                #self.ctx.front_face = "cw"
            except Exception as Message:
                print(Message)
                self.shared_data.error_message = "GameEngine > GameEngine > __init__: "+str(Message)
                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(self.shared_data)

    class OnscreenEventFunction:
        def __init__(self):
            pass

        def game_events(self):
            try:
                CurrentTime = self.shared_data.mod_time__.perf_counter()
                if self.Wkeydown or self.Akeydown or self.Skeydown or self.Dkeydown:
                    random_value = self.shared_data.mod_random__.randint(
                        50, 100)/100
                    
                    random_value_sprint = self.shared_data.mod_random__.randint(
                        25, 75)/100
                    
                if self.shared_data.use_mouse_input is False:
                    self.camera.rot_state(
                        -self.Joystick_Rotation[0]*self.shared_data.camera_angle_speed,
                        -self.Joystick_Rotation[1]*self.shared_data.camera_angle_speed)

                if self.RunForwardtimer:
                    if self.shared_data.mod_time__.perf_counter()-self.RunForwardtimer_start > 3.5:
                        self.Sprinting = True
                else:
                    self.Sprinting = False

                if self.Akeydown:
                    if self.shared_data.sound:
                        APressedTime = CurrentTime-self.Akeydowntimer_start

                        if APressedTime >= random_value:
                            self.shared_data.mod_sound_utils__.play_sound.play_footsteps_sound(
                                self.shared_data)

                            self.Akeydowntimer_start = self.shared_data.mod_time__.perf_counter()
                    self.shared_data.total_move_z -= 10
                    if self.shared_data.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.A,
                            self.keys.ACTION_PRESS,
                            None)

                else:
                    if self.shared_data.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.A,
                            self.keys.ACTION_RELEASE,
                            None)

                if self.Skeydown:
                    if self.shared_data.sound:
                        SPressedTime = CurrentTime-self.Skeydowntimer_start

                        if SPressedTime >= random_value:
                            self.shared_data.mod_sound_utils__.play_sound.play_footsteps_sound(
                                self.shared_data)

                            self.Skeydowntimer_start = self.shared_data.mod_time__.perf_counter()
                            
                    self.shared_data.total_move_x -= 10
                    if self.shared_data.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.S,
                            self.keys.ACTION_PRESS,
                            None)

                else:
                    if self.shared_data.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.S,
                            self.keys.ACTION_RELEASE,
                            None)

                if self.Dkeydown:
                    if self.shared_data.sound:
                        DPressedTime = CurrentTime-self.Dkeydowntimer_start

                        if DPressedTime >= random_value:
                            self.shared_data.mod_sound_utils__.play_sound.play_footsteps_sound(
                                self.shared_data)

                            self.Dkeydowntimer_start = self.shared_data.mod_time__.perf_counter()
                    self.shared_data.total_move_z += 10
                    if self.shared_data.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.D,
                            self.keys.ACTION_PRESS,
                            None)

                else:
                    if self.shared_data.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.D,
                            self.keys.ACTION_RELEASE,
                            None)

                
                if self.Wkeydown:
                    if self.shared_data.sound:
                        WPressedTime = CurrentTime-self.RunForwardtimer_start_sound
                        if self.Sprinting:
                            if WPressedTime >= random_value_sprint:
                                self.shared_data.mod_sound_utils__.play_sound.play_footsteps_sound(
                                    self.shared_data)

                                self.RunForwardtimer_start_sound = self.shared_data.mod_time__.perf_counter()

                        else:
                            if WPressedTime >= random_value:
                                self.shared_data.mod_sound_utils__.play_sound.play_footsteps_sound(
                                    self.shared_data)

                                self.RunForwardtimer_start_sound = self.shared_data.mod_time__.perf_counter()

                    if self.Sprinting:
                        self.RunForwardtimer_start = self.shared_data.mod_time__.perf_counter()
                        if self.shared_data.use_mouse_input is False:
                            self.camera.key_input(
                                self.keys.W,
                                self.keys.ACTION_PRESS,
                                None)
                            
                        if self.shared_data.devmode == 10 and self.IKeyPressed:
                            self.camera.velocity = 55
                            self.camera.projection.update(
                                near=0.1,
                                far=2000.0,
                                fov=100)

                            self.shared_data.total_move_x += 35
                        else:
                            self.camera.projection.update(
                                near=0.1,
                                far=2000.0,
                                fov=80)

                            self.camera.velocity = 15 #2.2352
                            self.shared_data.total_move_x += 15

                    else:
                        self.shared_data.total_move_x += 10
                        if self.shared_data.use_mouse_input is False:
                            self.camera.key_input(
                                self.keys.W,
                                self.keys.ACTION_PRESS,
                                None)
                            
                else:
                    if self.shared_data.use_mouse_input is False:
                        self.camera.key_input(
                            self.keys.W,
                            self.keys.ACTION_RELEASE,
                            None)
                        
                    if self.shared_data.devmode == 10 and self.IKeyPressed:
                        self.camera.velocity = 35
                        self.camera.projection.update(
                            near=0.1,
                            far=2000.0,
                            fov=90)

                    else:
                        self.camera.velocity = 10 #1.42
                        self.camera.projection.update(
                            near=0.1,
                            far=2000.0,
                            fov=70)

                if self.space_key_pressed and self.Jump is False:
                    self.Jump = True
                    self.jump_timer = self.shared_data.mod_time__.perf_counter()
                    self.StartYposition = self.camera.position.y

                if self.Jump:
                    current_time = self.shared_data.mod_time__.perf_counter()
                    delta = current_time - self.jump_timer
                    offset = delta*180
                    offset_radians = self.shared_data.mod_math__.radians(offset)

                    if self.shared_data.devmode == 10:
                        calculation = self.StartYposition + (self.shared_data.mod_math__.sin(
                            offset_radians) / (2 / self.modifier))
                        
                    else:
                        calculation = self.StartYposition + (self.shared_data.mod_math__.sin(
                            offset_radians) / 2)
                    
                    self.camera.position.y = calculation
                    if delta > 1:
                        self.Jump = False
                        if self.Collision == False:
                            self.camera.position.y = self.StartYposition

            except Exception as Message:
                self.shared_data.error_message = "GameEngine > GameEngine > __init__: "+str(Message)
                self.shared_data.error_message_detailed = "".join(
                    self.shared_data.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.shared_data.mod_error_utils__.generate_error_screen.error_screen(self.shared_data)

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
