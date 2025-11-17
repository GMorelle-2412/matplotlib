from pylab import*

xlim(0,20)
ylim(2,4)

x=[5]
y=[3]

for i in range(5,25):
    x.append(i)
    
    if i == 15:
        y.append(5)
    else:
        y.append(3)

plot(x,y,'*b')

show()