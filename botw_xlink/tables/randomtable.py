from typing import List

from ..binary import BinaryWriter, BinaryReader
from ..binary.types import Float32


class RandomTableEntry:
    min: Float32
    max: Float32

    @classmethod
    def read(cls, br: BinaryReader):
        inst = cls()

        inst.min = br.read_float32()
        inst.max = br.read_float32()

        return inst

    def write(self, bw: BinaryWriter):
        bw.write_float32(self.min)
        bw.write_float32(self.max)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.min}, {self.max})"


class RandomTable:
    entries: List[RandomTableEntry]

    @classmethod
    def read(cls, br: BinaryReader, numRandomTable: int):
        inst = cls()

        inst.entries = [RandomTableEntry.read(br) for _ in range(numRandomTable)]

        return inst

    def write(self, bw: BinaryWriter):
        [entry.write(bw) for entry in self.entries]
