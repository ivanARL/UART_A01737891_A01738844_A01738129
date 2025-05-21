import serial
import time

# Configuración del puerto UART
ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

mensajes = []

try:
    while len(mensajes) < 7:
        x = ser.readline().decode('utf-8').strip()
        if x:
            mensajes.append(x)

    for m in mensajes:
        print(m)
        time.sleep(3)

finally:
    ser.close()
