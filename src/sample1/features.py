'''
Created on Aug 25, 2015

@author: karurosu
'''

from optimiser.coverage import Feature


root = Feature('root', None, [
                              Feature('f1', None,[
                                                  Feature('f1a', None),
                                                  Feature('f1b', None, [
                                                                        Feature('f1aa', None),
                                                                        Feature('f1ab', None),
                                                                        Feature('f1ac', None)
                                                                        ])
                                                  ]),
                              Feature('f2', None,[
                                                  Feature('f2a', None),
                                                  Feature('f2b', None),
                                                  Feature('f2c', None),
                                                  Feature('f2d', None)
                                                  ]),
                              Feature('f3', None)
                              ])


root.distributeWeight()
root.index()