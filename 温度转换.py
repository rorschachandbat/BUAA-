def gettem(resist):
    A = 3.90802e-3
    B = -5.80195e-7
    C = -4.183e-12
    fT0 = (resist / 1000 - 1) / A
    if resist >= 18.52 and resist<1000:
        for i in range(50):
            fT = fT0 + (resist - 1000 * (1 + A * fT0 + B * fT0 * fT0 - 100 * C * fT0 * fT0 * fT0 + C * fT0 * fT0 * fT0 * fT0)) /(1000 * (A + 2 * B * fT0 - 300 * C * fT0 * fT0 + 4 * C * fT0 * fT0 * fT0))
            if abs(fT-fT0)<0.001:
                return fT
            else:
                fT0=fT
    elif resist >= 1000 and resist <= 1270:
        for i in range(50):
            fT = fT0 + (resist - 1000 * (1 + A * fT0 + B * fT0 * fT0)) / (1000 * (A + 2 * B * fT0))
            if abs(fT-fT0)<0.001:
                return fT
            else:
                fT0=fT
    else:
        return 'wrong'

x=eval(input())
print(gettem(x))