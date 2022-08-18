from asyncio.windows_events import NULL
import pyfirmata
import time
from ast import If, While
from pickle import TRUE
from tkinter import *
from pyfirmata import Arduino, SERVO
from time import sleep

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()

def servoctrl(pin, angle): #Recebe um valor angular e posiciona o servo
    board.digital[pin].write(angle)

def led(pin,boleano):
    board.digital[pin].write(0)

def Blink(pin,boleano):
    if boleano:
        while boleano :
            board.digital[pin].write(1)
            sleep(0.1)
            board.digital[pin].write(0)
            sleep(0.1)
    else:
        board.digital[pin].write(0)