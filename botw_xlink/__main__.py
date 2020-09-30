from pathlib import Path

from . import XLNK

testfiles_path = Path(__file__).parent / "testfiles"
elnk = testfiles_path / "ELink2DB.bin"
slnk = testfiles_path / "SLink2DB.bin"

xlnk = XLNK.fromfile(slnk)


# Dump all hash entries with their respective exRegion data chunks

out_path = testfiles_path / "out"
out_path.mkdir(exist_ok=True)

for i, entry in enumerate(xlnk.userDataTable.entries):
    with open(out_path / (str(entry.crc32) + ".bin"), "wb") as f:
        f.write(
            xlnk.exRegion.bytes[
                entry.exRegionOffset
                - xlnk.header.exRegionPos : xlnk.userDataTable.entries[
                    i + 1
                ].exRegionOffset
                - xlnk.header.exRegionPos
                if i + 1 < len(xlnk.userDataTable.entries)
                else len(xlnk.exRegion.bytes)
            ]
        )
