import numpy as np

def smoothingfunc(points,a,b,c):
    #print(this.a,this.b,this.c)
    x_values = np.linspace(0, 2*np.pi, points)
    #return this.a*np.sin(x_values)+this.b*np.cos(x_values)+this.c
    return a*np.sin(x_values)+b*np.cos(x_values)+c