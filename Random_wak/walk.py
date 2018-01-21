from random import choice

class RandomWalk():
    def __init__(self, num_walks=500):
        self.num_walks=num_walks

        self.x_val=[0]
        self.y_val=[0]
    def fill_walk(self):
        while len(self.x_val)<self.num_walks:
            x_dir=choice([1,-1])
            x_walk=choice([0,1,2,3,4])
            x_step=x_dir*x_walk

            y_dir=choice([1,-1])
            y_walk=choice([0,1,2,3,4])
            y_step=y_dir*y_walk

            if x_step==0 and y_step==0:
                continue

            next_xstep=self.x_val[-1]+x_step
            next_ystep=self.y_val[-1]+y_step

            self.x_val.append(next_xstep)
            self.y_val.append(next_ystep)


