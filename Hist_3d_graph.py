# modules
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

# Histograph function
def hist_graph(total):

    style.use('ggplot')
    fig = plt.figure()

    #subplot figure
    ax1 = fig.add_subplot(111, projection='3d')

    #x, y, z co-ordinates
    x = [5,6,7,8,9,10,11,12]
    y = [1,2,3,4,5,6,7,8]
    z = np.zeros(8)


    #bar sizes
    dx = np.ones(8)              # length along x-axis
    dy = np.ones(8)              # length along y-axs
    dz = np.array(total)         # height of bar


    #setting color scheme
    color = []
    for h in dz:
        if h >10:
            color.append('g')
        else:
            color.append('b')

# plotting the bars
    ax1.bar3d(x, y, z, dx, dy, dz, color = color)

# setting axes labels
    ax1.set_title('Total Tropical storms')
    ax1.set_xlabel('Months in Numbers')
    ax1.set_ylabel('y-axis')
    ax1.set_zlabel('Total Storms')

    plt.show()
