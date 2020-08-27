#OS version
import platform
import sys

info = 'Os info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture()
)
print(info)
