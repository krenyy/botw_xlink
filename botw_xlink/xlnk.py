from pathlib import Path
from typing import Union

from .binary import BinaryReader
from .header import Header
from .tables.conditiontable import ConditionTable
from .tables.curvepointtable import CurvePointTable
from .tables.curvetable import CurveTable
from .tables.directvaluetable import DirectValueTable
from .tables.exregion import ExRegion
from .tables.nametable import NameTable
from .tables.paramdefinetable import ParamDefineTable
from .tables.paramtable import ParamTable
from .tables.randomtable import RandomTable
from .tables.reftable import RefTable
from .tables.userdatatable import UserDataTable


class XLNK:
    header: Header
    userDataTable: UserDataTable
    paramDefineTable: ParamDefineTable

    resourceAssetParamTable: ParamTable
    triggerOverwriteParamTable: ParamTable

    localPropertyNameRefTable: RefTable
    localPropertyEnumNameRefTable: RefTable

    directValueTable: DirectValueTable
    randomTable: RandomTable
    curveTable: CurveTable
    curvePointTable: CurvePointTable

    exRegion: ExRegion

    conditionTable: ConditionTable
    nameTable: NameTable

    @classmethod
    def frombinary(cls, data: bytes):
        inst = cls()

        br = BinaryReader(data)
        br.big_endian = True

        inst.header = Header.read(br)
        inst.userDataTable = UserDataTable.read(br, inst.header.numUser)
        inst.paramDefineTable = ParamDefineTable.read(br)

        inst.resourceAssetParamTable = ParamTable.read(br,
                                                       inst.header.triggerOverwriteParamTablePos - br.tell())
        inst.triggerOverwriteParamTable = ParamTable.read(br,
                                                          inst.header.localPropertyNameRefTablePos - br.tell())

        inst.localPropertyNameRefTable = RefTable.read(br, inst.header.numLocalPropertyNameRefTable)
        inst.localPropertyEnumNameRefTable = RefTable.read(br,
                                                           inst.header.numLocalPropertyEnumNameRefTable)

        inst.directValueTable = DirectValueTable.read(br, inst.header.numDirectValueTable)
        inst.randomTable = RandomTable.read(br, inst.header.numRandomTable)
        inst.curveTable = CurveTable.read(br, inst.header.numCurveTable)
        inst.curvePointTable = CurvePointTable.read(br, inst.header.numCurvePointTable)

        assert br.tell() == inst.header.exRegionPos
        inst.exRegion = ExRegion.read(br, inst.header.conditionTablePos - inst.header.exRegionPos)

        inst.conditionTable = ConditionTable.read(br, inst.header.nameTablePos-br.tell())
        inst.nameTable = NameTable.read(br)

        return inst

    @classmethod
    def fromfile(cls, path: Union[Path, str]):
        with open(path, 'rb') as f:
            return cls.frombinary(f.read())
