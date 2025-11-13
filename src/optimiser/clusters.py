'''
Created on Aug 23, 2015

@author: karurosu
'''
import lang.basic as basic
from lang.solver import WorldSolver
from lang.basic import statusSet


class Cluster(object):
    def __init__(self, members, core):
        self.members = members
        self.core = core
        self.attributes = {}
    
    def __str__(self):
        return "Core: {0}\n{1}".format(str(self.core), "\n".join([str(x) for x in self.members]))
    
    def __iter__(self):
        return iter(self.members)

class Clusterizer(object):
    def __init__(self, world):
        self.solver = WorldSolver(world)
    
    def filter(self, testCases):
        '''
        Check test cases and return those that have posconditions that touch the preconditions
        '''
        filtered = []
        processed = []
        
        for testCase in testCases.values():
            for condition in testCase.postconditions:
                for precondition in testCase.preconditions:
                    if condition == precondition:
                        filtered.append(testCase)
                        break
                else:
                    continue
                break
            else:
                processed.append(testCase)
                
        return processed, filtered
    
    def clusterize(self, testplan):
        testcases, filtered = self.filter(testplan.testCases)
        clusters = []
        
        testcases.sort(key=lambda x: len(x.preconditions), reverse=True)
        
        while len(testcases) != 0:
            core = basic.statusSet() 
            core_negative = basic.statusSet()
            
            n = testcases.pop(0)
            
            if n.name == 'pci_alternate':
                pass
            
            self.solver.world.status.clear()
            self._extend(n.preconditions, core, core_negative)
            
#            if not self.solver.add(core):
            if not self.solver.add(n.preconditions):
                print "test case cannot be resolved",n
                return None
            
            core = self.solver.world.status
            
            g = [n]
            
            while True:
                changed = False
                
                for t in testcases:
                    if t not in g:
                        add = self._isCompatible(t, core, core_negative)
                        
                        if add is False:
                            continue
                        
                        core2 = core.clone()
                        core2.extend(add)
                        
                        solution = self._resolve(core2)
                        
                        if solution is not None:
                            changed = True
                            g.append(t)
                            core = solution.clone()
                            self._extendSign(t.preconditions, core_negative, True)
                        
                if not changed:
                    nc = Cluster(g, core.clone())
                    clusters.append(nc)
                    break
            
            for t_g in g:
                if t_g in testcases:
                    testcases.remove(t_g)
        
        for tc in filtered:
            self.solver.world.status.clear()
            if not self.solver.add(tc.preconditions):
                print "Cannot resolve test case",tc
                return None
            nc = Cluster([tc], self.solver.world.status.clone())
            clusters.append(nc)
        
        return clusters
    
    def _extend(self, conditions, core, core_negative):
        for cond in conditions:
            if cond.negated:
                core_negative.add(cond)
            else:
                core.add(cond)
                
    def _extendSign(self, source, dest, sign = False):
        for cond in source:
            if cond.negated == sign:
                dest.add(cond)
        
    def _isCompatible(self, tc, core, core_negative):
        add = []
        for post in tc.preconditions:
            if post.negated:
                if post in core:
                    return False
            else:
                if post not in core:
                    if post in core_negative:
                        #attempt to add a "forbidden" clause
                        return False
                    add.append(post)
        
        return add
    
    def _resolve(self, world):
        self.solver.world.status = statusSet()
        
        if self.solver.add(world):
            return self.solver.world.status
        
        return None