from ev3dev2.led import Leds

class LED():
    def __init__(self):
        self.leds = Leds()
        self.flag = 0

    def updateLeds(self):
        if self.flag == 20:
            self.flag = 0

        if self.flag < 10:
            self.leds.set_color('LEFT', 'RED')
            self.leds.set_color('RIGHT', 'GREEN')
        else:
            self.leds.set_color('LEFT', 'GREEN')
            self.leds.set_color('RIGHT', 'RED')

        self.flag += 1
