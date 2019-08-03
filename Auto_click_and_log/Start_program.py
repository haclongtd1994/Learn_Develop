from time import sleep
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse    import Button, Controller   as MouseController

keyboard = KeyboardController()
mouse = MouseController()
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
keyboard.type('cmd')
sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
sleep(1)
keyboard.type("cd D:\TuHocMoiThu\Renesas_Dev\Auto_click_and_log ")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
keyboard.type('python Auto_Click_and_type.py')
keyboard.press(Key.enter)
keyboard.release(Key.enter)