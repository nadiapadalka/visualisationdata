
import matplotlib.pyplot as plt

import csv

#initiliasing class with Weather data
class Weather:
    def __init__(self, date, temperature, atm, cloudy, num_of_rain):
        self.date = date
        self.temperature = temperature
        self.atm = atm
        self.cloudy = cloudy
        self.num_of_rain = num_of_rain
        self.year, self.month, self.day = self.date.split("/")


    #less than operator
    def __lt__(self, other):
        return self.date< other.date
    #print out data
    def __str__(self):
        return f'{self.date} {self.temperature} {self.atm} {self.cloudy} {self.num_of_rain} '
results = []
#defining a function in order to read from csv file
def read_from(file):
 with open(file, 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        s1 = Weather(line[0], int(line[1]), int(line[2]), line[3], int(line[4]))
        results.append(s1)

read_from('res1.csv')
read_from('res2.csv')
#sorting a list
sort_res = sorted(results)
my_iter = iter(sort_res)
for my_iter in sort_res:
    print(my_iter)
#task2
#we had to build a plot for every month where days and their atm are parameters
fig1 = plt.figure()
set_months = set()
for i in sort_res:
    set_months.add(int(i.month))
for month in set_months:
    dict_m_d=dict()
    for i in sort_res:
        if int(i.month) == month:
            dict_m_d[int(i.day)] = i

    x = []
    y = []
    z = []
    for el in dict_m_d:
        x.append(int(dict_m_d[el].day))
        y.append(int(dict_m_d[el].atm))
        z.append(dict_m_d[el].cloudy)
    x = sorted(x)
    plt.plot(x, y, color='green')
    plt.grid()
    plt.show()
#building a sector diagram for every month  for see the cloudy
    plt.pie(x, labels=z)
    plt.show()