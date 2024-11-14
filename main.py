import serial


port = "/dev/ttyUSB0"
baudrate = 4800
# Open the COM port
ser = serial.Serial(
    port,
    baudrate=baudrate,
    bytesize=7,
    parity="E",
    stopbits=2,
    timeout=1,
    xonxoff=False,
    rtscts=False,
)


def translate_hex(topaz_command):
    byte_values = bytes.fromhex(topaz_command)
    return byte_values


def TURN_LED():
    """Turning the light by inputed command"""
    try:
        command = input("Enter a command (e.g., 'ON', 'OFF'): ")
        # for i in com:
        print(command)
        if str(command) == "ON":
            light_on = translate_hex("7F 02 57 28 30 4F 31 4E 03 03 55")
            ser.write(light_on)
        elif str(command) == "OFF":
            light_off = translate_hex("7F 02 57 28 30 4F 30 4F 03 03 54")
            ser.write(light_off)

    except serial.SerialException as se:
        print("Serial port error:", str(se))

    except KeyboardInterrupt:
        pass

while True:
    TURN_LED()
