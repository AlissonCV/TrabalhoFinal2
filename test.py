from asyncio.windows_events import NULL
import pyfirmata
import time
from ast import If, While
from pickle import TRUE
from tkinter import *
from pyfirmata import Arduino, SERVO
from time import sleep

board = pyfirmata.Arduino('COM3')
pin = 9
board.digital[pin].mode = SERVO

def rotateServo(pin , angle): #Posicionar o servo 
    board.digital[pin].write(angle)

def servoctrl(angle): #Recebe um valor angular e posiciona o servo
    #A = input()
    if angle == "":
        rotateServo(pin, "0")
    else:
        rotateServo(pin, angle)

def ledon ():
    # board=pyfirmata.Arduino('COM3')
    board.digital[7].write(1)

def ledoff ():
    # board=pyfirmata.Arduino('COM3')
    board.digital[7].write(0)

def move_servo(angle):
    pin_9.write(angle)

def Blink():
    i=0
    while i < 10 :
        i += 1
        board.digital[4].write(1)
        sleep(0.1)
        board.digital[4].write(0)
        sleep(0.1)

def servonew():
    global pin_9

    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    pin_9 = board.get_pin('d:9:s')
    
    root = Tk()
    scale = Scale(root, command = move_servo, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Angle')
    scale.pack(anchor = CENTER)

    root.mainloop()

#while TRUE:
    #servoctrl()

# while TRUE:
#     if input() == "1":
#         ledon(1)
#     else:
#         ledoff(0)