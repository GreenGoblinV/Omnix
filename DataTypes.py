"""
Data Types
"""

#
class byte(bytearray):
    def __add__(self, other):
        ret = byte()
        over = 0
        for i in range(1,len(self)):
            temp = self[-i] + other[-i] + over
            if temp > 0xff:
                over = temp - 0xff
                temp = 255
            else:
                over = 0x00
            ret[-i] = temp
        if over > 0:
            while not over <= 0:
                pass
            

#
class word(bytearray):
    pass


#    
class dword(bytearray):
    pass
    

#
class qword(bytearray):
    pass


#
class int16(bytearray):
    pass


#
class uint16(bytearray):
    pass


#
class int32(bytearray):
    pass


#
class uint32(bytearray):
    pass
    

#
class int64(bytearray):
    pass
    
 
# 
class uint64(bytearray):
    pass


#
class int128(bytearray):
    pass



#
class uint128(bytearray):
    pass



#
class float32(bytearray):
    pass


#
class float64(bytearray):
    pass
    
 
#
class float128(bytearray):
    pass