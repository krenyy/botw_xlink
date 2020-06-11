from typing import List

from ..binary import BinaryWriter, BinaryReader
from ..binary.types import UInt32, Float32, UInt16, UInt8


class ConditionTableEntry:
    parentContainerType: UInt32

    weight: Float32

    propertyType: UInt32
    compareType: UInt32
    value: UInt32
    localPropertyEnumNameIdx: UInt16
    isSolved: UInt8
    isGlobal: UInt8

    @classmethod
    def read(cls, br: BinaryReader):
        inst = cls()

        inst.parentContainerType = br.read_uint32()

        if inst.parentContainerType in (1, 2):
            inst.weight = br.read_float32()
        else:
            inst.propertyType = br.read_uint32()
            inst.compareType = br.read_uint32()
            inst.value = br.read_uint32()
            inst.localPropertyEnumNameIdx = br.read_uint16()
            inst.isSolved = br.read_uint8()
            inst.isGlobal = br.read_uint8()

        return inst

    def write(self, bw: BinaryWriter):
        bw.write_uint32(self.parentContainerType)

        if self.parentContainerType in (1, 2):
            bw.write_float32(self.weight)
        else:
            bw.write_uint32(self.propertyType)
            bw.write_uint32(self.compareType)
            bw.write_uint32(self.value)
            bw.write_uint16(self.localPropertyEnumNameIdx)
            bw.write_uint8(self.isSolved)
            bw.write_uint8(self.isGlobal)


class ConditionTable:
    entries: List[ConditionTableEntry]

    @classmethod
    def read(cls, br: BinaryReader, size: int):
        inst = cls()

        inst.entries = []

        offset = br.tell()

        while size - (br.tell() - offset) != 0:
            inst.entries.append(ConditionTableEntry.read(br))

        return inst

    def write(self, bw: BinaryWriter):
        [entry.write(bw) for entry in self.entries]
