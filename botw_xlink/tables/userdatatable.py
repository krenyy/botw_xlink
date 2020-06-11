from typing import List

from ..binary import BinaryReader
from ..binary.types import UInt32


class UserDataTableEntry:
    crc32: UInt32
    exRegionOffset: UInt32

    def __init__(self, crc32: UInt32, exRegionOffset: UInt32):
        self.crc32 = crc32
        self.exRegionOffset = exRegionOffset

    def __repr__(self):
        return f"{self.__class__.__name__}({self.crc32}, {self.exRegionOffset})"


class UserDataTable:
    entries: List[UserDataTableEntry]

    @classmethod
    def read(cls, br: BinaryReader, numUser: UInt32):
        inst = cls()
        inst.entries = []

        crc32list = [br.read_uint32() for _ in range(numUser)]
        offsetlist = [br.read_uint32() for _ in range(numUser)]

        for h, o in zip(crc32list, offsetlist):
            inst.entries.append(UserDataTableEntry(h, o))

        return inst
