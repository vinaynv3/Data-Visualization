from random import choice




class walks():
    def __init__(self,num_wk=400):
        self.num_wk=num_wk

        self.x_t=[0]
        self.y_t=[0]

    def get_step(self):
        direction=choice([-1,1])
        distance=choice([0,1,2,3,4,5,6])
        step=direction*distance
        return step

    def st_wk(self):
        while len(self.x_t)<self.num_wk:
            x_tot=self.get_step()

            y_tot=self.get_step()

            if x_tot==0 and y_tot==0:
                continue

            next_x=self.x_t[-1]+x_tot
            next_y=self.y_t[-1]+y_tot

            self.x_t.append(next_x)
            self.y_t.append(next_y)





