import os
import pyperclip
import selenium.common.exceptions
from pynput import keyboard
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import WebAutoSearch

def process3():
    driver = webdriver.Firefox()                # Launches GeckoDriver
    driver.set_window_size(1106, 1080)          # Setting the windows size
    driver.get("https://www.duckduckgo.com")    # Setting duckduckgo as its search engine

    def fire():     # All available hotkeys
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
                        MAIN_SEARCH_BOX = driver.find_element(By.ID, "search_form_input_homepage")
                        MAIN_SEARCH_BOX.send_keys(data)
                        MAIN_SEARCH_BOX.send_keys(Keys.ENTER)
                        fire()

                    except selenium.common.exceptions.NoSuchElementException:
                        TOP_SEARCH_BOX = driver.find_element(By.ID, "search_form_input")
                        TOP_SEARCH_BOX.send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)
                        TOP_SEARCH_BOX.send_keys(data)
                        TOP_SEARCH_BOX.send_keys(Keys.ENTER)
                        fire()

            elif any([key in HOT for HOT in QUIT_KEY]):
                current.add(key)
                if any(all(k in current for k in HOT) for HOT in QUIT_KEY):
                    driver.quit()           # This kills the GeckoDriver process
                    L.stop()                # This stops the keyboard listener (Again, This is NOT a keylogger, so calm the fuck down) - 6H0$T
                    print("Exiting...")     # When user presses 'esc',
                    WebAutoSearch.main()    # It goes back to the main menu
                    os._exit(0)             # And kills this process

        def on_release(key):
            if any([key in HOT for HOT in AUTO_SEARCH_HOTKEY]):
                current.remove(key)
            elif any([key in HOT for HOT in QUIT_KEY]):
                current.remove(key)

        with keyboard.Listener(on_press=on_press, on_release=on_release) as L:
            L.join()

    fire()

if __name__ == "__main__":
    process3()
