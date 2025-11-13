'''
Created on Oct 13, 2015

@author: karurosu
'''
from lang.domain import TestCase
from lang.basic import status, variable
import world
import features

templates =  [
            TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.WINDOWS_VERSIONS, variable()),
                                         status(world.MEMORY_AMMOUNT, variable()),
                                         status(world.PROCESSOR, variable()),
                                         status(world.DISK_MODE, variable()),
                                         status(world.PCI_SLOT_1, variable())
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu"),
                                    'runtime': 20,
                                    'template': 'windows_boot_internal'
                                    }
                        ),

            TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.WINDOWS_VERSIONS, variable()),
                                         status(world.MEMORY_AMMOUNT, variable()),
                                         status(world.PROCESSOR, variable()),
                                         status(world.DISK_MODE, variable()),
                                         status(world.PCI_SLOT_1, variable())
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu"),
                                    'runtime': 20,
                                    'template': 'windows_boot_external'
                                    }
                        ),
            TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.LINUX_VERSIONS, variable()),
                                         status(world.MEMORY_AMMOUNT, variable()),
                                         status(world.PROCESSOR, variable()),
                                         status(world.DISK_MODE, variable()),
                                         status(world.PCI_SLOT_1, variable())
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu"),
                                    'runtime': 20,
                                    'template': 'linux_boot_internal'
                                    }
                        ),

            TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.LINUX_VERSIONS, variable()),
                                         status(world.MEMORY_AMMOUNT, variable()),
                                         status(world.PROCESSOR, variable()),
                                         status(world.DISK_MODE, variable()),
                                         status(world.PCI_SLOT_1, variable())
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu"),
                                    'runtime': 20,
                                    'template': 'linux_boot_external'
                                    }
                        ),

]

def genTestCase(template, vars, values):
    pre = []
    post = list(template.postconditions)
    attributes = {
                  'runtime': template.attributes['runtime'] 
                  }
    
    for cond in template.preconditions:
        if cond.isVariable():
            st = status(cond.category, values[vars.index(cond)])
            pre.append(st)
        else:
            pre.append(cond)
    
    name = "{0}_{1}".format(template.attributes['template'], "_".join([str(s) for s in values]))
    print "Creating test case",name
    
    if "windows_boot_internal" == template.attributes['template']:
        attributes['coverage'] = features.root.get('internal-windows')
        
    if "linux_boot_internal" == template.attributes['template']:
        attributes['coverage'] = features.root.get('internal-linux')
    
    if "windows_boot_external" == template.attributes['template']:
        attributes['coverage'] = features.root.get('external-windows')
        
    if "linux_boot_external" == template.attributes['template']:
        attributes['coverage'] = features.root.get('external-linux')
    
    if template.attributes['template'] in ["windows_boot_internal","linux_boot_internal"] and world.HIGH_MEM in values:
        print "Incompatible configuration"
        return None,None
    
    return name, TestCase(preconditions=pre, postconditions=post,attributes=attributes)

def expand():
    for template in templates:
        vars = []
        
        for p in template.preconditions:
            if p.isVariable():
                vars.append(p)
        
        values = []
        
        for var in vars:
            values.append(list(var.category.body))
        
        counters = [0]*len(values)
        stop = False
        while True:
            
            r = []
            for i,c in enumerate(counters):
                r.append(values[i][c])
            
            name, tc = genTestCase(template, vars, r)
            if name is not None:
                globals()[name] = tc
            
            for i in range(len(counters)):
                c = counters[i]
                c+=1
                
                if c == len(values[i]):
                    if i + 1 == len(counters):
                        print "Stop"
                        stop = True
                        break
                    counters[i] = 0
                    continue
                
                counters[i] = c
                break
            if stop:
                break
            
            
        
            
