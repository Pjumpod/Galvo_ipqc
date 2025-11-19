import serial

ser = serial.Serial('COM5', 2000000)  # Adjust 'COM5' to your actual port, #USB225 has baud rate of 2000000

while True:
    if ser.in_waiting > 0:
        data = ser.read(ser.in_waiting)
        print(data)