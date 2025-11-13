'''
Created on Aug 21, 2015

@author: karurosu
'''

from lang import basic

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
        variables = basic.statusSet()
        world = self.world.status.clone()
        negative = basic.statusSet()
        variables_n = basic.statusSet()
        
        for condition in conditions:
            if condition.negated:
                negative.add(condition)
            else:
                if condition.isVariable():
                    variables.add(condition)
                else:
                    world.add(condition)
        
        uniques = []
        depends = []
        
        for rule in self.world.representationRules:
            if isinstance(rule, basic.depends):
                depends.append(rule)
            else:
                uniques.append(rule)
        
        #quick check to make sure uniques are not violated
        for unique in uniques:
            if not unique.verify(world):
                print "Unique rules are broken from the beginning, cannot solve"
                return False
        
        #quick check for negative
        for negated in negative:
            if negated in world:
                print "Negated rules are broken from the beginning, cannot solve"
                return False
        
        #now process each rule and keep a list of activated rules
        activated = []
        
        pending = []
        
        while True:
            for rule in depends:
                if rule not in activated and rule.head in world:
                    activated.append(rule)
                    #now check each body clause, add it to the corresponding list
                    for clause in rule.body:
                        if clause.negated:
                            if clause.isVariable():
                                variables_n.add(clause)
                            else:
                                negative.add(clause)
                        else:
                            #these have to be checked again
                            pending.append(clause)
            if pending == []:
                break
            else:
                for c in pending:
                    if c.isVariable():
                        variables.add(c)
                    else:
                        world.add(c)
                pending = []
                continue
        
        #remove variables already satisfied
        variables = [var for var in variables if var not in world]
        
        #check that the negative constrains are taken into account
        for negated in negative:
            if negated in world:
                print "Negated rules are broken after analysis, cannot solve:",negated
                return False
        
        for negated in variables_n:
            if negated in world:
                print "Negated rules are broken after analysis, cannot solve:",negated
                return False
        
        #check again uniques
        for unique in uniques:
            if not unique.verify(world):
                print "Unique rules are broken after analysis, cannot solve",unique
                return False
        
        #now try to solve
        print "Starting search"
        