#Refactoring classes
from read_files import *
from multiline_graph import multi_line_graph
from pie_chart import pie_ct
from Hist_3d_graph import hist_graph

#main
if __name__=='__main__':

    #Readind Data
    data=read_data('Hurricanes.csv')
    data_2=reading_yearly_data('Hurricanes.csv')
    sum_of_storms=[sum(data_2[0]),sum(data_2[1]),sum(data_2[2]),sum(data_2[3]),sum(data_2[4]),sum(data_2[5]),
                   sum(data_2[6]),sum(data_2[7])]


    #Graphs
    #multi_line_graph(data_2)           #line graph
    #pie_ct(data[0],sum_of_storms)      #pie chart
    hist_graph(sum_of_storms)         #3D-Histograph
