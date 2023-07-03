print("Das ist ein Test")

import threading
from ctypes import *

ok = windll.user32.BlockInput(True)  # enable block

# or

oks = windll.user32.BlockInput(False)  # disable block

import keyboard
from pynput.mouse import Controller
from time import sleep


def blockinput():
    global block_input_flag
    block_input_flag = 1
    t1 = threading.Thread(target=blockinput_start)
    t1.start()
    print("[SUCCESS] Input blocked!")


def blockinput_start():
    mouse = Controller()
    global block_input_flag
    for i in range(150):
        keyboard.block_key(i)
    while block_input_flag == 1:
       mouse.position = (0, 0)
# das Problem die maus wird nicht entfernt


def blockinput_stop():
    global block_input_flag
    for i in range(150):
        keyboard.unblock_key(i)
    block_input_flag = 0


def unblock_input():
    blockinput_stop()
    print("[SUCCESS] Input unblocked!")


blockinput()
print("now blocking")
sleep(10)
unblock_input()
print("now unblocking")
