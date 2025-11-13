'''
Created on Sep 8, 2015

@author: karurosu
'''

import random
import math
import os

class BaseOptimiser(object):
    '''
    Basic class for implementing the optimiser
    '''


    def __init__(self, data, t0 = 1000.0, alpha = 0.99, limit = 0.00001):
        '''
        Constructor
        '''
        self.temp = t0
        self.alpha = alpha
        self.limit = limit
        self.data = data
        self.budget = 0
        
    def value(self, item):
        raise NotImplementedError()
    
    def size(self, item):
        raise NotImplementedError()
    
    def random(self):
        raise NotImplementedError()
    
    def neighbor(self, item):
        raise NotImplementedError()
    
    def optimise(self, budget, log):
        
        print "Saving log at", os.path.abspath(log)
        logf = open(log, "w")
        logf.write("iteration,temp,current value,best value\n")
        
        
        self.budget = budget
        t = self.temp
        c = self.random()
        
        best = c
        best_value = self.value(best)
        
        iteration = 0
        logf.write("{0},{3},{1},{2}\n".format(iteration, float(best_value), float(best_value),t))
        
        
        while t > self.limit:
            iteration += 1
            n = self.neighbor(c)
            
            if n is None:
                n = self.random()
            
            value_c = self.value(c)
            value_n = self.value(n)
            
            logf.write("{0},{3},{1},{2}\n".format(iteration, float(value_n), float(best_value),t))
            
            if best_value < value_n:
                best = n
                best_value = value_n
            
            if value_n > value_c:
                c = n
            else:
                if random.uniform(0,1) < math.exp((value_n - value_c)/t):
                    c = n
            
            t = t * self.alpha
        
        print "Stopped after",iteration,"iterations"
        logf.close()
        
        return best