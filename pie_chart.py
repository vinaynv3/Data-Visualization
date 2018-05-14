import matplotlib.pyplot as plt


#pie chart
def pie_ct(months,total):
    month = months
    values = total
    colors = ['green', 'red', 'yellow', 'blue','pink','brown','violet','cyan']

    #autopct function
    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
        return my_autopct

# plotting pie chart
    plt.pie(values, labels = month, colors=colors,
            startangle=70, shadow = True, explode = (0.1, 0, 0, 0,0,0,0,0),
            radius = 1.1, autopct = make_autopct(values))
    plt.title('Total monthly perentage of storms from 2005 to 2015\n')
    plt.legend()
    plt.show()
