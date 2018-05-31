#bar graph
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
x_val=[5,6,3,7,6]

plt.bar(x,x_val,label='bar')
plt.legend()
plt.show()