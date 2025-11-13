'''
Created on Aug 9, 2015

@author: karurosu
'''
from lang.domain import TestPlan
from lang.solver import WorldSolver
from lang.basic import status, variable, compositeSet, statusSet

from optimiser.clusters import Clusterizer

import sample3.world as world
import sample3.plan as plan

from optimiser.coverage import RuntimeOptimiser, weight

import sys

if __name__ == '__main__':
    print "Aemos v1 - AI Enhanced Multi Objective Scheduler"
    print "Sample 1"
   
    tp = TestPlan()
    
    print "Importing world"
    
    tp.world.addTokensFromModule(world)
    tp.world.addGenerationRulesFromModule(world)
    tp.world.addRepresentationRulesFromModule(world)
    
    print "Generating test cases"
    plan.expand()
    
    tp.loadTestCases(plan)
    
    solver = WorldSolver(tp.world)
    
    print "World status:"
    print tp.world
    
    
#     filtered = ['pci_configuration', 'full_boot', 'pci_failover', 'test_pci_linux', 'pci_alternate']
#     
#     if filtered:
#         for tcn in filtered:
#             print "Retesting",tcn
#             tp.world.status = statusSet()
#             tc = tp.testCases[tcn]
#             w = solver.add(tc.preconditions)
#             print w
#     
    
    failed = []
    tp.world.status = statusSet()
    ok = 0
    for name,tc in tp.testCases.items():
        print "Testing",name
        tp.world.status = statusSet()
        if not solver.add(tc.preconditions):
            print
            print "!!! Cannot resolve world !!!"
            print "Testcase:",name
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print
            failed.append(name)
            continue
        print
        print ">>> World resolved:"
        print ">>>",tp.world
        print
        print
        ok += 1
        
    
    if failed != []:
        print "There were some unsolved worlds",len(failed)
        print failed
        sys.exit(-2)
    
    print "Scan complete:", ok, "test cases verified out of",len(tp.testCases)
    cl = Clusterizer(tp.world)
    
    tc, filt =  cl.filter(tp.testCases)
    
    #print "Test Cases=>",", ".join([str(t) for t in tc])
    print "Filtered=>",", ".join([str(t) for t in filt])
    
    r = cl.clusterize(tp)
    
    print
    print ">>> Clusters:"
    print 
    
    failed = []
    
    for cluster in r:
        print "Validating cluster"
        print cluster
        tp.world.status = cluster.core
        if not tp.world.validate():
            print "!!!! Cluster is invalid!"
            failed.append(cluster)
            continue
        for tc in cluster.members:
            if not tp.world.compatible(tc.preconditions):
                print "!!!! Test case is incompatible with core:",tc
                failed.append(cluster)
                continue
        acc = 0
        for tc in cluster:
            acc += tc.attributes['runtime']
        cluster.attributes['runtime'] = acc
        print "Runtime",acc
        
        
        collection = []
        
        for tc in cluster:
            collection.append(tc.attributes['coverage'])
        cluster.attributes['coverage'] = weight(*collection)
        print "Coverage:", cluster.attributes['coverage']
        print
    
    print "Clustering done. Found",len(r),"clusters"
    
    if failed != []:
        print "There were failures in the clustering: ",len(failed)
        sys.exit(-3)
    
    print "Calculating larger selection"
    rt = 0
    
    for cluster in r:
        rt += cluster.attributes['runtime']
    
    col = []
    for tc in tp.testCases.values():
        col.append(tc.attributes['coverage'])
    
    cov = weight(*col)
    
    print "Runtime:",rt
    print "Coverage", float(cov)
    print
    
    print "Cluster verification (extra)"
    for cluster in r:
        for another in r:
            if another is cluster:
                continue
            
            for cond in cluster.core:
                if cond not in another.core:
                    break
            else:
                print "---------------------------"
                print "Found 2 identical or compatible clusters"
                print cluster
                print another
                print "---------------------------"
                print
                 
    print
    print ">>> Optimiser:"
    print 
    
    op = RuntimeOptimiser(r)
    results = op.optimise(3200, "test-auto-3200.csv")
    
    print "Selection:"
    print "Length",len(results)
    for cluster in results:
        print cluster
        print cluster.attributes