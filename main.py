from pylab import*

xlim(0,20)
ylim(2,4)

x=[5]
y=[3]

for i in range(5,15):
    x.append(i)
    y.append(3)

plot(x,y,'*b')

show()