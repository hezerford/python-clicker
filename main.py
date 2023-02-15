import time 
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

key = input('The input key for the clicker: ')
toggle_key = KeyCode(char=s)
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.01) # время отклика мыши

def toggle_event(key):
    if key == toggle_key:
        global clicking
        clicking = not clicking 

def main():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()

if __name__ == '__main__':
    main()