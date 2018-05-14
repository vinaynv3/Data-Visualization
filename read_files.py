import csv


#Extractind data from csv
def read_data(filename):

    months=[]
    avg=[]
    with open(filename) as f:
        file=csv.reader(f)
        next(file)
        for line in file:
            months.append(line[0])
            avg.append(line[1])
        return months,avg


#yearly hurricane data from 2005 to 2015
def reading_yearly_data(filename_2):
    y_2005,y_2006,y_2007,y_2008,y_2009,y_2010,y_2011,y_2012,y_2013,y_2014,y_2015=[],[],[],[],[],[],[],[],[],[],[]
    with open(filename_2) as f:
        file_2=csv.reader(f)
        next(file_2)
        for line in file_2:
            y_2005.append(int(line[2]))
            y_2006.append(int(line[3]))
            y_2007.append(int(line[4]))
            y_2008.append(int(line[5]))
            y_2009.append(int(line[6]))
            y_2010.append(int(line[7]))
            y_2011.append(int(line[8]))
            y_2012.append(int(line[9]))
            y_2013.append(int(line[10]))
            y_2014.append(int(line[11]))
            y_2015.append(int(line[12]))

        return y_2005,y_2006,y_2007,y_2008,y_2009,y_2010,y_2011,y_2012,y_2013,y_2014,y_2015






