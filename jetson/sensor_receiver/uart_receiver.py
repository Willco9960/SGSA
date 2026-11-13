import serial
import time

ser = serial.Serial(
    port='/dev/ttyTHS1',
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

print("Jetson listening on /dev/ttyTHS1 ...")

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8', errors='ignore').strip()
            if data:
                print(f"From STM32 → {data}")
                # Optional reply
                ser.write(f"ACK from Jetson: {data}\n".encode())
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Closing...")
finally:
    ser.close()