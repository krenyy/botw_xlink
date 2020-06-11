from .binary import BinaryReader
from .binary.types import UInt32


class Header:
    magic: UInt32
    dataSize: UInt32
    version: UInt32
    numResParam: UInt32
    numResAssetParam: UInt32
    numResTriggerOverwriteParam: UInt32
    triggerOverwriteParamTablePos: UInt32
    localPropertyNameRefTablePos: UInt32
    numLocalPropertyNameRefTable: UInt32
    numLocalPropertyEnumNameRefTable: UInt32
    numDirectValueTable: UInt32
    numRandomTable: UInt32
    numCurveTable: UInt32
    numCurvePointTable: UInt32
    exRegionPos: UInt32
    numUser: UInt32
    conditionTablePos: UInt32
    nameTablePos: UInt32

    @classmethod
    def read(cls, br: BinaryReader):
        inst = cls()

        inst.magic = br.read_uint32()
        inst.dataSize = br.read_uint32()
        inst.version = br.read_uint32()
        inst.numResParam = br.read_uint32()
        inst.numResAssetParam = br.read_uint32()
        inst.numResTriggerOverwriteParam = br.read_uint32()
        inst.triggerOverwriteParamTablePos = br.read_uint32()
        inst.localPropertyNameRefTablePos = br.read_uint32()
        inst.numLocalPropertyNameRefTable = br.read_uint32()
        inst.numLocalPropertyEnumNameRefTable = br.read_uint32()
        inst.numDirectValueTable = br.read_uint32()
        inst.numRandomTable = br.read_uint32()
        inst.numCurveTable = br.read_uint32()
        inst.numCurvePointTable = br.read_uint32()
        inst.exRegionPos = br.read_uint32()
        inst.numUser = br.read_uint32()
        inst.conditionTablePos = br.read_uint32()
        inst.nameTablePos = br.read_uint32()

        return inst
