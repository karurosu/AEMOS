'''
Created on Oct 13, 2015

@author: karurosu
'''
from optimiser.coverage import Feature


root = Feature('root', None, [
                              Feature('booting', None,[
                                                  Feature('internal', None, [
                                                                            Feature('internal-windows', None),
                                                                            Feature('internal-linux', None),
                                                                            Feature('internal-menu', None)
                                                                            ]),
                                                  Feature('minibios', None, [
                                                                            Feature('minibios-menu', None)
                                                                            ]),
                                                  Feature('external', None, [
                                                                            Feature('external-windows', None),
                                                                            Feature('external-linux', None),
                                                                            Feature('external-menu', None)
                                                                            ])
                                                  ]),
                              Feature('reliability', None,[
                                                           Feature('reliability-memory', None,[
                                                                                  Feature('memory-mirroring', None),
                                                                                  Feature('memory-sparing', None),
                                                                                  Feature('memory-reduced', None),
                                                                                  Feature('memory-maximum', None),
                                                                                  Feature('memory-stress', None)
                                                                                  ]),
                                                           Feature('reliability-processor', None),
                                                           Feature('safe-boot', None),
                                                           Feature('error-handling', None, [
                                                                                            Feature('recoverable-error', None),
                                                                                            Feature('fatal-error', None),
                                                                                            ])
                                                  ]),
                              Feature('upgrade', None, [
                                                        Feature('bios-upgrade', None),
                                                        Feature('bios-downgrade', None),
                                                        Feature('bios-recovery', None)
                                                        ]),
                              Feature('pci', None, [
                                                    Feature('pci-detection', None),
                                                    Feature('pci-features', None),
                                                    Feature('pci-configuration', None),
                                                    Feature('pci-failures', None),
                                                    Feature('pci-performance', None),
                                                    ]),
                              Feature('devices', None,[
                                                       Feature('devices-detection', None),
                                                       Feature('devices-configuration', None),
                                                       Feature('devices-failures', None)
                                                       ]),
                              Feature('security', None,[
                                                        Feature('security-cpu', None),
                                                        Feature('security-pci', None),
                                                        Feature('security-devices', None),
                                                        Feature('security-memory', None),
                                                        ]),
                              Feature('os', None, [
                                                   Feature('os-windows', None, [
                                                                                Feature('os-windows-current', None),
                                                                                Feature('os-windows-legacy', None),
                                                                                ]),
                                                   Feature('os-linux', None, [
                                                                              Feature('os-linux-server', None),
                                                                              Feature('os-linux-desktop', None),
                                                                              ]),
                                                   Feature('os-other', None),
                                                   ])
                              ])


root.distributeWeight()
root.index()