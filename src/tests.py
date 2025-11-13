'''
Created on Aug 19, 2015

@author: karurosu
'''
import unittest
from lang.domain import TestPlan
from lang.basic import status, variable, compositeSet

import sample1.world
import sample1.plan

from fractions import Fraction

import optimiser.coverage

class Test(unittest.TestCase):
    def setUp(self):
        tp = TestPlan()
    
        print "Importing world"
        
        tp.world.addTokensFromModule(sample1.world)
        tp.world.addGenerationRulesFromModule(sample1.world)
        tp.world.addRepresentationRulesFromModule(sample1.world)
        tp.loadTestCases(sample1.plan)
        
        self.tp = tp
        
    def testStatusEquality(self):
        s1 = status(sample1.world.BIOS, sample1.world.BIOSN)
        s2 = status(sample1.world.BIOS, sample1.world.BIOSN)
        s3 = status(sample1.world.BIOS, variable("X"))
        s4 = status(sample1.world.BIOS, variable("Y"))
        s5 = status(sample1.world.DRIVER, variable("Y"))
        s6 = status(sample1.world.BIOS, sample1.world.BIOSN_1)
        
        self.assertEqual(s1,s2)
        self.assertEqual(s1,s3)
        self.assertEqual(s4,s3)
        self.assertNotEqual(s4,s5)
        self.assertNotEqual(s1,s6)
    
    def testWorldManipulation(self):
        tp = self.tp
        
        s1 = status(sample1.world.BIOS, sample1.world.BIOSN)
        s2 = status(sample1.world.BIOS, sample1.world.BIOSN)
        s3 = status(sample1.world.BIOS, variable("X"))
        s4 = status(sample1.world.BIOS, variable("Y"))
        s5 = status(sample1.world.DRIVER, variable("Y"))
        s6 = status(sample1.world.BIOS, sample1.world.BIOSN_1)
        s7 = status(sample1.world.BIOS, sample1.world.BIOSN_2)
        
        tp.world.status.add(s1)
        tp.world.status.add(s2)
        tp.world.status.add(s6)
        
        self.assertEqual(len(tp.world.status),2)
        
        self.assertTrue(s1 in tp.world.status)
        self.assertTrue(s2 in tp.world.status)
        self.assertTrue(s3 in tp.world.status)
        self.assertTrue(s4 in tp.world.status)
        self.assertTrue(s5 not in tp.world.status)
        self.assertTrue(s7 not in tp.world.status)
        
        tp.world.status.remove(s3)
        self.assertEqual(0, len(tp.world.status))
        
        tp.world.status.add(s1)
        tp.world.status.add(s2)
        tp.world.status.add(s6)
        
        tp.world.status.remove(s2)
        self.assertEqual(1, len(tp.world.status))
        
        tp.world.status.clear()
        self.assertEqual(0, len(tp.world.status))
    
        w2 = tp.world.status.clone()
        self.assertEqual(0, len(w2))
    
    def testRules(self):
        tp = self.tp
        
        self.assertFalse(tp.world.modify(compositeSet(status(sample1.world.DRIVER,sample1.world.DRIVER_V12))))
        self.assertEqual(0, len(tp.world.status))
        
        self.assertTrue(tp.world.modify(compositeSet(status(sample1.world.BIOS,sample1.world.BIOSN))))
        self.assertEqual(1, len(tp.world.status))
        
        self.assertTrue(tp.world.modify(compositeSet(-status(sample1.world.BIOS,sample1.world.BIOSN))))
        self.assertEqual(0, len(tp.world.status))
        
        self.assertTrue(tp.world.modify(compositeSet(status(sample1.world.BIOS,sample1.world.BIOSN))))
        self.assertEqual(1, len(tp.world.status))
        
        self.assertFalse(tp.world.modify(compositeSet(status(sample1.world.BIOS,sample1.world.BIOSN_1))))
        self.assertEqual(1, len(tp.world.status))
        
        self.assertTrue(tp.world.modify(compositeSet(
                                     status(sample1.world.BIOS,sample1.world.BIOSN),
                                     status(sample1.world.OS,sample1.world.WINDOWS),
                                     status(sample1.world.WINDOWS_VERSIONS,sample1.world.WINXP),
                                     status(sample1.world.DRIVER,sample1.world.DRIVER_V13)
                                     )))
        
        self.assertEqual(4, len(tp.world.status))
        
        self.assertFalse(tp.world.modify(compositeSet(-status(sample1.world.BIOS,sample1.world.BIOSN))))
        
        self.assertEqual(4, len(tp.world.status))
    
    def testPlan(self):
        self.assertEqual(len(self.tp.testCases), 7)
        
        self.tp.world.modify(compositeSet(
                                     status(sample1.world.BIOS,sample1.world.BIOSN),
                                     status(sample1.world.OS,sample1.world.WINDOWS),
                                     status(sample1.world.WINDOWS_VERSIONS,sample1.world.WINXP),
                                     status(sample1.world.DRIVER,sample1.world.DRIVER_V13)
                                     )
                        )
        
        self.assertEqual(self.tp.testCases['boot_windows'].name, 'boot_windows')
        self.assertEqual(len(self.tp.testCases['boot_windows'].preconditions), 2)
        
        self.assertTrue(self.tp.world.compatible(self.tp.testCases['boot_windows'].preconditions))
        self.assertFalse(self.tp.world.compatible(self.tp.testCases['test_windows_clean'].preconditions))
        
        self.assertTrue(self.tp.world.modify(compositeSet(-status(sample1.world.DRIVER,sample1.world.DRIVER_V13))))
        self.assertTrue(self.tp.world.compatible(self.tp.testCases['test_windows_clean'].preconditions))
    
    def testFeatures(self):
        import sample1.features
        sample1.features.root.distributeWeight()
        
        self.assertEquals(1, sample1.features.root.calculateWeight())
        self.assertEquals(Fraction(1,3), sample1.features.root.children[0].weight)
        self.assertEquals(Fraction(1,18), sample1.features.root.children[0].children[1].children[0].weight)
        
        l = sample1.features.root.flatten()
        self.assertEquals(9, len(l))
        
        self.assertTrue(sample1.features.root.children[2] in l)
        
        self.assertEqual(sample1.features.root.get("f1"), set([
                                                               sample1.features.root.index["f1a"],
                                                               sample1.features.root.index["f1aa"],
                                                               sample1.features.root.index["f1ab"],
                                                               sample1.features.root.index["f1ac"]
                                                               ]))
        
        self.assertEquals(optimiser.coverage.weight([
                                                   sample1.features.root.index["f1a"],
                                                   sample1.features.root.index["f1aa"],
                                                   sample1.features.root.index["f1ab"],
                                                   sample1.features.root.index["f1ac"]
                                                   ],
                                                    [
                                                   sample1.features.root.index["f1a"],
                                                   sample1.features.root.index["f1aa"],
                                                   sample1.features.root.index["f1ab"],
                                                   sample1.features.root.index["f1ac"]
                                                   ])
                                                   , Fraction(1,3)
                          )
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()