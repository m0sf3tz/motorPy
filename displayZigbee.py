import serial
import matplotlib.pyplot as plt

TOTAL_BLOCKS_TO_SEND = 20

ser = serial.Serial()
ser.baudrate = 57600
ser.port = 'COM7'
ser.close()
ser.open()


arrOuter = []
for I in range(0,TOTAL_BLOCKS_TO_SEND):
    buf0 = ser.read(256);
    arrInner = []
    arr = []
    arr16 = []
    for x in range (0,128):
        lsb = int( format(ord(buf0[2*x]), 'd')    )
        msb = int( format(ord(buf0[2*x+1]), 'd')  )

        num = msb << 8 | lsb
        num = (num*2.0/0xfff0)*2.5
        arr16.append( num)


    arrOuter.append(arr16)

ser.close()

completeData = []
incrementAxis = []

for x in arrOuter:
    completeData.extend(x)

count = 0;
for elm in completeData:
    cout = count + 1
    incrementAxis.append(count)

plt.ylim(0, 5)

plt.plot(completeData)
plt.ylabel('some numbers')
plt.show()


1
