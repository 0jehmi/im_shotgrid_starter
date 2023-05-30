# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Welcome(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Welcome()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsWelcome(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Welcome
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Welcome
    def Session(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Welcome
    def Roles(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from wamp.proto.RouterRoles import RouterRoles
            obj = RouterRoles()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Welcome
    def Realm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Welcome
    def Authid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Welcome
    def Authrole(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Welcome
    def Authmethod(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Welcome
    def Authprovider(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Welcome
    def Authextra(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from wamp.Map import Map
            obj = Map()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Welcome
    def Resumed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Welcome
    def Resumable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Welcome
    def ResumeToken(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def WelcomeStart(builder): builder.StartObject(11)
def Start(builder):
    return WelcomeStart(builder)
def WelcomeAddSession(builder, session): builder.PrependUint64Slot(0, session, 0)
def AddSession(builder, session):
    return WelcomeAddSession(builder, session)
def WelcomeAddRoles(builder, roles): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(roles), 0)
def AddRoles(builder, roles):
    return WelcomeAddRoles(builder, roles)
def WelcomeAddRealm(builder, realm): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(realm), 0)
def AddRealm(builder, realm):
    return WelcomeAddRealm(builder, realm)
def WelcomeAddAuthid(builder, authid): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(authid), 0)
def AddAuthid(builder, authid):
    return WelcomeAddAuthid(builder, authid)
def WelcomeAddAuthrole(builder, authrole): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(authrole), 0)
def AddAuthrole(builder, authrole):
    return WelcomeAddAuthrole(builder, authrole)
def WelcomeAddAuthmethod(builder, authmethod): builder.PrependUint8Slot(5, authmethod, 0)
def AddAuthmethod(builder, authmethod):
    return WelcomeAddAuthmethod(builder, authmethod)
def WelcomeAddAuthprovider(builder, authprovider): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(authprovider), 0)
def AddAuthprovider(builder, authprovider):
    return WelcomeAddAuthprovider(builder, authprovider)
def WelcomeAddAuthextra(builder, authextra): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(authextra), 0)
def AddAuthextra(builder, authextra):
    return WelcomeAddAuthextra(builder, authextra)
def WelcomeAddResumed(builder, resumed): builder.PrependBoolSlot(8, resumed, 0)
def AddResumed(builder, resumed):
    return WelcomeAddResumed(builder, resumed)
def WelcomeAddResumable(builder, resumable): builder.PrependBoolSlot(9, resumable, 0)
def AddResumable(builder, resumable):
    return WelcomeAddResumable(builder, resumable)
def WelcomeAddResumeToken(builder, resumeToken): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(resumeToken), 0)
def AddResumeToken(builder, resumeToken):
    return WelcomeAddResumeToken(builder, resumeToken)
def WelcomeEnd(builder): return builder.EndObject()
def End(builder):
    return WelcomeEnd(builder)