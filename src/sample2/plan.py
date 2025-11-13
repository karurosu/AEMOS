'''
Created on Oct 13, 2015

@author: karurosu
'''
from lang.domain import TestCase
from lang.basic import status
import world
import features

boot_internal = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu"),
                                    'runtime': 20
                                    }
                        )

boot_external = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu"),
                                    'runtime': 20
                                    }
                        )

boot_mini = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_M),
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("minibios-menu"),
                                    'runtime': 20
                                    }
                        )

boot_internal_windows = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-windows"),
                                    'runtime': 30
                                    }
                        )

boot_external_windows = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", "external-windows"),
                                    'runtime': 30
                                    }
                        )

boot_internal_linux = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.LINUX)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-linux"),
                                    'runtime': 35
                                    }
                        )

boot_external_linux = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.LINUX)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", "external-linux"),
                                    'runtime': 25
                                    }
                        )

boot_internal_windows_max = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.WINDOWS),
                                         status(world.MEMORY_AMMOUNT, world.HIGH_MEM),
                                         status(world.PROCESSOR, world.DUAL_PROC)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-windows", 'memory-maximum', 'reliability-processor'),
                                    'runtime': 60
                                    }
                        )

boot_internal_linux_max = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.LINUX),
                                         status(world.MEMORY_AMMOUNT, world.HIGH_MEM),
                                         status(world.PROCESSOR, world.DUAL_PROC)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-linux", 'memory-maximum', 'reliability-processor'),
                                    'runtime': 10
                                    }
                        )

boot_internal_windows_min = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.WINDOWS),
                                         status(world.MEMORY_AMMOUNT, world.MINIMAL_MEM),
                                         status(world.PROCESSOR, world.SINGLE_PROC)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-windows", 'memory-reduced', 'reliability-processor'),
                                    'runtime': 10
                                    }
                        )

boot_internal_linux_min = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.LINUX),
                                         status(world.MEMORY_AMMOUNT, world.MINIMAL_MEM),
                                         status(world.PROCESSOR, world.SINGLE_PROC)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-linux", 'memory-reduced', 'reliability-processor'),
                                    'runtime': 60
                                    }
                        )

boot_external_windows_max = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.WINDOWS),
                                         status(world.MEMORY_AMMOUNT, world.HIGH_MEM),
                                         status(world.PROCESSOR, world.DUAL_PROC),
                                         status(world.MEMORY_MODE, world.NORMAL)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", "external-windows", 'memory-maximum', 'reliability-processor'),
                                    'runtime': 50
                                    }
                        )

boot_external_windows8 = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.WINDOWS_VERSIONS, world.WIN8),
                                         status(world.MEMORY_MODE, world.NORMAL)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", "external-windows", 'os-windows-current'),
                                    'runtime': 20
                                    }
                        )

boot_internal_windows8 = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.WINDOWS_VERSIONS, world.WIN8),
                                         status(world.MEMORY_MODE, world.NORMAL)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-windows", 'os-windows-current'),
                                    'runtime': 34
                                    }
                        )

boot_internal_windows7 = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.WINDOWS_VERSIONS, world.WIN7),
                                         status(world.MEMORY_MODE, world.NORMAL)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-windows", 'os-windows-current'),
                                    'runtime': 32
                                    }
                        )

boot_external_windows7 = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.WINDOWS_VERSIONS, world.WIN7),
                                         status(world.MEMORY_MODE, world.NORMAL)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", "external-windows", 'os-windows-current'),
                                    'runtime': 22
                                    }
                        )

boot_internal_ubuntu = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.LINUX_VERSIONS, world.LINUXUBUNTU),
                                         status(world.MEMORY_MODE, world.NORMAL)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-linux", 'os-linux-desktop'),
                                    'runtime': 32
                                    }
                        )

boot_internal_sles = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.LINUX_VERSIONS, world.LINUXSLES),
                                         status(world.MEMORY_MODE, world.NORMAL)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-linux", 'os-linux-server'),
                                    'runtime': 19
                                    }
                        )

