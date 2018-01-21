import matplotlib.pyplot as plt
from walk import RandomWalk
while True:
    rw=RandomWalk(50000)
    rw.fill_walk()
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_walks))
    plt.scatter(rw.x_val, rw.y_val, c=point_numbers, cmap=plt.cm.Blues,
    edgecolor='none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=15)
    plt.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolors='none',
    s=15)
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)
    plt.title('Person taking random 500 steps')
    plt.xlabel('Direction')
    plt.ylabel('Steps')
    plt.show()

    keep_running=input("you want take another random walk(Y/N)")
    if keep_running=='N':
        break
