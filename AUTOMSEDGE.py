import os
import pyperclip
import selenium.common.exceptions
from pynput import keyboard
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import WebAutoSearch

def process2():

    driver = webdriver.Edge()               #Launches MsEdgeDriver
    driver.set_window_size(1106, 1080)      #Setting the window size
    driver.get("https://www.bing.com")      #Setting bing as its search engine

    def edge():     #All available hotkeys

        AUTO_SEARCH_HOTKEY = [
            {keyboard.Key.alt_l}
        ]

        QUIT_KEY = [
            {keyboard.Key.esc}
        ]

        current = set()

        def on_press(key):

            if any([key in HOT for HOT in AUTO_SEARCH_HOTKEY]):
                current.add(key)
                if any(all(k in current for k in HOT) for HOT in AUTO_SEARCH_HOTKEY):

                    data = pyperclip.paste()
                    pyperclip.copy(data)

                    try:

                        TOP_SEARCH_BOX = driver.find_element(By.ID, "sb_form_q")
                        TOP_SEARCH_BOX.send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)
                        TOP_SEARCH_BOX.send_keys(data)
                        TOP_SEARCH_BOX.send_keys(Keys.ENTER)
                        edge()

                    except selenium.common.exceptions.NoSuchElementException:

                        print("Error: I can't seem to find the XPATH")



            elif any([key in HOT for HOT in QUIT_KEY]):
                current.add(key)
                if any(all(k in current for k in HOT) for HOT in QUIT_KEY):

                    driver.quit()           #This kills the MsEdgeDriver process
                    L.stop()                #This stops the keyboard listener (This is not a keylogger, so calm the fuck down) - 6H0$T
                    print("Exiting...")     #When user presses 'esc',
                    WebAutoSearch.main()    #It goes back to the main menu
                    os._exit(0)             #And kills this process

        def on_release(key):
            if any([key in HOT for HOT in AUTO_SEARCH_HOTKEY]):
                current.remove(key)

            elif any([key in HOT for HOT in QUIT_KEY]):
                current.remove(key)

        with keyboard.Listener(on_press = on_press, on_release = on_release) as L:
            L.join()

    edge()

if __name__ == "__main__":
    process2()