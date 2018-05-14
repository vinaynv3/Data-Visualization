import matplotlib.pyplot as plt
import numpy as np

#Total Monthly storm analysis
def multi_line_graph(y):

    x =np.array([5,6,7,8,9,10,11,12])

    #year 2005
    x1=x
    y1 = np.array(y[0])
    plt.plot(x1, y1, label = "2005",color='red', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='red', markersize=8)
    #year 2006
    x2 = x
    y2 = np.array(y[1])
    plt.plot(x2, y2, label = "2006", color='green', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='green', markersize=8)

    #year 2007
    x3 = x
    y3 = np.array(y[2])
    plt.plot(x3, y3, label = "2007", color='blue', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='blue', markersize=8)

    #year 2008
    x4 = x
    y4 = np.array(y[3])
    plt.plot(x4, y4, label = "2008", color='cyan', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='cyan', markersize=8)

    #year 2009
    x5 = x
    y5 = np.array(y[4])
    plt.plot(x5, y5, label = "2009", color='violet', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='violet', markersize=8)

    #year 2010
    x6 = x
    y6 = np.array(y[5])
    plt.plot(x6, y6, label = "2010", color='orange', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='orange', markersize=8)

    #year 2011
    x7 = x
    y7 = np.array(y[6])
    plt.plot(x7, y7, label = "2011", color='brown', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='brown', markersize=8)

    #year 2012
    x8 = x
    y8 = np.array(y[7])
    plt.plot(x8, y8, label = "2012", color='yellow', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='yellow', markersize=8)

    #year 2013
    x9 = x
    y9 = np.array(y[8])
    plt.plot(x9, y9, label = "2013", color='pink', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='pink', markersize=8)

    #year 2014
    x10 = x
    y10 = np.array(y[9])
    plt.plot(x10, y10, label = "2014", color='black', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='black', markersize=8)

    #year 2015
    x11 = x
    y11 = np.array(y[10])
    plt.plot(x11, y11, label = "2015", color='blue', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='blue', markersize=8)

    plt.xlabel('May to December')
    plt.ylabel('Total')
    plt.title('Total Tropical storms from 2005 to 2015')
    plt.legend()
    plt.show()
