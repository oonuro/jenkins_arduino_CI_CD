import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Wait for Arduino to initialize
time.sleep(2)

# Send command to turn LED on
ser.write(b'1\n')
response = ser.readline().strip()
print(response)

# Wait for LED to blink
time.sleep(5)

# Send command to turn LED off
ser.write(b'2\n')
response = ser.readline().strip()
print(response)

time.sleep(3)

ser.write(b'1\n')
response = ser.readline().strip()
print(response)

# Wait for LED to blink
time.sleep(2)

ser.close()
