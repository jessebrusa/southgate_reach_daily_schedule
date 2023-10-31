from gui import ReachFormat
from driver import ReachAppDriver
import tkinter as tk
import threading
from decouple import config


chromedriver_path = "project\chromedriver.exe"
reach_username = 'JBrusa'
reach_password = config('MY_REACH_PASSWORD')


gui = ReachFormat()
formatted_text = gui.reach_format
before_dates = gui.before_date_list
after_dates = gui.after_date_list

custom_font = (25)

class App:
    def __init__(self, root):
        self.root = root
        root.title("My Application")

        self.label = tk.Label(root, text="Starting Chrome",
                              font=custom_font)
        self.label.pack(padx=10, pady=10)

        self.task_thread = threading.Thread(target=self.run_tasks)
        self.task_thread.start()

    def update_label(self, text):
        self.label.config(text=text)
        self.root.update_idletasks()

    def run_tasks(self):
        reach_app = ReachAppDriver(chromedriver_path)
        reach_app.start_chrome()
        self.update_label("Navigating to daily schedule within ReachApp")

        reach_app.reachapp_login_navigate_to_schedule(reach_username, reach_password)
        self.update_label("Deleting Old Events")

        reach_app.delete_old_events()
        self.update_label("Loading New Events")

        reach_app.load_new_events(formatted_text, before_dates, after_dates)
        self.update_label("Complete!")

        self.root.after(4000, self.close_window) 

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()