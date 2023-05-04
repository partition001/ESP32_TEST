from machine import Pin, ADC
import time

hall_sensor = ADC(Pin(34))  # init Hall Sensor
voltage_pin = ADC(Pin(35))
hall_sensor.atten(ADC.ATTN_6DB)  # analog signal tunning
hall_sensor.width(ADC.WIDTH_12BIT)  # grad 12 bit

sensitivity = 0.1  # 100 мВ/А
VREF = 3.3


while True:
    
    voltage = voltage_pin.read() * VREF / 4095.0
    
    current = voltage / sensitivity
    
    hall_value = hall_sensor.read()
    
    print("Amp:", hall_value, "Volt: {:.2f}V".format(voltage), "Cur: {:.2f}A".format(current))
    
    time.sleep(1)
