'''
Created on Oct 13, 2015

@author: karurosu
'''
from lang.basic import token,category,status,variable,rules
#import the rules manager
rules = rules()
unique = rules.unique
depends = rules.depends

SKU_1 = token()
SKU_2 = token()
SKU_3 = token()
SKU_4 = token()

WIN2000 = token()
WINXP = token()
WIN7 = token()
WIN8 = token()

LINUXRH9 = token()
LINUXSLES = token()
LINUXUBUNTU = token()

BIOS_I = token()
BIOS_E = token()
BIOS_M = token()

NONE = token()
WINDOWS = token()
LINUX = token()

PCI_NONE = token()
PCI_LSI = token()
PCI_IGE = token()
PCI_NVGFX = token()
PCI_SSD = token()

SAS = token()
SATA = token()

SINGLE_PROC = token()
DUAL_PROC = token()

HIGH_MEM = token()
MINIMAL_MEM = token()
MID_MEM = token()

NORMAL = token()
MIRROR = token()
SPARE = token()

#generation rules
SKU = category(SKU_1,SKU_2,SKU_3,SKU_4)
OS = category(NONE, WINDOWS, LINUX)
LINUX_VERSIONS = category(LINUXRH9, LINUXSLES, LINUXUBUNTU)
WINDOWS_VERSIONS = category(WIN2000, WINXP, WIN7, WIN8)
BIOS = category(BIOS_I, BIOS_E, BIOS_M)

PCI_SLOT_1 = category(PCI_NONE, PCI_IGE, PCI_LSI, PCI_NVGFX, PCI_SSD)
PCI_SLOT_2 = category(PCI_NONE, PCI_IGE, PCI_LSI, PCI_NVGFX, PCI_SSD)
PCI_SLOT_3 = category(PCI_NONE, PCI_IGE, PCI_LSI, PCI_NVGFX, PCI_SSD)
PCI_SLOT_4 = category(PCI_NONE, PCI_IGE, PCI_LSI, PCI_NVGFX, PCI_SSD)

DISK_MODE = category(SAS, SATA)
PROCESSOR = category(SINGLE_PROC,DUAL_PROC)
MEMORY_AMMOUNT = category(HIGH_MEM,MID_MEM,MINIMAL_MEM)
MEMORY_MODE = category(NORMAL, MIRROR, SPARE)

#representation rules
unique(OS)
unique(SKU)
unique(WINDOWS_VERSIONS)
unique(LINUX_VERSIONS)
unique(BIOS)
unique(PCI_SLOT_1)
unique(PCI_SLOT_2)
unique(PCI_SLOT_3)
unique(PCI_SLOT_4)
unique(DISK_MODE)
unique(PROCESSOR)
unique(MEMORY_AMMOUNT)
unique(MEMORY_MODE)

#Windows linux
depends(status(OS,WINDOWS)).And(status(WINDOWS_VERSIONS,variable()))
depends(status(OS,LINUX)).And(status(LINUX_VERSIONS,variable()))
depends(status(WINDOWS_VERSIONS,variable())).And(status(OS, WINDOWS))
depends(status(LINUX_VERSIONS,variable())).And(status(OS, LINUX))

#Windows/linux cannot run on miniBIOS
depends(status(OS,WINDOWS)).And(-status(BIOS,BIOS_M))
depends(status(OS,LINUX)).And(-status(BIOS,BIOS_M))

#A bios needs an sku to run
depends(status(BIOS,variable())).And(status(SKU,variable()))

#SKU specific
#SKU 1:
# single processor
# only mid level memory
# 2 PCI slots
# All BIOS
depends(status(SKU,SKU_1)).And(status(PROCESSOR,SINGLE_PROC))\
.And(-status(MEMORY_AMMOUNT,HIGH_MEM))\
.And(status(PCI_SLOT_3,PCI_NONE)).And(status(PCI_SLOT_4,PCI_NONE))

#SKU 2:
# single or dual processor
# only mid level memory
# 3 PCI slots
# All BIOS
depends(status(SKU,SKU_2))\
.And(-status(MEMORY_AMMOUNT,HIGH_MEM))\
.And(status(PCI_SLOT_4,PCI_NONE))

#SKU 3:
# dual processor only
# all memory
# 4 PCI slots
# Only I and M BIOS
depends(status(SKU,SKU_3)).And(status(PROCESSOR,DUAL_PROC))\
.And(-status(BIOS,BIOS_E))

#SKU 4:
# all processors
# all memory
# 4 PCI slots
# Only E BIOS
depends(status(SKU,SKU_4)).And(status(BIOS,BIOS_E))

#memory rules
#spare only works on mid memory
depends(status(MEMORY_MODE, SPARE)).And(status(MEMORY_AMMOUNT,MID_MEM))

#mirroring only works on full memory
depends(status(MEMORY_MODE, MIRROR)).And(status(MEMORY_AMMOUNT,HIGH_MEM))

#sparing/mirroring only works on Windows (except xp) and redhat
depends(status(WINDOWS_VERSIONS, WINXP)).And(-status(MEMORY_MODE, MIRROR))
depends(status(WINDOWS_VERSIONS, WINXP)).And(-status(MEMORY_MODE, SPARE))
depends(status(LINUX_VERSIONS, LINUXSLES)).And(-status(MEMORY_MODE, SPARE)).And(-status(MEMORY_MODE, MIRROR))
depends(status(LINUX_VERSIONS, LINUXUBUNTU)).And(-status(MEMORY_MODE, SPARE)).And(-status(MEMORY_MODE, MIRROR))

#all skus must have all variables defined
depends(status(SKU,variable())).And(status(PROCESSOR,variable())).And(status(DISK_MODE,variable()))\
.And(status(MEMORY_AMMOUNT,variable())).And(status(MEMORY_MODE,variable()))\
.And(status(PCI_SLOT_1,variable())).And(status(PCI_SLOT_2,variable()))\
.And(status(PCI_SLOT_3,variable())).And(status(PCI_SLOT_4,variable()))

#OS depends on a BIOS
depends(status(OS,variable())).And(status(BIOS,variable()))