'''
Created on Aug 25, 2015

@author: karurosu
'''
from fractions import Fraction
import random
from base import BaseOptimiser

class Feature(object):
    def __init__(self, name, weight = None, children = None):
        self.name = name
        self.weight = weight
        self.parent = None
        self.directory = None
        if children is None:
            self.children = []
        else:
            self.children = children
            for child in self.children:
                child.parent = self
    
    def distributeWeight(self):
        if self.parent is None:
            self.weight = Fraction(1)
        
        if self.weight is None:
            raise ValueError("Weight has not been initialized for {0}".format(self.name))
        
        if len(self.children) == 0:
            return
        
        each = self.weight / len(self.children)
        
        for child in self.children:
            child.weight = each
            child.distributeWeight()
    
    def calculateWeight(self):
        if self.weight is None:
            raise ValueError("Weight has not been initialized for {0}".format(self.name))
        
        if len(self.children) == 0:
            return self.weight
        else:
            s = Fraction(0)
            for child in self.children:
                s = s + child.calculateWeight()
            
            if s != self.weight:
                raise ValueError('Incorrect weight sum for children of {0}'.format(self.name))    
            
            return s
    
    def flatten(self):
        if len(self.children) == 0:
            return [self]
        else:
            out = []
            for child in self.children:
                out.extend(child.flatten())
            return out
    
    def index(self):
        self.index = {}
        
        pending = []
        pending.extend(self.children)
        
        while len(pending) != 0:
            next = pending.pop()
            if next.name in self.index:
                raise ValueError("Repeated feature name: "+next.name)
            self.index[next.name] = next
            pending.extend(next.children)
            
    def get(self, *args):
        out = set()
        
        for name in args:
            for f in self.index[name].flatten():
                out.add(f)
        
        return out
    
def weight(*args):
    """
    Get the weight of the passed collections, assumes that all are leaf nodes.
    each parameter must be a collection
    """
    out = Fraction(0)
    p = set()
    for arg in args:
        for e in arg:
            if e not in p:
                out += e.weight
                p.add(e)
    
    return out

class RuntimeOptimiser(BaseOptimiser):
    b = 2.0
    
    def value(self, item):
        collection = []
        for c in item:
            for tc in c:
                collection.append(tc.attributes['coverage'])
        
        return weight(*collection)
    
    def size(self, item):
        c = 0
        
        for itm in item:
            c += itm.attributes['runtime']
        
        return c
    
    def random(self):
        s = []
        acc = 0.0
        c = list(self.data)
        
        while len(c) > 0 or acc < self.budget:
            if len(c) == 0:
                break
            n = random.choice(c)
            nt = n.attributes['runtime'] + acc
            
            if nt > self.budget:
                break
            
            acc = nt
            c.remove(n)
        
        return s
    
    def neighbor(self, item):
        m = [ x for x in self.data if x not in item ]
        
        #first, attempt to add new items
        for n in m:
            item.append(n)
            if self.size(item) > self.budget:
                item.pop()
                continue
            return item
        else:
            #could not add, lets swap
            while len(m) != 0:
                copy = list(item)
                
                n = random.choice(m)
                
                if copy != []:
                    r = random.choice(item)
                    copy.remove(r)
                
                copy.append(n)
                
                if self.size(copy) > self.budget:
                    m.remove(n)
                    continue
                else:
                    return copy
        
        return None
            
            
        