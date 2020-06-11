from typing import List

from ..binary import BinaryWriter, BinaryReader
from ..binary.types import UInt32


class DirectValueTable:
    entries: List[UInt32]

    @classmethod
    def read(cls, br: BinaryReader, numDirectValueTable: int):
        inst = cls()

        inst.entries = [br.read_uint32() for _ in range(numDirectValueTable)]

        return inst

    def write(self, bw: BinaryWriter):
        [bw.write(entry) for entry in self.entries]
