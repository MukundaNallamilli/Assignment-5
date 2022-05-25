from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-20,30,num=100)
y = np.linspace(0,0,num=100)

x1 = np.linspace(0,15,num=25)
y1 = np.linspace(5,5,num=25)

x2 = np.linspace(15,15,num=25)
y2 = np.linspace(0,8,num=25)

x3 = np.linspace(0,0,num=25)
y3 = np.linspace(-7,0,num=25)

x7 = np.linspace(0,0,num=25)
y7 = np.linspace(5,15,num=25)

x6 = np.linspace(0,0,num=25)
y6 = np.linspace(0,5,num=25)

x4 = np.linspace(15,30,num=25)
y4 = np.linspace(8,8,num=25)

x5 = np.linspace(-20,0,num=25)
y5 = np.linspace(0,0,num=25)

plt.figure(num= 0,dpi=90)
plt.text(27,-1,"x")
plt.gca().axes.get_yaxis().set_visible(False)
plt.gca().axes.get_xaxis().set_visible(False)
plt.text(-3,14,"F(x)")
plt.text(0,-1,'0')
plt.text(0,8,'-')
plt.text(15,-1,'1')
plt.text(-2.5,8,'1')
plt.text(-2.5,5,'q') 
plt.plot(x1,y1,color='r')
plt.plot(x,y,color='g')
plt.plot(x2,y2,'--',color='r')
plt.plot(x3,y3,color='g')
plt.plot(x7,y7,color='g')
plt.plot(x4,y4,color='r')
plt.plot(x5,y5,color='r')
plt.plot(x6,y6,'--',color='r')
plt.title("(cumulative distribution)")
plt.show()