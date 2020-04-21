
# -*- coding: utf-8 -*-

"""

Created on Wed Jun 20 17:09:13 2018



@author: 96jie

"""

 

#导入cv模块

import numpy as np

import matplotlib as mpl

import matplotlib.pyplot as plt

 

#数据

a = np.random.standard_normal((1, 500))

x = np.arange(0,50,0.1)

y = np.arange(20,120,0.2)

y = y - a*10

y = y[0]

 

 

#梯度下降

def Optimization(x,y,theta,learning_rate):

    for i in range(iter):

        theta = Updata(x,y,theta,learning_rate)

    return theta

 

def Updata(x,y,theta,learning_rate):

    m = len(x)

    sum = 0.0

    sum1 = 0.0

    alpha = learning_rate

    h = 0

    for i in range(m):

        h = theta[0] + theta[1] * x[i]

        sum += (h - y[i])

        sum1 += (h - y[i]) * x[i]

    theta[0] -= alpha * sum / m 

    theta[1] -= alpha * sum1 / m 

    return theta

 

#数据初始化

learning_rate = 0.001

theta = [0,0]

iter = 1000

theta = Optimization(x,y,theta,learning_rate)

 

plt.rcParams['font.sans-serif']=['SimHei']

plt.rcParams['axes.unicode_minus'] = False



plt.figure(figsize=(35,35))

plt.scatter(x,y,marker='o')

plt.xticks(fontsize=40)

plt.yticks(fontsize=40)

plt.xlabel('特征X',fontsize=40)

plt.ylabel('Y',fontsize=40)

plt.title('样本',fontsize=40)

plt.savefig("样本.jpg")



#可视化

b = np.arange(0,50)

c = theta[0] + b * theta[1]

 

plt.figure(figsize=(35,35))

plt.scatter(x,y,marker='o')

plt.plot(b,c)

plt.xticks(fontsize=40)

plt.yticks(fontsize=40)

plt.xlabel('特征X',fontsize=40)

plt.ylabel('Y',fontsize=40)

plt.title('结果',fontsize=40)

plt.savefig("结果.jpg")
