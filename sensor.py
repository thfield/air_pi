import serial, time
#from Adafruit_IO import Client
#aio = Client('your-adafruit-username', 'adafruit-key')

ser = serial.Serial('/dev/ttyUSB0')

timeout = 0
while timeout < 6:
    data = []
    for index in range(0,10):
        datum = ser.read()
        data.append(datum)
    
    pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
    pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
    #aio.send('kingswoodtwofive', pmtwofive)
    #aio.send('gingswoodtwofice',pmtem)
    print((pmtwofive,pmten))
    timeout += 1
    time.sleep(10)
