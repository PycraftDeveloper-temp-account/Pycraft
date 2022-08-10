if __name__ != "__main__":
    print("Started <Pycraft_ShareDataUtil>")

    class Share:
        def __init__(self):
            pass

        def initialize(Data):
            try:
                global self
                self = Data
            except Exception as Message:
                self.error_message = "ShareDataUtils > Share > initialize: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

        def initialize_controller(Data):
            try:
                global Controller
                Controller = Data
            except Exception as Message:
                self.error_message = "ShareDataUtils > Share > initialize_controller: "+str(Message)

                self.error_message_detailed = "".join(
                    self.mod_traceback__.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(self)

        def initialize_controller_game(Data):
            try:
                global Game_SharedData
                Game_SharedData = Data
            except Exception as Message:
                self.error_message = "".join(("ShareDataUtils > Share > ",
                                             f"initialize_controller_game: {str(Message)}"))

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
