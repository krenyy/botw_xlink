from typing import List

from ..binary import BinaryReader
from ..binary.types import UInt32


class NameTableEntry:
    offset: UInt32
    value: str

    @classmethod
    def read(cls, br: BinaryReader, baseOffset: UInt32):
        inst = cls()

        inst.offset = br.tell() - baseOffset
        inst.value = br.read_string()

        return inst

    def __repr__(self):
        return f"{self.__class__.__name__}({self.offset}, {self.value})"


class NameTable:
    entries: List[NameTableEntry]

    @classmethod
    def read(cls, br: BinaryReader):
        inst = cls()

        inst.entries = []

        offset = br.tell()

        while br.tell() < len(br.getvalue()) - 4:
            inst.entries.append(NameTableEntry.read(br, offset))

        br.align_to(4)  # either 4 or 8, doesn't matter for reading

        return inst
