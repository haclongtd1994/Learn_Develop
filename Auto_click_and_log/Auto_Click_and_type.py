'''
    Desciption: Initialization for phase coding
    Author: PTH
    Version: v1.0.0
'''
'''-------------------Import Package------------------'''
# Lib to monitor time and delay
from time import sleep
#Lib to ctreate progress bar
from tqdm import tqdm, trange
import colorama
# Lib to listener and control keyboard and mouse of user
from pynput.mouse    import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse    import Button, Controller   as MouseController
'''-------------------Initialization Variable--------------'''
#--------------------Controller---------------------#
keyboard = KeyboardController()
mouse = MouseController()
#------------------Progress Bar---------------------#
# Color terminal
# If using Windows, init() will cause anything sent to stdout or stderr
# will have ANSI color codes converted to the Windows versions. Hooray!
# If you are already using an ANSI compliant shell, it won't do anything
colorama.init()
color = {
    'white':    "\033[1;37m",
    'yellow':   "\033[1;33m",
    'green':    "\033[1;32m",
    'blue':     "\033[1;34m",
    'cyan':     "\033[1;36m",
    'red':      "\033[1;31m",
    'magenta':  "\033[1;35m",
    'black':      "\033[1;30m",
    'darkwhite':  "\033[0;37m",
    'darkyellow': "\033[0;33m",
    'darkgreen':  "\033[0;32m",
    'darkblue':   "\033[0;34m",
    'darkcyan':   "\033[0;36m",
    'darkred':    "\033[0;31m",
    'darkmagenta':"\033[0;35m",
    'darkblack':  "\033[0;30m",
    'off':        "\033[0;0m"
}
# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = '\033[2J'

# Progress bar by tqdm 
for i in trange(25):
	sleep(0.1)

print(color['red'] + "This is bot automation of PTH" + color['off'])
print(color['yellow'] + "Version: 1.0.0" + color['off'])

print("Hello please set some information for me !")
print("Hello Customer?")
User_name="PTH"               #str(input())
print("Hello "+color['cyan']+"{0}".format(User_name)+color['off'])

keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
keyboard.type('cmd')
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
keyboard.type("cd D:\TuHocMoiThu\Renesas_Dev\Auto_click_and_log")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
keyboard.type('python Log_file_to_determine_position.py')
keyboard.press(Key.enter)
keyboard.release(Key.enter)