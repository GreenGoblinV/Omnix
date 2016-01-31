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
    fields = [
        [],
    ]
    def __init__(self, _bytes = None):
        self.sh_name = None
        self.sh_type = None
        self.sh_flags = None
        self.sh_addr = None
        self.sh_offset = None
        self.sh_size = None
        self.sh_link = None
        self.sh_info = None
        self.sh_addralign = None
        sh_entsize = None


