def GigawattPower(batteryOne, batteryTwo, gigawattTarget):
    res = dict()
    for i in batteryOne:
        res[gigawattTarget - i]=gigawattTarget - i

    for j in batteryTwo:
        if j in res:
            return True

    return False

GigawattPower