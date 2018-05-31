#stack plot
import matplotlib.pyplot as plt
a = [1,2,3,4,5]
b = [7,8,6,11,7]
c =   [2,3,4,3,2]
d =  [7,8,7,2,2]
e =  [8,5,7,8,13]

plt.stackplot(a,b,c,d,e)
plt.legend()
plt.show()