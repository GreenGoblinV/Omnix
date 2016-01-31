# ELF File Format
class ELFHeader(object):
    fields = [
        [],
    ]
    def __init__(self):
        self.e_ident = bytearray([
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
            ])
        self.e_type = bytearray([0,0])
        self.e_machine = bytearray([0,0,0,0])
        self.e_version = bytearray([0,0,0,0])
        self.e_entry = bytearray([0,0,0,0])
        self.e_phoff = bytearray([0,0,0,0])
        self.e_shoff = bytearray([0,0,0,0])
        self.eflags = bytearray([0,0,0,0])
        self.e_ensize = bytearray([0,0])
        self.e_phentsize = bytearray([0,0])
        self.e_phnum = bytearray([0,0])
        self.e_shentsize = bytearray([0,0])
        self.e_shnum = bytearray([0,0])
        self.e_shstrndx = bytearray([0,0])
        

class ELFSectionHeader(object):
    fields = [
        [],
    ]
    def __init__(self):
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


class ELFProgramHeader(object):
    fields = [
        [],
    ]
    def __init__(self):
        self.p_type = None
        self.p_offset = None
        self.p_vaddr = None
        self.p_paddr = None
        self.p_filesz = None
        self.p_memsz = None
        self.p_flags = None
        self.p_align = None
