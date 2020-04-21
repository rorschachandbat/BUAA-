import math
import csv


def gettem(resist):
    A = 3.90802e-3
    B = -5.80195e-7
    C = -4.183e-12
    fT0 = (resist / 1000 - 1) / A
    if resist >= 18.52 and resist < 1000:
        for i in range(50):
            fT = fT0 + (resist - 1000 * (1 + A * fT0 + B * fT0 * fT0 - 100 * C * fT0 * fT0 * fT0 + C * fT0 * fT0 * fT0 * fT0)) / (1000 * (A + 2 * B * fT0 - 300 * C * fT0 * fT0 + 4 * C * fT0 * fT0 * fT0))
            if abs(fT-fT0) < 0.001:
                return fT
            else:
                fT0 = fT
    elif resist >= 1000 and resist <= 1270:
        for i in range(50):
            fT = fT0 + (resist - 1000 * (1 + A * fT0 + B * fT0 * fT0)) / (1000 * (A + 2 * B * fT0))
            if abs(fT-fT0) < 0.001:
                return fT
            else:
                fT0 = fT
    else:
        return 'wrong'


fo = open('data.txt', 'r')
text = fo.read()

fo.close()

data = list(map(eval, text.split(',')))
# print(len(data))

for i in range(31):
    data[i] = data[i]*1000
temp = []
tempH = gettem(data[31]*1000)
tempround = []
x = []
y = []
xx = []
yy = []
xy = []

for i in data[:31]:
    j = gettem(i)
    if j == 'wrong':
        print('你输入的电阻值有问题')
        break
    else:
        temp.append(j)

# print(len(temp))
for i in range(30):
    tempround.append((temp[i]+temp[i+1])/2)
    x.append(tempround[i]-tempH)
    y.append((temp[i+1]-temp[i])/60)
    xx.append(x[i]*x[i])
    yy.append(y[i]*y[i])
    xy.append(x[i]*y[i])

xr = sum(x)/30
yr = sum(y)/30
xxr = sum(xx)/30
yyr = sum(yy)/30
xyr = sum(xy)/30

# print(yy)
print(tempH)
print(temp)
# print(xr,yr,xxr,yyr,xyr)
# print(len(x),len(y),len(xx),len(yy),len(xy))
b = (xr*yr-xyr)/(xr**2-xxr)
a = yr-b*xr
r = (xyr-xr*yr)/math.sqrt(abs((xxr-xr**2)*(yyr-yr**2)))

with open('result.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['时间/min', '温度', 'x', 'y', 'x*x', 'y*y(10e-6),x*y(10e-3)'])
    for i in range(30):
        w.writerow([str(i), str(tempround[i]), str(x[i]), str(y[i]), str(xx[i]), str(yy[i]*10e5), str(xy[i]*10e2)])
    w.writerow(['平均值', ' ', str(xr), str(yr), str(xxr), str(yyr), str(xyr)])
    w.writerow(['a:'+str(a), 'b:'+str(b), 'r:'+str(r)])
    w.writerow('转换的温度')
    for i in range(31):
        w.writerow([str(i), str(temp[i])])
    w.writerow(['还有最后一步没有算，因为考虑到要算那个值还要再输入四个数据，只为了这一步增加你的工作量不划算，所以就请你自己算出来吧！！'])

