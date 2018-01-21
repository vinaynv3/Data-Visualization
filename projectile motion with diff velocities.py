import matplotlib.pyplot as plt
import math
g=9.8

def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel('x co-ordinate')
    plt.ylabel('y co-ordinate')
    plt.title('Projectile motion with different velocities')



def frange(start,final,interval):
    num=[]
    while start<final:
        num.append(start)
        start=start+interval
    return num

def draw_trajectory(u,theta,t_flight):
    x=[]
    y=[]
    intervals=frange(0,t_flight,0.001)
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t-0.5*g*t*t)
    draw_graph(x,y)

if __name__=='__main__':
    num_trj=int(input('Enter number of trajectory: '))
    velocity=[]
    angle=[]
    for i in range(1,num_trj+1):
        v=input('Please enter initial velocity(m/s) {0}: '.format(i))
        theta=input('Please enter the angle(Degree) {0}: '.format(i))
        velocity.append(float(v))
        angle.append(math.radians(float(theta)))

    for i in range(num_trj):
        t_flight=(2*velocity[i]*math.sin(angle[i]))/g
        S_x=velocity[i]*math.cos(angle[i])*t_flight
        S_y=(velocity[i]*math.sin(angle[i])*t_flight)-(1/2)*g*(t_flight/2)**2
        print('Initial velocity: {0} and Angle of projection: {1} '.format(velocity[i],math.degrees(angle[i])))
        print('T: {0} Sx:{1} Sy:{2}'.format(t_flight,S_x,S_y))
        print()
        draw_trajectory(velocity[i],angle[i],t_flight)

    legends=[]
    for i in range(0, num_trj):
        legends.append('{0} - {1}'.format(velocity[i], math.degrees(angle[i])))
    plt.legend(legends)
    plt.show()


