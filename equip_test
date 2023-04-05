import machine
import esp32
import gc
import esp
import time


machine.UART(0, baudrate=115200)  

# Show chip info
print("ESP32 processor info:")
print("  Chip ID:			", hex(int.from_bytes(machine.unique_id(), 'big')))
print("  Co-processor:			", esp32.ULP())
print("  Frequency:			", machine.freq() / 1000000, "MHz")
print("  Temperature:			", esp32.raw_temperature() / 10, "°C")
print("  Hall sensor:			", esp32.hall_sensor())

# Show memory info
print("ESP32 memory info:")
#print("Flash ID: ", hex(esp32.flash_id()))
print("  Flash size:			", esp.flash_size() / 1000, "bytes")
print("  Free heap size:		", gc.mem_free())
print("  Total heap size:		", gc.mem_alloc() + gc.mem_free())
print("  Allocated heap size:		", gc.mem_alloc())

# Show wifi info
print("Wi-Fi info:")
print("  MAC address:", ':'.join('{:02x}'.format(i) for i in machine.unique_id()))