boot_internal_winxp = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.WINDOWS_VERSIONS, world.WINXP),
                                         status(world.MEMORY_MODE, world.NORMAL)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-windows", 'os-windows-legacy'),
                                    'runtime': 32
                                    }
                        )

windows_mirroring = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.WINDOWS),
                                         status(world.MEMORY_MODE, world.MIRROR)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-windows", 'memory-mirroring'),
                                    'runtime': 70
                                    }
                        )

linux_mirroring = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.LINUX_VERSIONS, world.LINUXRH9),
                                         status(world.MEMORY_MODE, world.MIRROR)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-linux", 'memory-mirroring', 'os-linux-server'),
                                    'runtime': 75
                                    }
                        )

windows_sparing = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.WINDOWS),
                                         status(world.MEMORY_MODE, world.SPARE)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-windows", 'memory-sparing'),
                                    'runtime': 55
                                    }
                        )

linux_sparing = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.LINUX_VERSIONS, world.LINUXRH9),
                                         status(world.MEMORY_MODE, world.SPARE)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", "internal-linux", 'memory-sparing', 'os-linux-server'),
                                    'runtime': 57
                                    }
                        )

minimal_boot = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_M),
                                         status(world.PROCESSOR, world.SINGLE_PROC),
                                         status(world.MEMORY_AMMOUNT, world.MINIMAL_MEM)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("minibios-menu", 'memory-reduced', 'reliability-processor'),
                                    'runtime': 5
                                    }
                        )

full_boot = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.PROCESSOR, world.DUAL_PROC),
                                         status(world.MEMORY_AMMOUNT, world.HIGH_MEM),
                                         -status(world.PCI_SLOT_1, world.PCI_NONE),
                                         -status(world.PCI_SLOT_2, world.PCI_NONE),
                                         -status(world.PCI_SLOT_3, world.PCI_NONE),
                                         -status(world.PCI_SLOT_4, world.PCI_NONE)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", 'reliability-processor', 'memory-maximum'),
                                    'runtime': 120
                                    }
                        )

pci_configuration = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.WINDOWS),
                                         -status(world.PCI_SLOT_1, world.PCI_NONE)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", 'internal-windows', 'pci-detection', 'pci-features'),
                                    'runtime': 37
                                    }
                        )

pci_failover = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.WINDOWS),
                                         -status(world.PCI_SLOT_1, world.PCI_NONE),
                                         -status(world.PCI_SLOT_2, world.PCI_NONE)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", 'internal-windows', 'pci-failures'),
                                    'runtime': 53
                                    }
                        )

usb3_test_windows = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", 'internal-windows', 'devices'),
                                    'runtime': 40
                                    }
                        )

usb3_test_linux = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.LINUX)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu", 'internal-linux', 'devices'),
                                    'runtime': 38
                                    }
                        )

locks_test = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_M),
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("minibios-menu", 'security-cpu', 'security-pci'),
                                    'runtime': 15
                                    }
                        )

memory_locks = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", 'external-windows', 'security-memory'),
                                    'runtime': 25
                                    }
                        )

device_locks = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.LINUX)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", 'external-linux', 'security-devices'),
                                    'runtime': 20
                                    }
                        )

upgrade_bios = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E)
                                         ],
                        postconditions= [
                                         -status(world.BIOS, world.BIOS_E),
                                         status(world.BIOS, world.BIOS_I),
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", 'internal-menu', 'bios-upgrade'),
                                    'runtime': 10
                                    }
                        )

downgrade_bios = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I)
                                         ],
                        postconditions= [
                                         -status(world.BIOS, world.BIOS_I),
                                         status(world.BIOS, world.BIOS_E),
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", 'internal-menu', 'bios-downgrade'),
                                    'runtime': 10
                                    }
                        )

recovery = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get('internal-menu', 'bios-recovery'),
                                    'runtime': 10
                                    }
                        )

