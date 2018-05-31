#pie chart
import matplotlib.pyplot as plt
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,labels=activities,colors=cols,shadow=True,startangle=90)
plt.show()