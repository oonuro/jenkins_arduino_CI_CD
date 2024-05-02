import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Wait for Arduino to initialize
time.sleep(5)

# Send command to turn LED on
ser.write(b'on\n')
response = ser.readline().strip()
print(response)

# Wait for LED to blink
time.sleep(5)

# Send command to turn LED off
ser.write(b'off\n')
response = ser.readline().strip()
print(response)

time.sleep(5)

ser.write(b'on\n')
response = ser.readline().strip()
print(response)

# Wait for LED to blink
time.sleep(5)

# Send command to turn LED off
ser.write(b'off\n')
response = ser.readline().strip()
print(response)

time.sleep(5)

ser.close()
