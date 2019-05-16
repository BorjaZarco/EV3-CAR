class LineSensor():
    def __init__(self, left_sensor, rigth_sensor):
        self.left_sensor = left_sensor
        self.rigth_sensor = rigth_sensor
        self.left_sensor.mode = 'COL-REFLECT'
        self.rigth_sensor.mode = 'COL-REFLECT'

    def getMovement(self):
        whiteLeft = self.left_sensor.value()
        whiteRight = self.rigth_sensor.value()
        k = 2
        leftTurn = 0
        rightTurn = 0
        if whiteLeft > 10:
            rightTurn = k*40 if (whiteLeft > 45) else k*(whiteLeft - 10)
        if whiteRight > 10:
            leftTurn = -k*40 if (whiteRight > 45) else -k*(whiteRight - 10)
        return rightTurn if (abs(rightTurn) > abs(leftTurn)) else leftTurn


class Direction():
    def __init__(self, motor):
        self.initial_position = motor.position
        self.motor = motor

    def steerToDeg(self, deg):
        desired_position = self.initial_position + deg
        if abs(abs(self.motor.position) - abs(desired_position)) > 10:
            self.motor.run_to_abs_pos(position_sp=desired_position, speed_sp=200)
