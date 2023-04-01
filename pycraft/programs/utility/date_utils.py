if __name__ != "__main__":
    try:
        import datetime
    except ModuleNotFoundError as Message:
        from tkinter import messagebox
        error_message = f"{Message} in date_utils"
        messagebox.showerror(
            "Startup Error",
            error_message)
        quit()
            
    class Date:
        def __init__(self):
            self.time = datetime.datetime.now()
            
            self._iso_day = f"{self.time.day: 03d}".strip()
            self._iso_month = f"{self.time.month: 03d}".strip()
            self._iso_year = self.time.year
            
            self._iso_hour = f"{self.time.hour: 03d}".strip()
            self._iso_minute = f"{self.time.minute: 03d}".strip()
            self._iso_second = f"{self.time.second: 03d}".strip()
            
            self.formatted_iso_time = self.calculate_formatted_time()
            self.time_code = self.calculate_time_code()
            
        def get_time(self):
            return self.time
        
        def update_time(self):
            self.time = datetime.datetime.now()
            self.formatted_iso_time = self.calculate_formatted_time()
            self.time_code = self.calculate_time_code()
            
        def calculate_formatted_time(self):
            self.formatted_iso_time = "".join((f"{self._iso_day}/{self._iso_month}/",
                                               f"{self._iso_year} at {self._iso_hour}:",
                                               f"{self._iso_minute}:{self._iso_second}"))
            
        def calculate_time_code(self):
            self.time_code = "".join((f"{self._iso_year}{self._iso_month}",
                                        f"{self._iso_day}{self._iso_hour}",
                                        f"{self._iso_minute}{self._iso_second}"))
            
        def get_formatted_time(self):
            return self.formatted_iso_time
        
        def get_time_code(self):
            return self.time_code
        
else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
