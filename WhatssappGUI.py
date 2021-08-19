# cython: language_level=3

"""Whatssapp message automation"""
from selenium import webdriver
from tkinter import *
import getpass
import time


def run():
    """Run Whatssapp Automation"""

    # get data's

    t = int(timeText.get(0.0, END)[:-1])
    message = textText.get(0.0, END)[:-1]

    sendMessage(t, message)


"""Initialize WP Class"""
# define root and config it
root = Tk()
root.title("Whatssapp automation")

# font and background color
font = ("San Serif", 15)

color = "#888888"

# whatssapp run class

# labels
timeLabel = Label(root, text="Time", height=5, width=10, font=font, bg=color)
textLabel = Label(root, text="Text", height=5, width=10, font=font, bg=color)

# text boxes
timeText = Text(root, height=5, bg=color, borderwidth=2, font=font)
textText = Text(root, height=5, bg=color, borderwidth=2, font=font)

# run button
runButton = Button(root, text="Run", height=2, bg=color, font=font, command=run)

# row and cols
row = 3
col = 2

# username
username = getpass.getuser()

# drivers
driverPath = fr"C:\Users\{username}\Desktop\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverPath)
driver.get("https://web.whatsapp.com")
driver.maximize_window()


def ConfigRowAndCol():
    """Configure Row And Columns"""
    Grid.columnconfigure(root, index=0, weight=7)
    Grid.columnconfigure(root, index=1, weight=1)

    for num in range(row):
        Grid.rowconfigure(root, index=num, weight=5)
    Grid.rowconfigure(root, index=2, weight=1)


def Pack():
    """Pack"""
    # grid time
    timeLabel.grid(row=0, column=0, sticky="news")
    timeText.grid(row=0, column=1, sticky="news")

    # grid text
    textLabel.grid(row=1, column=0, sticky="news")
    textText.grid(row=1, column=1, sticky="news")

    # grid run button
    runButton.grid(row=2, column=0, columnspan=2, sticky="news")


def sendMessage(t, message):
    """Run button"""
    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

    for _ in range(t):
        start = time.time()
        msg_box.send_keys(message)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
        print(time.time()-start)


def main():
    """Main function"""
    ConfigRowAndCol()
    Pack()

    root.mainloop()


if __name__ == '__main__':
    main()
