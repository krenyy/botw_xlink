from ..binary import BinaryReader, BinaryWriter


class ParamTable:
    """
    No idea what to do with this yet
    """

    bytes: bytes

    @classmethod
    def read(cls, br: BinaryReader, size: int):
        inst = cls()

        inst.bytes = br.read(size)

        return inst

    def write(self, bw: BinaryWriter):
        bw.write(self.bytes)
