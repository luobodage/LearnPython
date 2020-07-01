import numpy as np 

a = np.array([[1,2],[3,4]])
b = np.array([[4,3],[2,1]])

c = np.mat(a)
d = np.mat(b)

print(c*d)
