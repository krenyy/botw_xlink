from typing import List

from ..binary import BinaryReader, BinaryWriter
from ..binary.types import Float32


class CurvePointTableEntry:
    x: Float32
    y: Float32

    @classmethod
    def read(cls, br: BinaryReader):
        inst = cls()

        inst.x = br.read_float32()
        inst.y = br.read_float32()

        return inst

    def write(self, bw: BinaryWriter):
        bw.write_float32(self.x)
        bw.write_float32(self.y)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"


class CurvePointTable:
    entries: List[CurvePointTableEntry]

    @classmethod
    def read(cls, br: BinaryReader, numCurvePointTable: int):
        inst = cls()

        inst.entries = [CurvePointTableEntry.read(br) for _ in range(numCurvePointTable)]

        return inst

    def write(self, bw: BinaryWriter):
        [entry.write(bw) for entry in self.entries]
