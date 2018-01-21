from matplotlib import pyplot as vin
import math
def draw_graph(x,y):
    vin.plot(x,y)
    vin.xlabel('x Cordinate')
    vin.ylabel('y cordinate')
    vin.title('Projectile motion of ball')

def f_range(start,last,interval):
    numbers=[]
    while start<last:
        numbers.append(start)
        start=start+interval
    return numbers

def trajectory(u,theta):
    theta=math.radians(theta)
    g=9.8
    t_flight=2*u*math.sin(theta)/g
    intervals=f_range(0,t_flight,0.001)
    x=[]
    y=[]
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t-0.5*g*t*t)
    draw_graph(x,y)

if __name__=='__main__':
    list=[20,40,60]
    theta=60
    for u in list:
        trajectory(u,theta)
    vin.legend(['20','40','60'])
    vin.show()
