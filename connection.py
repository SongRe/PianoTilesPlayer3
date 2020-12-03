import serial
class Connection():
    def __init__(self, path, frequency):
        self.serial = serial.Serial(path, frequency, timeout=1)
        self.serial.flush()
        print ("HERE")
    def sendTap(self, number):
        # if number != 1:
        #     return
        assert (number in range(1,5))
        self.serial.write(str.encode(str(number) + '\n'))
    def sendTaps(self, numbers):
        # if number != 1:
        #     return
        assert (len(numbers) == 4)
        print ("".join(map(str, numbers)))
        self.serial.write(str.encode("".join(map(str, numbers)) + '\n'))
    
    def read(self):
        # line = self.serial.readline().decode('utf-8').rstrip()
        return ""
