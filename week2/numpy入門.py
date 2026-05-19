import numpy as np

#(1)
a = np.ones((5,1))
print(a)

#(2)
a = np.array([[1],[1],[3.14],[1],[1]])
print(a)

#(3)
b = a.T
print(b)

#(4)
print(np.dot(a,b))

#(5)
c = np.random.rand(10,1)
print(c)

#---------

#(6)
d = np.random.normal(10, 2, (2, 5))
print(d)

#(7)
print(d[:,1])

#(8)
print(d[:,2:4])

#(9)
e = np.random.rand(5,2)
print(e)
print(d.T * e)