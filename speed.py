def getSpeed(distance):
    speed = round((72440 + (- 72530)/(1 + (distance/407000000000)**0.265))/100, 3)
    # print(str(speed))
    if speed > 1:
        return 1
    elif speed < -1: 
        return -1
    elif distance < 4:
        return -0.25
    elif (distance < 9 and distance > 6): 
        return 0
    else:
        return speed