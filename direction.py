class LineSensor():
    def __init__(self, left_sensor, rigth_sensor):
        self.left_sensor = left_sensor
        self.rigth_sensor = rigth_sensor
        self.left_sensor.mode='COL-REFLECT'
        self.rigth_sensor.mode='COL-REFLECT'
    
    def getMovement(self):
        whiteLeft = self.left_sensor.value()
        whiteRight = self.rigth_sensor.value()
        k = 2
        if whiteLeft > 10:
            if whiteLeft > 45:
                return k*40

            return k*(whiteLeft - 10)
        elif whiteRight > 10:
            if whiteRight > 45:
                return -k*40

            return -k*(whiteRight - 10)
        return 0

class Direction():
    def __init__(self, motor):
        self.initial_position = motor.position
        self.motor = motor
    
    def steerToDeg(self, deg):
        desired_position = self.initial_position + deg
        if abs(abs(self.motor.position) - abs(desired_position)) > 10:
            self.motor.run_to_abs_pos(position_sp=desired_position, speed_sp=200)