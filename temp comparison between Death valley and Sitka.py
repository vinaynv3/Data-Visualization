import matplotlib.pyplot as plt
from datetime import  datetime
import csv
def get_data(file,dates,high,low):
    with open(file) as f:
        read=csv.reader(f)
        header_row=next(read)
    #for index,row in enumerate(header_row):
        #print(1+index, row
    #dates,high,low=[],[],[]
        for row in read:
            try:
                current_date=datetime.strptime(row[0],"%Y-%m-%d")

                h=int(row[1])
                l=int(row[3])
            except ValueError:
                print(current_date,'missing data')

            else:
                dates.append(current_date)
                high.append(h)
                low.append(l)

dates,high,low=[],[],[]
get_data('sitka_weather_2014.csv',dates,high,low)

fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,high,c='red',alpha=0.4)
plt.plot(dates,low,c='blue',alpha=0.4)
plt.fill_between(dates,high,low, facecolor='grey', alpha=0.8)


dates,high,low=[],[],[]
get_data('death_valley_2014.csv',dates,high,low)

plt.plot(dates,high,c='red',alpha=0.2)
plt.plot(dates,low,c='blue',alpha=0.2)
plt.fill_between(dates,high,low, facecolor='grey', alpha=0.4)
plt.title('Daily temperature in Death Valley and Sitka(2014)')
plt.xlabel('YEAR 2014')
fig.autofmt_xdate()
plt.ylabel('Temperature in F')
plt.tick_params(axis='both', which='major', labelsize=14)
plt.ylim(10,120)
plt.show()


