
import numpy as np
import random as ran

class Simulation:
    def __init__(self,T):
        
        # system states
        self.N = 0
        self.T = T

        # simulation variables
        self.clock = 0

        # event list
        self.tArr = self.genArr()
        self.tDep = T
        # self.tSer = self.genService()

        # statistical counters
        self.arrN = 0
        self.depN = 0
        self.totalWait = 0.0


    def advanceTime(self):
        # which will happen first: next customer's arrival or previous custonmer's departure?
        tEvent = min(self.tArr, self.tDep) 
        self.totalWait += (self.N * (tEvent - self.clock))
        self.clock = tEvent # update time

        # determine if we need to handle an arrival or a departure and calculate th service time
        if self.tArr < self.tDep:
            self.handleArr()
        else: self.handleDep()
        # pass


    
    def handleArr(self):
        self.arrN += 1 # update arrivals
        self.N += 1 # update customers
        
        if self.N <= 1:
            self.tServ = self.genService() # how long the next service will take
            self.tDep = self.clock + self.tServ # clock time when customer will depart

        # if there are less than 6 arrivals, the next arrival time is inifinity
        if self.arrN < 6:
            self.newArr = self.genArr() # the time between previous and next arrival/relative arrival time
            self.tArr = self.clock + self.newArr # clock time when next customer will arrive
        else: self.tArr = self.T

    
    def handleDep(self):
        self.depN += 1 # update departures
        self.N -= 1 # update queue length

        # if there are more than 0 customers in the store
        if self.N > 0:
            # generate a new service and departure time
            self.tServ = self.genService() # relative departure time
            self.tDep = self.clock + self.tServ
        # if there are 0 customers in store, the clock time for next departure is infinity
        else: 
            self.tDep = self.T


        
    def genArr(self): # generates random arrival time
        return np.random.exponential(1./3)


    def genService(self): # generates random service time
        return np.random.exponential(1./4)