safe_boot = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get('external-menu', 'external-windows', 'safe-boot'),
                                    'runtime': 31
                                    }
                        )

external_stress_windows = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get('external-menu', 'external-windows', 'reliability-processor', 'memory-stress'),
                                    'runtime': 200
                                    }
                        )

external_stress_linux = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.LINUX)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get('external-menu', 'external-linux', 'reliability-processor', 'memory-stress'),
                                    'runtime': 200
                                    }
                        )

external_windows7_graphics = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.WINDOWS),
                                         status(world.WINDOWS_VERSIONS, world.WIN7),
                                         status(world.PCI_SLOT_1, world.PCI_NVGFX)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get('external-menu', 'external-windows', 'os-windows-current'),
                                    'runtime': 60
                                    }
                        )

internal_sas = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         -status(world.OS, world.NONE),
                                         status(world.DISK_MODE, world.SAS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get('internal-menu', 'devices-detection'),
                                    'runtime': 20
                                    }
                        )

internal_sata = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         -status(world.OS, world.NONE),
                                         status(world.DISK_MODE, world.SATA)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get('internal-menu', 'devices-detection'),
                                    'runtime': 20
                                    }
                        )

external_sas = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         -status(world.OS, world.NONE),
                                         status(world.DISK_MODE, world.SAS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get('external-menu', 'devices-detection'),
                                    'runtime': 20
                                    }
                        )

external_sata = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         -status(world.OS, world.NONE),
                                         status(world.DISK_MODE, world.SATA)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get('external-menu', 'devices-detection'),
                                    'runtime': 20
                                    }
                        )


pci_alternate = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         -status(world.OS, world.NONE),
                                         -status(world.PCI_SLOT_1, world.PCI_NONE),
                                         status(world.PCI_SLOT_2, world.PCI_NONE),
                                         -status(world.PCI_SLOT_3, world.PCI_NONE),
                                         status(world.PCI_SLOT_4, world.PCI_NONE)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get('internal-menu', 'pci-detection','pci-features','pci-configuration'),
                                    'runtime': 20
                                    }
                        )

test_pci_linux = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.LINUX),
                                         -status(world.PCI_SLOT_1, world.PCI_NONE),
                                         -status(world.PCI_SLOT_2, world.PCI_NONE),
                                         status(world.PCI_SLOT_3, world.PCI_NONE),
                                         status(world.PCI_SLOT_4, world.PCI_NONE)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", 'external-linux', 'pci-detection'),
                                    'runtime': 24
                                    }
                        )

test_pci_network = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.LINUX),
                                         status(world.PCI_SLOT_1, world.PCI_IGE)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", 'external-linux', 'pci-features'),
                                    'runtime': 12
                                    }
                        )

test_pci_performance = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.WINDOWS),
                                         status(world.PCI_SLOT_1, world.PCI_LSI)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", 'external-windows', 'pci-features', 'pci-performance'),
                                    'runtime': 33
                                    }
                        )

boot_windows_ssd = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.WINDOWS),
                                         status(world.PCI_SLOT_1, world.PCI_SSD)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", 'external-windows', 'pci-features'),
                                    'runtime': 20
                                    }
                        )

boot_linux_ssd = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_E),
                                         status(world.OS, world.LINUX),
                                         status(world.PCI_SLOT_1, world.PCI_SSD)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("external-menu", 'external-linux', 'pci-features'),
                                    'runtime': 20
                                    }
                        )

test_setup_menu = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu"),
                                    'runtime': 400
                                    }
                        )

test_recoverable_error = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu","internal-windows",'recoverable-error'),
                                    'runtime': 26
                                    }
                        )

test_fatal_error = TestCase(
                        preconditions = [
                                         status(world.BIOS, world.BIOS_I),
                                         status(world.OS, world.WINDOWS)
                                         ],
                        postconditions= [
                                         ],
                        attributes={
                                    'coverage': features.root.get("internal-menu","internal-windows",'fatal-error'),
                                    'runtime': 30
                                    }
                        )