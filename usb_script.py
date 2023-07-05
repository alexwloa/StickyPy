import sys
import threading
from ctypes import *

ok = windll.user32.BlockInput(True)  # enable block
oks = windll.user32.BlockInput(False)  # disable block

import keyboard
from pynput.mouse import Controller
import time

# -------------------------------------------- Block -------------------------------------------- #
# block all class
def blockinput_start():
    mouse = Controller()
    global block_input_flag
    for i in range(150):
        keyboard.block_key(i)
    while block_input_flag == 1:
        mouse.position = (0, 0)


# block input
def blockinput():
    global block_input_flag
    block_input_flag = 1
    t1 = threading.Thread(target=blockinput_start)
    t1.start()
    print("[SUCCESS] Input blocked!")


# -------------------------------------------- Unblock -------------------------------------------- #
# stop block
def blockinput_stop():
    global block_input_flag
    for i in range(150):
        keyboard.unblock_key(i)
    block_input_flag = 0


# unblock input
def unblock_input():
    blockinput_stop()
    print("[SUCCESS] Input unblocked!")


# -------------------------------------------- Main -------------------------------------------- #
# Variante 1
blockinput()
time.sleep(10)
unblock_input()
sys.exit()
