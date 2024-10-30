import serial
# 7F 02 57 28 30 4F 31 4E 03 03 55 вкл подсветки
# 7F 02 57 28 30 4F 30 4F 03 03 54 откл подсветки
# Configure the COM port
port = "COM5"  # Replace with the appropriate COM port name
baudrate = 4800
chunk=b'\x7f'+b'\x02'+b'\x57'+b'\x28'+b'\x30'+b'\x4f'+b'\x30'+b'\x4f'+b'\x03'+b'\x03'+b'\x54'
try:
    # Open the COM port
    print("Serial connection established.")
    ser = serial.Serial(port, baudrate=baudrate, bytesize=7, parity='E', stopbits=2, timeout=1, xonxoff=False,
                        rtscts=False)

    # Adjust the parameters as needed
    # Send commands to the Arduino
    while True:
        command = input("Enter a command (e.g., 'ON', 'OFF'): ")

        # Send the command to the Arduino
       # for i in com:
        ser.write(chunk)

except serial.SerialException as se:
    print("Serial port error:", str(se))

except KeyboardInterrupt:
    pass

finally:
    # Close the serial connection
    if ser.is_open:
        ser.close()
        print("Serial connection closed.")
