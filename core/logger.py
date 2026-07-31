from datetime import datetime


class Logger:

    def log(self, message):

        current_time = datetime.now().strftime("%H:%M:%S")

        print(f"[{current_time}] {message}")