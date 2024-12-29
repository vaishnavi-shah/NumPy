import numpy as np

# Get the datatype of a NumPy array with integer
n = np.array([10,20,30])
print(n)
print(n.dtype)

# Get the datatype of NumPy array with string
q = np.array(["vaishnavi","clifton"])
print(q)
print(q.dtype)

# Set the datatype size within a NumPy array
p = np.array(["hindi","english","marathi","maths","science"],dtype='S5')
print(p)
print(p.dtype)

# Convert one datatype to another
r = np.array(['10','20','30','40','50'])
print(r)
print(r.dtype)

c = r.astype('i')
print(c)
print(c.dtype)






