import matplotlib.pyplot as plt
def plot_forecast():
    time_of_day = ['4 AM', '7 AM', '10 AM', '1 PM', '4 PM', '7PM', '10 PM']
    forecast_temp = [1, 7, 7, 8, 12, 11, 7]
    time_interval = range(1, len(time_of_day) + 1)
    plt.plot(time_interval, forecast_temp, 'o-')
    plt.xticks(time_interval, time_of_day)
    plt.show()
if __name__ == '__main__':
    plot_forecast()
