from ctypes import *

"""
Class: Structure
    Handles the logic behind building up a header or table,
    based on some given information. It will hopefully be
    applicable to all sorts of binary streams with static or
    variable sized member fields. The idea is taken from
    scapy.
"""
class Structure(object):
    fields = [['name', 'offset', 'size', 'type']]
    field_idx_cache = {}
    def __init__(self, _bytes = None):
        self.bytes = []
        for i in range(len(self.fields)):
            if self.fields[3] is None:
                self.bytes.append(bytearray(
                    b'\x00' * self.fields[i][2])
                    )
            elif self.fields[3]:
                self.bytes.append(self.fields[3]())
    
    def __getattr__(self, attr):
        if attr in self.field_idx_cache:
            return \
                self.bytes[
                    self.field_idx_cache[attr]
                    ]
        for i in range(len(self.fields)):
            if self.fields[i][0] == attr:
                self.field_idx_cache[attr] = i
                return self.bytes[i]
                
    def __setattr__(self, attr, rval):
        if attr in self.field_idx_cache:
            self.bytes[
                self.field_idx_cache[attr]
                ] = rval
                return
        for i in range(len(self.fields)):
            if self.fields[i][0] == attr:
                self.field_idx_cache[attr] = i
                self.bytes[i] = rval
                return
        object.__getattr__(self, attr, rval)
        return


#
#
class Padding(Structure):
    def __init__(self, _bytes = None):
        self.fields = [
            ['padding', 0, 0, None]
        ]
        Structure.__init__(self)

#
#
