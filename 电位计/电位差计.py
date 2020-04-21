import math

fo=open('data.txt','r')
text=fo.read()
R1,R2,R11,R22,R111,R222,R0,U0,Ux,t,n,cR=map(eval,text.split(','))
data=list(map(eval,text.split(',')))
dR=[]
for i in data[:7]:
    dR.append(int(i//1000%10)+int(i//100%10)*0.1+int(i//10%10)*0.02+int(i//1%10)*0.005+int((i-int(i))*10)*0.005+cR)
fo.close()
print(data)
print(dR)


fo=open('result.txt','w',encoding='utf-8')

fo.write('实验一\n')

En=1.01860-3.99*10e-5*(t-20)-0.94*10e-6*math.pow(t-20,2)+9*10e-9*math.pow(t-20,3)
fo.write('En={:.3f}\n'.format(En))

Ex=En*(R1+R2)*R11/R1/(R11+R22)
fo.write('Ex={:.3f}\n'.format(Ex))

fo.write('2.仪器误差\n')
fo.write('▲R1={:.3f}\n'.format(dR[0]))
fo.write('u(R1)=▲R1/√3={:.3f}\n'.format(dR[0]/math.sqrt(3)))

fo.write('▲R2={:.3f}\n'.format(dR[1]))
fo.write('u(R2)=▲R1/√3={:.3f}\n'.format(dR[1]/math.sqrt(3)))

fo.write('▲R1\'={:.3f}\n'.format(dR[2]))
fo.write('u(R1\')=▲R1/√3={:.3f}\n'.format(dR[2]/math.sqrt(3)))

fo.write('▲R2\'={:.3f}\n'.format(dR[3]))
fo.write('u(R2\')=▲R1/√3={:.3f}\n'.format(dR[3]/math.sqrt(3)))





fo.write('3.灵敏度\n')

S=n/(R222/1000-R22/1000)
fo.write('S={:.0f}div/({:.3f}-{:.3f})={:.3f}div/V\n'.format(n,R222/1000,R22/1000,abs(n/(R222/1000-R22/1000))))
fo.write('灵敏度误差(对Ex位置)\n')
fo.write('▲灵Ex=0.2/S={:.7f}    u灵(Ex)=▲灵Ex/√3={:.7f}V\n'.format(0.2/S,0.2/S/math.sqrt(3)))

Exx=math.sqrt((R2/R1*dR[0])**2+dR[1]**2+(R22*dR[2]/R11)**2+dR[3]**2)/(R1+R2)/math.sqrt(3)
uEx=Exx*Ex
fo.write('4.合成不确定度：\n略去En的示值误差；略去因辅助电源E和标准电池En再两次示零过程中的变化所带入的误差；略去两次示零过程中示零电路的灵敏度误差；并假定R1和R1\'，R2和R2\'相互独立，可得\n')
fo.write('u(Ex)/Ex=√(1/R1-1/R1+R2)²u²(R1)+[u(R2)/(R1+R2)]²+[1/R1\'-1(R1\'+R2\')]²u²(R1\')+[u(R2\')/(R1\'+R2\')]²\n')
fo.write('=1/(R1+R2)*√[R2/R1u(R1)]²+[u(R2)]²+[R2\'/R1\'u(R1\')]²+[u(R2\')]={:.8f}\n'.format(Exx))
fo.write('u(Ex)=Ex*u(Ex)/Ex={:.8f}\n'.format(uEx))


fo.write('5.测量的最终表达为\n')
fo.write('Ex±u(Ex)={:.3f}±{:.3f}\n'.format(Ex,uEx))

fo.write('实验二\n')
fo.write('2.固定电阻阻值\n')
Rx=Ux*R0/U0
uR0=dR[6]/math.sqrt(3)
uU0=(U0+0.01)*10e-5/math.sqrt(3)
uUx=(Ux+0.01)*10e-5/math.sqrt(3)
uRx=math.sqrt((uR0/R0)**2+(uUx/Ux)**2+(uU0/U0)**2)
fo.write('Rx=Ux*R0/U0={:.8f}\n'.format(Rx))
fo.write('3.不确定度的计算\n')
fo.write('▲R0={:.8f}\n'.format(dR[6]))
fo.write('u(R0)=▲R0/√3={:.8f}\n'.format(uR0))
fo.write('▲U0={:.8f}\n'.format((U0+0.01)*10e-5))
fo.write('u(U0)=▲U0/√3={:.8f}\n'.format(uU0))
fo.write('▲Ux={:.8f}\n'.format((Ux+0.01)*10e-5))
fo.write('u(Ux)=▲Ux/√3={:.8f}\n'.format(uUx))

fo.write('4.合成不确定度\n')
fo.write('U(Rx)/Rx={:.8f}\n'.format(uRx))
fo.write('U(Rx)=Rx*U(Rx)/Rx={:.3f}\n'.format(uRx*Rx))

fo.write('5.最终结果表达\n')
fo.write('Rx±u(Rx)=({:.4f}+{:.5f})\n'.format(Rx,uRx))

fo.close()
