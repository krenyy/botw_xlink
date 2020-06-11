from typing import List

from ..binary import BinaryReader, BinaryWriter
from ..binary.types import UInt32


class RefTable:
    entries: List[UInt32]

    @classmethod
    def read(cls, br: BinaryReader, numEntries: int):
        inst = cls()

        inst.entries = [br.read_uint32() for _ in range(numEntries)]

        return inst

    def write(self, bw: BinaryWriter):
        [bw.write_uint32(entry) for entry in self.entries]
