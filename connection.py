import serial
class Connection():
    def __init__(self, path, frequency):
        self.serial = serial.Serial(path, frequency, timeout=1)
        self.serial.flush()
    def sendTap(self, number):
        assert (number in range(1,5))
        self.serial.write(str.encode(str(number) + '\n'))