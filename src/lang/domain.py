'''
Created on Aug 9, 2015

Contains representations used by the domain, uses the basic tokens

@author: karurosu
'''

import basic

class TestCase(object):
    def __init__(self, preconditions, postconditions, attributes):
        self.name = None
        self.preconditions = preconditions
        self.postconditions = basic.statusSet(postconditions)
        self.attributes = attributes
    
    def __str__(self):
        return "Testcase: {0}".format(self.name)

class TestPlan(object):
    def __init__(self):
        self.world = basic.World()
        self.testCases = {}
        
    def loadTestCases(self, module):
        for name,obj in module.__dict__.items():
            if isinstance(obj, TestCase):
                obj.name = name
                self.testCases[name]=obj
