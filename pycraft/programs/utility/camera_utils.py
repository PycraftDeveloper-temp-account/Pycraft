if __name__ != "__main__":
    try:
        import time

        import math_utils
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

    class compute_camera:
        """
            NYI
            
            - Args:
                - None
    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            
        def __init__(self):
            pass

        def camera_move_state(
                camera,
                direction,
                activate,
                RIGHT,
                LEFT,
                FORWARD,
                BACKWARD,
                UP,
                DOWN,
                STILL,
                POSITIVE,
                NEGATIVE):
            """
            NYI
            
            - Args:
                - camera ():
                - direction ():
                - activate ():
                - RIGHT ():
                - LEFT ():
                - FORWARD ():
                - BACKWARD ():
                - UP ():
                - DOWN ():
                - STILL ():
                - POSITIVE ():
                - NEGATIVE ():
    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            if direction == RIGHT:
                camera._xdir = POSITIVE if activate else STILL
            if direction == LEFT:
                camera._xdir = NEGATIVE if activate else STILL
            if direction == FORWARD:
                camera._zdir = NEGATIVE if activate else STILL
            if direction == BACKWARD:
                camera._zdir = POSITIVE if activate else STILL
            if direction == UP:
                camera._ydir = POSITIVE if activate else STILL
            if direction == DOWN:
                camera._ydir = NEGATIVE if activate else STILL

        def get_camera_values(
                self,
                camera,
                camera_up,
                compile_math,
                STILL,
                POSITIVE,
                NEGATIVE):
            """
            NYI
            
            - Args:
                - self ():
                - camera ():
                - camera_up ():
                - compile_math ():
                - STILL ():
                - POSITIVE ():
                - NEGATIVE ():
    
            - Keyword Args:
                - None

            - Output:
                - cam_matrix ():
                - position ():
            """
            position = camera.position

            compute_camera.compute_camera_dir(
                self, camera, POSITIVE, NEGATIVE)

            if compile_math:
                cam_matrix = math_utils.compiled_math_functions.gl_look_at(
                    position, position + camera.dir, camera_up)  # slow but works
                
            else:
                cam_matrix = math_utils.math_functions.gl_look_at(
                    position, position + camera.dir, camera_up)  # slow but works

            return cam_matrix, position
            
        def compute_camera_dir(
                self,
                camera,
                POSITIVE,
                NEGATIVE):
            """
            NYI
            
            - Args:
                - self ():
                - camera ():
                - POSITIVE ():
                - NEGATIVE ():
    
            - Keyword Args:
                - None

            - Output:
                - None
            """
            # Use separate time in camera so we can move it when the demo is paused
            now = time.time()
            # If the camera has been inactive for a while, a large time delta
            # can suddenly move the camera far away from the scene
            t = max(now - camera._last_time, 0)
            camera._last_time = now

            # X Movement
            if camera._xdir == POSITIVE:
                camera.position += camera.right * camera._velocity * t
            elif camera._xdir == NEGATIVE:
                camera.position -= camera.right * camera._velocity * t

            # Z Movement
            if camera._zdir == NEGATIVE:
                camera.position += camera.dir * camera._velocity * t
            elif camera._zdir == POSITIVE:
                camera.position -= camera.dir * camera._velocity * t

            # Y Movement
            if camera._ydir == POSITIVE:
                camera.position += camera.up * camera._velocity * t
            elif camera._ydir == NEGATIVE:
                camera.position -= camera.up * camera._velocity * t
                
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
