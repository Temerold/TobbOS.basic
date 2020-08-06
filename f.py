import sys
import os
import time
import random
import time
from time import sleep
import tkinter as tkk
import TobsTTS_lib as ttt
import playsound
from playsound import playsound

def current():
    global current_input
    current_input = input("\n> ")
    return current_input

def boot(fast_boot = False):
    if fast_boot == False:
        rand_fast_boot = random.randint(1, 1000)
        if rand_fast_boot == 1:
            playsound("intro2.mid")
        else:
            playsound("intro1.mid")

        sleep(1)
        print("Välkommen till TobbOS!")
        sleep(1)
        

def tick_check():
    global current_input

    current()




        
boot()

while True:
    tick_check()
