'''
Created on Aug 9, 2015

@author: karurosu
'''

from lang.basic import token,category,status,variable,rules

#tokens
WIN2000 = token()
WINXP = token()
WIN7 = token()
WIN8 = token()

LINUXRH9 = token()
LINUXSLES = token()
LINUXUBUNTU = token()

BIOSN = token()
BIOSN_1 = token()
BIOSN_2 = token()

DRIVER_V12 = token()
DRIVER_V13 = token()
DRIVER_V14 = token()

WINDOWS = token()
LINUX = token()

#generation rules
OS = category(WINDOWS, LINUX)
LINUX_VERSIONS = category(LINUXRH9, LINUXSLES, LINUXUBUNTU)
WINDOWS_VERSIONS = category(WIN2000, WINXP, WIN7, WIN8)
BIOS = category(BIOSN, BIOSN_1, BIOSN_2)
DRIVER = category(DRIVER_V12, DRIVER_V13, DRIVER_V14)

#import the rules manager
rules = rules()
unique = rules.unique
depends = rules.depends

#representation rules
unique(OS)
unique(DRIVER)
unique(WINDOWS_VERSIONS)
unique(LINUX_VERSIONS)
unique(BIOS)

#for windows/linux to be defined, there must be at least one OS
depends(status(OS,WINDOWS)).And(status(WINDOWS_VERSIONS,variable()))
depends(status(OS,LINUX)).And(status(LINUX_VERSIONS,variable()))

#if Win/Lin was loaded, cannot load another
depends(status(WINDOWS_VERSIONS, variable())).And(-status(LINUX_VERSIONS, variable()))
depends(status(LINUX_VERSIONS, variable())).And(-status(WINDOWS_VERSIONS, variable()))

#for OS to be loaded, there must be at least one BIOS
depends(status(OS,variable())).And(status(BIOS,variable()))

#a driver requires an OS
depends(status(DRIVER,variable())).And(status(OS,variable()))

#driver 12 only works on windows and bios n-2
depends(status(DRIVER,DRIVER_V12)).And(status(OS,WINDOWS)).And(status(BIOS,BIOSN_2))

#driver 14 is windows only
depends(status(DRIVER,DRIVER_V14)).And(status(OS,WINDOWS))

#driver 14 does not work on winxp
depends(status(DRIVER,DRIVER_V14)).And(-status(WINDOWS_VERSIONS,WINXP))

#win8 will only boot on the latest BIOS
depends(status(WINDOWS_VERSIONS,WIN8)).And(status(BIOS,BIOSN))
