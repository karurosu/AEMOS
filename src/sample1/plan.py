'''
Created on Aug 19, 2015

@author: karurosu
'''
from lang.domain import TestCase
from lang.basic import status, variable
import world
import features

boot_windows = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOSN),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("f1"),
                                    'runtime': 20
                                    }
                        )

boot_windows_n1 = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOSN_1),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("f1aa", "f2"),
                                    'runtime': 30
                                    }
                        )

boot_windows_n2 = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOSN_2),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("f2a", "f3"),
                                    'runtime': 20
                                    }
                        )

test_driver_12 = TestCase(
                        preconditions = [
                                         status(world.DRIVER, world.DRIVER_V12),
                                         status(world.BIOS, world.BIOSN_2),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("f2"),
                                    'runtime': 5
                                    }
                        )

test_downgrade_bios = TestCase(
                        preconditions = [
                                         status(world.DRIVER, world.DRIVER_V12),
                                         status(world.BIOS, world.BIOSN_2),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         -status(world.BIOS, world.BIOSN_2),
                                         status(world.BIOS, world.BIOSN_1)
                                         ],
                        attributes={
                                    'coverage': features.root.get("f2b", "f2c"),
                                    'runtime': 40
                                    }
                        )

test_windows_clean = TestCase(
                        preconditions = [
                                         -status(world.DRIVER, variable()),
                                         status(world.BIOS, variable()),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("f1", "f2"),
                                    'runtime': 67
                                    }
                        )

test_complete_cleanup = TestCase(
                        preconditions = [
                                         status(world.BIOS, variable()),
                                         status(world.OS, variable())
                                         ],
                        postconditions= [
                                         -status(world.BIOS, variable()),
                                         -status(world.OS, variable()),
                                         ],
                        attributes={
                                    'coverage': features.root.get("f3"),
                                    'runtime': 90
                                    }
                        )