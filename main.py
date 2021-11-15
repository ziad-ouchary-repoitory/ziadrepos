import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()


portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")


for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInstance = serial.Serial(portVar, 9600, timeout = 1)

time.sleep(2)
""" while True:
    i = input("input (on/off): ").strip()
    if i == 'done':
        print('finished program')
        break
    serialInstance.write(i.encode())
    time.sleep(0.5)
    print(serialInstance.readline().decode('ascii')) """

serialInstance.write("on".encode())

serialInstance.close()