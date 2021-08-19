"""Whatssapp message automation"""
import threading

try:
    from selenium import webdriver
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'selenium'])
    from selenium import webdriver

from tkinter import *
import getpass
import time


class WP:
    """'WP Class"""
    def __init__(self):
        """Initialize WP Class"""
        # define root and config it
        self.root = Tk()
        self.root.title("Whatssapp automation")

        # font and background color
        self.font = ("San Serif", 15)
        self.color = "#888888"

        # whatssapp run class
        self.wpRun = WpAutomation()

        # labels
        self.timeLabel = Label(self.root, text="Time", height=5, width=10, font=self.font, bg=self.color)
        self.textLabel = Label(self.root, text="Text", height=5, width=10, font=self.font, bg=self.color)

        # text boxes
        self.timeText = Text(self.root, height=5, bg=self.color, borderwidth=2, font=self.font)
        self.textText = Text(self.root, height=5, bg=self.color, borderwidth=2, font=self.font)

        # run button
        self.runButton = Button(self.root, text="Run", height=2, bg=self.color, font=self.font, command=self.run)
        # row and cols
        self.row = 3
        self.col = 2

        self.ConfigRowAndCol()
        self.Pack()

        self.root.mainloop()

    def run(self):
        """Run Whatssapp Automation"""

        # get data's
        t = int(self.timeText.get(0.0, END)[:-1])
        message = self.textText.get(0.0, END)[:-1]

        self.wpRun.run(t, message)

    def ConfigRowAndCol(self):
        """Configure Row And Columns"""
        Grid.columnconfigure(self.root, index=0, weight=7)
        Grid.columnconfigure(self.root, index=1, weight=1)

        for num in range(self.row):
            Grid.rowconfigure(self.root, index=num, weight=5)
        Grid.rowconfigure(self.root, index=2, weight=1)

    def Pack(self):
        """Pack"""

        # grid time
        self.timeLabel.grid(row=0, column=0, sticky="news")
        self.timeText.grid(row=0, column=1, sticky="news")

        # grid text
        self.textLabel.grid(row=1, column=0, sticky="news")
        self.textText.grid(row=1, column=1, sticky="news")

        # grid run button
        self.runButton.grid(row=2, column=0, columnspan=2, sticky="news")


class WpAutomation:
    """Whatssapp Automation"""
    def __init__(self):
        """Initialize Whatssapp Automation"""

        # username
        self.username = getpass.getuser()

        # drivers
        self.driverPath = fr"C:\Users\{self.username}\Desktop\driver\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.driverPath)
        self.driver.get("https://web.whatsapp.com")
        self.driver.maximize_window()

    def send(self, message):
        """Send Message"""
        self.msg_box.send_keys(message)
        self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

    def run(self, t, message):
        """Run button"""
        self.msg_box = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

        for _ in range(t):
            thread = threading.Thread(target=self.send, args=(message,))
            thread.start()
            thread.join()


if __name__ == '__main__':
    WP()
