from math import exp

def sigmoid(x):
    return (exp(0.075*x+0.3) / (exp(0.075*x + 0.01) + 4.7 )) - 0.36

def getSpeed(distance):
    # speed = round((72440 + (- 72530)/(1 + (distance/407000000000)**0.265))/100, 3)
    # print(str(speed))
    if distance <= 6:
        return -0.25
    elif (distance < 9 and distance > 6): 
        return 0
    else:
        return round(sigmoid(distance), 3)