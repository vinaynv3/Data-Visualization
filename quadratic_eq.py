import matplotlib.pyplot as plt

def draw_graph(x,y):
    plt.plot(x,y, marker='o')
    plt.xlabel('X values')
    plt.ylabel('y values')
    plt.title('Quadratic equation')
    plt.show()

if __name__=='__main__':
    x_list=range(-100,100,20)
    y_values=[]
    for x in x_list:
        y=x**2+2*x+1
        y_values.append(y)
        print('x={0} y={1}'.format(x,y))
    draw_graph(x_list,y_values)
