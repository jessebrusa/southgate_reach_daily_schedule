from tkinter import *
from datetime import datetime, timedelta

custom_font = (25)

class ReachFormat():

    def __init__(self):
        self.month = ""
        self.year = ""
        self.before_date_list = []
        self.after_date_list = []
        self.event_list = []
        self.reach_format = []
        self.event_count = 1
        self.st_list = [1, 21, 31]
        self.nd_list = [2, 22]
        self.rd_list = [3, 23]
        self.calendar_month = {
            'January': '01',
            'February': '02',
            'March': '03',
            'April': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'August': '08',
            'September': '09',
            'October': '10',
            'November': '11',
            'December': '12'
        }
        self.gui()


    def submit_entry(self):
        try:
            self.month = self.month_entry.get().strip()
            self.year = self.year_entry.get().strip()

            self.event_label = Label(text="Event 1: ", font=custom_font)
            self.event_label.grid(row=2, column=0)
            self.event_entry = Entry(width=40)
            self.event_entry.grid(row=2, column=1)

            self.month_label.destroy()
            self.month_entry.destroy()

            self.year_label.destroy()
            self.year_entry.destroy()
        except TclError:
            pass

        self.event_list.append(self.event_entry.get())
        self.event_entry.delete(0, END)
        

        if self.event_count in self.st_list:
            day = f"{self.event_count}st"
        elif self.event_count in self.nd_list:
            day = f"{self.event_count}nd"
        elif self.event_count in self.rd_list:
            day = f"{self.event_count}rd"
        else:
            day = f"{self.event_count}th"
        self.event_label.config(text=f"{self.month}, {day} - Event:")
        self.event_count += 1
    

    def all_done_format(self):
        self.event_list.pop(0)
        for num in range(len(self.event_list)):

            if num + 1 in self.st_list:
                day = f"{num+1}st"
            elif num + 1 in self.nd_list:
                day = f"{num+1}nd"
            elif num +1 in self.rd_list:
                day = f"{num+1}rd"
            else:
                day = f"{num+1}th"

            day_of_week = datetime.strptime(f"{self.month} {num+1}, {self.year}", '%B %d, %Y').strftime('%A') 

            message = f"-\n{day_of_week}, {self.month} {day}\n{self.event_list[num]}\n-\n"
            self.reach_format.append(message)


        self.date = f"{self.calendar_month[self.month]}-01-{self.year}"
        self.calculate_before_date()
        self.calculate_after_date()

        self.window.destroy()


    def on_enter_key(self, event):
        self.submit_entry()


    def calculate_before_date(self):
        day_counter = -4
        original_date = datetime.strptime(self.date, "%m-%d-%Y")
        for num in range(len(self.reach_format)):
            before_date_unformatted = original_date + timedelta(days=day_counter)
            self.before_date_list.append(before_date_unformatted.strftime("%m/%d/%Y"))
            day_counter += 1


    def calculate_after_date(self):
        day_counter = 1
        original_date = datetime.strptime(self.date, "%m-%d-%Y")
        for num in range(len(self.reach_format)):
            after_date_unformatted = original_date + timedelta(days=day_counter)
            self.after_date_list.append(after_date_unformatted.strftime("%m/%d/%Y"))
            day_counter += 1


    def gui(self):
        self.window = Tk()
        self.window.title('Reach Format')
        self.window.config(padx=10, pady=10)

        self.month_label = Label(text="Month: ", font=custom_font)
        self.month_label.grid(row=0, column=0)
        self.month_entry = Entry(width=40)
        self.month_entry.grid(row=0, column=1)

        self.year_label = Label(text="Year: ", font=custom_font)
        self.year_label.grid(row=1, column=0)
        self.year_entry = Entry(width=40)
        self.year_entry.grid(row=1, column=1)

        self.submit_button = Button(text='Submit', command=self.submit_entry, 
                                    width=30, font=custom_font)
        self.submit_button.grid(row=3, column=0, columnspan=2)
        self.window.bind('<Return>', self.on_enter_key)

        self.all_done_button = Button(text='All Done', command=self.all_done_format, 
                                      width=30, font=custom_font)
        self.all_done_button.grid(row=4, column=0, columnspan=2)

        self.window.mainloop()