import ctypes

Elf32_Addr = ctypes.c_uint32
Elf32_Half = ctypes.c_uint16
ELF32_Off = ctypes.c_uint32
Elf32_Sword = ctypes.c_int32
Elf32_Word = ctypes.c_uint32
unsigned_char = ctypes.c_uint8



class E_Ident(Structure):
    def __init__(self, _bytes = None):
        self.fields = [
            ['EI_MAG', 0x00, 4, None],
            ['EI_CLASS', 0x04, 1, None],
            ['EI_DATA', 0x05, 1, None],
            ['EI_VERSION', 0x06, 1, None],
            ['EI_OSABI', 0x07, 1, None],
            ['EI_ABIVERSION', 0x08, 1, None],
            ['EI_PAD', 0x09, 7, None]
        ]
        Structure.__init__(self)


# ELF File Format
class ELFHeader(object):
    def __init__(self, _bytes = None):
        self.fields = [
            ['e_ident', 0x0, 16, E_Ident],
            ['e_type', 0x10, 2, None],
            ['e_machine', 0x12, 2, None],
            ['e_version', 0x14, 4, None],
            ['e_entry', 0x18, 4, None],
            ['e_phoff', 0x1C, 4, None],
            ['e_shoff', 0x20, 4, None],
            ['e_flags', 0x24, 4, None],
            ['e_ehsize', 0x28, 2, None],
            ['e_phentsize', 0x2A, 2, None],
            ['e_phnum', 0x2C, 2, None],
            ['e_shentsize', 0x2E, 2, None],
            ['e_shnum', 0x30, 2, None],
            ['e_shstrndx', 0x32, 2, None]
        ]
        Structure.__init__(self)




class ProgramHeader(object):
    def __init__(self, _bytes = None):
        fields = [
            ['p_type', 0x00, 4, None],
            ['p_offset', 0x04, 4, None],
            ['p_vaddr', 0x08, 4, None],
            ['p_paddr', 0x0C, 4, None],
            ['p_filesz', 0x10, 4, None],
            ['p_memsz', 0x14, 4, None],
            ['p_flags', 0x18, 4, None],
            ['p_align', 0x1C, 4, None]
        ]
        Structure.__init__(self)
        

class SectionHeader(object):

    def __init__(self, _bytes = None):
        self.fields = [
            #This member specifies the name of the section.
            ['sh_name', 0x00, 4, None],
            # Categorizes the section's contents/semantics
            ['sh_type', 0x04, 4, None],
            # Describe miscellaneous attributes.
            ['sh_flags', 0x08, 4, None],
            # Address where section's 1st byte should reside
            ['sh_addr', 0x0C, 4, None],
            # Offset from beginning of file to 1st byte in the section.
            ['sh_offset', 0x10, 4, None],
            # The section's size in bytes
            ['sh_size', 0x14, 4, None],
            # Holds a section header table index link.
            ['sh_link', 0x18, 4, None],
            # Holds extra info, interpretation depends on the section type.
            ['sh_info', 0x1C, 4, None],
            # Alignment constraints
            ['sh_addralign', 0x20, 4, None],
            # Size of fixed sized entries, 0 if variable sized entries.
            ['sh_entsize', 0x24, 4, None]
        ]
        Structure.__init__(self)
#



#
class StringTable(Structure):
    def __init__(self):
        self.fields = [
            ['st_strings', 0x00, 0, None],
        ]
        Structure.__init__(self)
#


#
class SymbolTableEntry(Structure):
    def __init__(self):
        self.fields = [
            ['st_name', 0x00, 4, Elf32_Word],
            ['st_value', 0x04, 4, Elf32_Addr],
            ['st_size', 0x08, 4, Elf32_Word],
            ['st_info', 0x0C, 1, unsigned_char],
            ['st_other', 0x0D, 1, unsigned_char],
            ['st_shndx', 0x0E, 2, Elf32_Half]
        ]
        Structure.__init__(self)
#

class Elf32_Rel(Structure):
    def __init__(self):
        self.fields = [
            ['r_offset', 0x00, 4, Elf32_Addr],
            ['r_info', 0x04, 4, Elf32_Word]
        ]
        Structure.__init__(self)
#

#
class Elf32_Rela(Structure):
    def __init__(self):
        self.fields = [
            ['r_offset', 0x00, 4, Elf32_Addr],
            ['r_info', 0x04, 4, Elf32_Word]
            ['r_addend', 0x08, 4, Elf32_Sword]
        ]
        Structure.__init__(self)
#


#
class ProgramHeaderTable(Structure):
    pass
#


#
class SectionHeaderTable(Structure):
    pass
#


#
class ELFRelocatable(Structure):
    pass
#

    

#
class ELFExecutable(Structure):
    pass
#


#
class ELFSharedObject(Structure):
    pass
#