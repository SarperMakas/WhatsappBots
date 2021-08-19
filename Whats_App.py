from selenium import webdriver
import time
import sys
import getpass, os
# self.userName = getpass.getuser()  # user name


def open():
    global driver
    driver_path = "C:\\Users\\Sarper\\Desktop\\driver\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://web.whatsapp.com")
    driver.maximize_window()


def var():
    global name, msg, count
    print("Do you want to quit?")
    quiting = input("Yes(y) No(n):")
    if quiting.lower() == "n":
        print("Going on.")
    else:
        exitmsg = "Message sender finish."
        while True:
            for i in exitmsg:
                print(i, end="", sep="", flush=True)
            break
        sys.exit()
    name = input("Enter name or group name:")
    msg = input("Enter message:")
    while True:
        try:
            count = int(input("Enter count:"))
            break
        except ValueError:
            print("Count must be integer.")
    return name, msg, count


def scan():
    time.sleep(0.3)
    return input("Enter anything after scan QR code:")


def message():
    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
    print("Message sending finish.")


def main():
    open()
    while True:
        print("\n\n")
        var()
        scan()
        message()


main()
