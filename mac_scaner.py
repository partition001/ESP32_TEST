import time
import machine
from bluetooth import BLE
from binascii import hexlify
from micropython import const
from time import localtime, sleep



# PIN2 PWM parameters
led_pin = machine.Pin(2, machine.Pin.OUT)
pwm = machine.PWM(led_pin)

# PWM parameters
pwm.freq(1500) # freq 1,5 kHz
pwm.duty(0) # low brightless

_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)

found_addresses = []  # create an empty list to store found addresses
found = False  # set the initial value of the found flag to False

def handle_scan(ev, data):
    global found_addresses, found  # declare global variables

    if ev == _IRQ_SCAN_RESULT:
        addr = hexlify(data[1], ":").decode()
        rssi = data[3]
        if found_addresses.count(addr) == 0:  # check if the address is already in the list
            print("Device: {0} ({1} dBm):".format(addr, rssi))
            found_addresses.append(addr)  # add found address to list

    elif ev == _IRQ_SCAN_DONE:
        print("Scan done.")
        if not found:  # if the list of found addresses has not been printed yet
            print("Found addresses: ", found_addresses)  # print list of found addresses
            found = True  # set the value of the found flag to True
    else:
        print("Unexpected event: {0}".format(ev))

BLE().active(True)
BLE().irq(handle_scan)
print("Start scanning...")
BLE().gap_scan(0, 50000, 25250)  # scan often & indefinitely

while True:
    sleep(5)
