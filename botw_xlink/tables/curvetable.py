from typing import List

from ..binary import BinaryReader, BinaryWriter
from ..binary.types import UInt16, UInt32


class CurveTableEntry:
    curvePointStartPos: UInt16
    numPoint: UInt16
    curveType: UInt16
    isPropGlobal: UInt16
    propName: UInt32
    propIdx: UInt32
    localPropertyNameIdx: UInt16
    Padding: UInt16

    @classmethod
    def read(cls, br: BinaryReader):
        inst = cls()

        inst.curvePointStartPos = br.read_uint16()
        inst.numPoint = br.read_uint16()
        inst.curveType = br.read_uint16()
        inst.isPropGlobal = br.read_uint16()
        inst.propName = br.read_uint32()
        inst.propIdx = br.read_uint32()
        inst.localPropertyNameIdx = br.read_uint16()
        inst.Padding = br.read_uint16()

        return inst

    def write(self, bw: BinaryWriter):
        bw.write_uint16(self.curvePointStartPos)
        bw.write_uint16(self.numPoint)
        bw.write_uint16(self.curveType)
        bw.write_uint16(self.isPropGlobal)
        bw.write_uint32(self.propName)
        bw.write_uint32(self.propIdx)
        bw.write_uint16(self.localPropertyNameIdx)
        bw.write_uint16(self.Padding)


class CurveTable:
    entries: List[CurveTableEntry]

    @classmethod
    def read(cls, br: BinaryReader, numCurveTable: int):
        inst = cls()

        inst.entries = [CurveTableEntry.read(br) for _ in range(numCurveTable)]

        return inst

    def write(self, bw: BinaryWriter):
        [entry.write(bw) for entry in self.entries]
