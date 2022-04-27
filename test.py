import numpy as np
m1 = -1
m2 = 0.99
print(int(360/(np.arctan((m2- m1)/(1+m1*m2))*180/np.pi)))