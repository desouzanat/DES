# Nathalia De Souza -- DES of Fast Food Takeout Queue -- 2/17/2023

import numpy as np
import DES
import matplotlib.pyplot as plt
import tabulate


np.random.seed(10)
s = DES.Simulation(float('inf'))

N = [] # each index is number of customers in the store at a given time

tArr1 = s.tArr
arrTime = [] # list of the clock times of each customer's arrival
arrTime.insert(0, tArr1)

servTime = [] # list of service times for each customer
depTime = [] # list of clock times of each customer's departure
waitTime = [] # list of wait times for each customer
watch = [] # alternative to word clock, timespan

arrN = []
newArr = []
depN = []

# initialization values 
N.append(s.N)
arrN.append(s.arrN)
depN.append(s.depN)
waitTime.append(s.totalWait)
watch.append(s.clock)

# for 5 customers
while s.depN < 6:

    # change values for the event timer, total wait timer, and clock
    s.advanceTime()

    # append lists with respective content
    N.append(s.N) 
    arrN.append(s.arrN)
    newArr.append(s.newArr)
    depN.append(s.depN)
    waitTime.append(s.totalWait)
    watch.append(s.clock)

    
    # if s.tArr not in arrTime:
    arrTime.append(s.tArr) # arrival time of an individual customer gets added to list

    # if s.tServ not in servTime:
    servTime.append(s.tServ) # service time of an individual customer gets added to list

    # if s.tDep not in depTime:
    depTime.append(s.tDep) # departure time of an individual customer gets added to list


CustDeets = zip(N, arrN, depN, waitTime, watch)
CustDeets2 = zip(arrTime, servTime, depTime)
print("\n\n")
print(tabulate.tabulate(CustDeets, headers=["# of Customers in Queue", "# of Arrivals", "# of Departures", "Total Wait Time", "Clock Time"]), "\n") 
print("\n****************************\n")
print(tabulate.tabulate(CustDeets2, headers=["Relative Arrival Time", "Service Time", "Departure Time"]), "\n") 


# plots
plt.plot(watch, N, '-o')
plt.xlabel("Time")
plt.ylabel( "Number of People")
plt.title("Number of People in Queue vs Time")
plt.show()

plt.plot(watch, waitTime, '-o')
plt.xlabel("Time")
plt.ylabel("Total Wait Time")
plt.title("Total Wait Time vs Clock Time")
plt.show()
