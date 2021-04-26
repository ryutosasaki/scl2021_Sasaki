#!/usr/bin/env python
# coding: utf-8

# # Pythonゼミ
# # 12. 偏微分方程式 その２
# 2021-4-26 佐々木 瑠斗

# C++のソースコードをPythonに変換

# In[6]:


import math

N  =  300
ex  =  []
hy  =  []

T = input()
T = int(T) #strからintに変換

for i in range(0,N,1):
    ex.append(0) #リストに要素を追加
    hy.append(0)
    
ex = list(map(float,ex)) #リストの要素をfloatに変換

for t in range(1,T+1,1):
    for i in range(1,N,1):
        ex[i] = ex[i] + (hy[i-1] - hy[i])/2
        
    ex[int(N/2)] = math.exp(-0.5*(40-t)*(40-t)/144)
    
    for i in range(0,N-1,1):
        hy[i] = hy[i] + (ex[i] - ex[i+1])/2
        
for i in range(0,N,1):
    print(i,ex[i])


# 可視化を行った

# In[7]:


import math
import numpy as np
import matplotlib.pyplot as plt

N  =  300
T = []
cmap = plt.get_cmap("tab10") #カラーマップ
plt.figure(figsize=(12,9)) #表示する図の大きさ

for j in range(0, 10, 1):
    ex  =  []
    hy  =  []
    T.append((j+1)*20) #20から20刻みでリストに要素を追加
    
    for i in range(0,N,1):
        ex.append(0) #リストに要素を追加
        hy.append(0)
    
    ex = list(map(float, ex)) #リストの要素をfloatに変換

    for t in range(1, T[j]+1, 1):
        for i in range(1,N,1):
            ex[i] = ex[i] + (hy[i-1] - hy[i])/2
        
        ex[int(N/2)] = math.exp(-0.5*(40-t)*(40-t)/144)
    
        for i in range(0,N-1,1):
            hy[i] = hy[i] + (ex[i] - ex[i+1])/2
            
    x = np.linspace(0, N, N)
    plt.plot(x, ex, color = cmap(j), label =T[j] ) #プロットを描画
    plt.legend()
plt.show()

