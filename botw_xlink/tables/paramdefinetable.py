from typing import List, Union

from ..binary import BinaryReader
from ..binary.types import UInt32, Float32


class ParamDef:
    nameOffset: UInt32
    type: UInt32
    defaultValue: Union[UInt32, Float32, bool]

    @classmethod
    def read(cls, br: BinaryReader):
        inst = cls()

        inst.nameOffset = br.read_uint32()
        inst.type = br.read_uint32()

        if inst.type == 0:  # Int
            inst.defaultValue = br.read_uint32()
        elif inst.type == 1:  # Float
            inst.defaultValue = br.read_float32()
        elif inst.type == 2:  # Bool
            inst.defaultValue = bool(br.read_uint32())
        elif inst.type == 3:  # Enum?
            inst.defaultValue = br.read_uint32()
        elif inst.type == 4:  # Offset into stringtable
            inst.defaultValue = br.read_uint32()
        elif inst.type == 5:  # ???
            inst.defaultValue = br.read_uint32()
        else:
            print("Something else")
            inst.defaultValue = br.read_uint32()

        return inst

    def __repr__(self):
        return f"{self.__class__.__name__}({self.nameOffset}, {self.type}, {self.defaultValue})"


class StringTableEntry:
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


class ParamDefineTable:
    size: UInt32
    numUserParams: UInt32
    numAssetParams: UInt32
    unknown: UInt32
    numTriggerParams: UInt32

    userParams: List[ParamDef]
    assetParams: List[ParamDef]
    triggerParams: List[ParamDef]

    stringTable: List[str]

    @classmethod
    def read(cls, br: BinaryReader):
        offset = br.tell()

        inst = cls()

        inst.size = br.read_uint32()
        inst.numUserParams = br.read_uint32()
        inst.numAssetParams = br.read_uint32()
        inst.unknown = br.read_uint32()
        inst.numTriggerParams = br.read_uint32()

        inst.userParams = [ParamDef.read(br) for _ in range(inst.numUserParams)]
        inst.assetParams = [ParamDef.read(br) for _ in range(inst.numAssetParams)]
        inst.triggerParams = [ParamDef.read(br) for _ in range(inst.numTriggerParams)]

        inst.stringTable = []

        string_table_beginning_offset = br.tell()

        while inst.size - (br.tell() - offset) > 3:
            inst.stringTable.append(
                StringTableEntry.read(br, string_table_beginning_offset)
            )

        br.align_to(4)

        return inst
