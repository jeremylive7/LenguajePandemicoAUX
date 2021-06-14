import random

def caracoles(sms):
    almacen_sms = sms
    caracolA = 0
    caracolB = 0
    caracolC = 0
    largo = len(sms)
    largo = largo - 1
    flag = 0
    parada = 1
    pasos_posibles = 3
    while flag != parada  :
        pasosA = random.randint(0,pasos_posibles)
        pasosB = random.randint(0,pasos_posibles)
        pasosC = random.randint(0,pasos_posibles)
        caracolA = caracolA + pasosA
        caracolB = caracolB + pasosB
        caracolC = caracolC + pasosC
        if caracolA > largo  :
            flag = True
        if caracolB > largo  :
            flag = True
        if caracolC > largo  :
            flag = True
        if flag != True  :
            sms = almacen_sms
            sms = list(sms)
            sms[caracolA] = "A"
            sms[caracolB] = "B"
            sms[caracolC] = "C"
            sms = "".join(sms)
        print(sms)
    return sms
caracoles('-------------')