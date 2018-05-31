#simple line graph
import matplotlib.pyplot as plt 
x = [1,2,3,4,5]
y = [3,4,5,6,7]

x2=[4,2,5,3,6]
y2=[2,5,3,4,6]

plt.plot(x,y,label='case1')
plt.plot(x2,y2,label='case2')
plt.xlabel('time')
plt.ylabel('distance')
plt.title('time vs distance')
plt.legend()
plt.show()