from time import *
from serial import *

def worker(conn,ser):
    n = 0

    while True:
        sizeRead = ser.read(32)

        if sizeRead > 0:
            pass    #@todo implement logic lol

        if conn.poll(): #check to see if we have anything in here... if so, read it and parse as required
            msg = child_conn.recv()
            print msg
            ser.write("a")

        if n == 50:
            n = 0 #reset
            #poll SRRI

        sleep(.005)




if __name__ == '__main__':
    ser = Serial()

    ser.port = 8
    ser.baudrate = 115200
    ser.parity   = PARITY_NONE
    ser.stopbits = STOPBITS_ONE
    ser.bytesize = EIGHTBITS
    ser.timeout  = 0  # non-blocking mode, return immediately in any case, returning zero or more, up to the requested number of bytes
    ser.open()

    parent_conn, child_conn = Pipe()
    t = Thread(target=worker, args=(child_conn,ser,))
    t.start()

    while True:
        sleep(1)
        parent_conn.send([42, None, 'hello'])




