'''
Created on Aug 21, 2015

@author: karurosu
'''

import basic

class WorldSolver(object):
    '''
    This class is a simple backtracking  solver that attempts to take a set of conditions and create a compatible world
    '''

    def __init__(self, world):
        '''
        Constructor
        '''
        
        self.world = world
        
    
    def add(self, conditions):
        #check if any of the negative conditions is in the world, if it is, we cannot do anything
        pending = []
        negated = []
        
        for condition in conditions:
            if condition.negated:
                negated.append(condition)
                if condition in self.world.status:
                    print "Negative condition is already in the world", condition
                    return False
                continue
            
            if condition in self.world.status:
                continue
            else:
                pending.append((condition,self.expand(condition)))
        
        pending.sort(key=lambda p:p[1][0], reverse=True)
        
        nworld = self.world.status.clone()
        
        for condition in pending:
            if not condition[0].isVariable():
                nworld.add(condition[0])
            
        for condition in pending:
            condition = condition[0]
            if not condition.isVariable():
                
                nworld = self.satisfy(condition, nworld.clone(), negated)
                
                if nworld is False:
                    print "Cannot satisfy condition",condition
                    return False
            else:
                for value in self.expandVariable(condition):
                    r = self.satisfy(value, nworld.clone(), negated)
                
                    if r is not False:
                        print "Satisfied with value:",value
                        nworld = r
                        break
                else:
                    print "Cannot satisfy condition",condition
                    return False
        
        self.world.status = nworld
        
        #last check
        if not self.world.validate():
            print "The solver returned an invalid configuration!"
            return False
        
        if not self.world.compatible(conditions):
            print "The solver did not return a compatible configuration!"
            return False
            
        return True
        
    
    def satisfy(self, target, world, negated):
        print "Satisfying",target
        
        world.add(target)
        
        for condition in negated:
            if condition in world:
                print "World has a globally negated clause"
                return False
        
        for rule in self.world.representationRules:
            if isinstance(rule, basic.unique) and not rule.verify(world):
                print "Unique rule is violated for",target,"cannot continue"
                return False
        
            elif isinstance(rule, basic.depends) and not rule.verify(world):
                print "Rule failed",rule,"expanding dependencies"
                
                for condition in rule.body:
                    if condition.negated and condition in world:
                        print "Negative condition is already in the world"
                        return False
                    #if the condition is already met
                    if condition in world:
                        print "Condition met",condition
                        continue
                    if condition.negated:
                        print "Negative condition is not in world, continue",condition
                        continue
                        
                    if not condition.isVariable():
                        
                        world = self.satisfy(condition, world.clone(), negated)
                        
                        if world is False:
                            print "Cannot satisfy condition",condition
                            return False
                    else:
                        for value in self.expandVariable(condition):
                            r = self.satisfy(value, world.clone(), negated)
                        
                            if r is not False:
                                print "Satisfied with value:",value
                                world = r
                                break
                        else:
                            print "Cannot satisfy condition",condition
                            return False
        print "Satisfied",target
        return world
    
    def expandVariable(self, target):
        print "Expanding variable",target
        out = []
        for value in target.category.body:
            v = basic.status(target.category, value)
            out.append((v, self.expand(v)))
        
        out.sort(key = lambda t: t[1][0],reverse=True)
        
        return [v for v,_ in out]
    
    def expand(self, target):
        i = 0
        uniques = []
        depends = []
        for rule in self.world.representationRules:
            if rule.head == target:
                i += 1
                if isinstance(rule, basic.depends):
                    depends.append(rule)
                else:
                    uniques.append(rule)
        return (i, uniques, depends)
                