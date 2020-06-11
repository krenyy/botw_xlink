from . import XLNK

xlnk = XLNK.fromfile('/home/kreny/projects/python/botw_xlink/botw_xlink/testfiles/ELink2DB.bin')

xlnk.nameTable.entries = xlnk.nameTable.entries[-7:-1]

print()
