from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def hill_climb(expr):
    def f(x,y):
        g=eval(expr)
        return g
    current=(np.random.uniform(-2,2),np.random.uniform(-2,2))
    stp=0.01
    flg=True
    print('value',f(current[0],current[1]))
    while(flg):
        cur_val=f(current[0],current[1])
        if f(current[0]+stp,current[1])>cur_val:
            current=(current[0]+stp,current[1])
        elif