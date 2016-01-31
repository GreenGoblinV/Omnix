
# COFF file header
class COFFFileHeader(Structure):
    def __init__(self):
        self.fields = [
            # Name, Offset, Size
            ['Machine', 0, 2, None],
            ['NumberOfSections', 2, 2, None],
            ['TimeDateStamp', 4, 4, None],
            ['PointerToSymbolTable', 8, 4, None],
            ['NumberOfSymbols', 12, , None],
            ['SizeOfOptionalHeader', 16, 2, None],
            ['Characteristics', 18, 4, None]
        ]
        Structure.__init__(self)


class StandardCOFFFields(Structure):
    def __init__(self):
        self.fields = [
            ['Magic', 0, 2, None],
            ['MajorLinkerVersion', 2, 1, None],
            ['MinorLinkerVersion', 3, 1, None],
            ['SizeOfCode', 4, 4, None],
            ['SizeOfInitializedData', 8, 4, None],
            ['SizeOfUnitializedData', 12, 4, None],
            ['EntryPoint', 16, 4, None],
            ['BaseOfCode', 20, 4, None],
            ['BaseOfData', 24, 4, None],
        ]
        Structure.__init__(self)


class MicrosoftSpecificFields(Structure):
    def __init__(self):
        self.fields = [ 
            ['ImageBase', 28, 4, None],
            ['SectionAlignment', 32, 4, None],
            ['FileAlignment', 36, 4, None],
            ['MajorOsVersion', 40, 2, None],
            ['MinorOsVersion', 42, 2, None],
            ['MajorImageVersion', 44, 2, None],
            ['MinorImageVersion', 46, 2, None],
            ['MajorSubSystemVersion', 48, 2, None],
            ['MinorSubSystemVersion', 50, 2, None],
            ['Win32VersionValue', 52, 4, None],
            ['SizeOfImage', 56, 4, None],
            ['SizeOfHeaders', 60, 4, None],
            ['Checksum', 64, 4, None],
            ['Subsystem', 68, 2, None],
            ['DllCharacteristics', 70, 2, None],
            ['SizeOfStackReserve', 72, 4, None],
            ['SizeOfStackCommit', 76, 4, None],
            ['SizeOfHeapReserve', 80, 4, None],
            ['SizeOfHeapCommit', 84, 4, None],
            ['LoaderFlags', 88, 4, None],
            ['NumberOfRVAsAndSizes', 92, 4, None]
        ]
        Structure.__init__(self)
    

# Optional Header
class OptionalHeader(Structure):
    def __init__(self):
        self.fields = [
            ['StandardCOFFFields', 0, 28, StandardCOFFFields],
            ['MicrosoftSpecificFields', 28, 68, \
                MicrosoftSpecificFields],
            ['DataDirectories', 96, 0, DataDirectories]
        ]
        Structure.__init__(self)
    

# PE Section Header
class PESectionHeader(Structure):
    def __init__(self):
        self.fields = [
            ['Name', 0, 8, None],
            ['VirtualSize', 8, 4, None],
            ['VirtualAddress', 12, 4, None],
            ['SizeOfRawDate', 16, 4, None],
            ['PointerToRawDate', 20, 4, None],
            ['PointerToRelocations', 24, 4, None],
            ['PointerToLinenumbers', 28, 4, None],
            ['NumberOfRelocations', 32, 2, None],
            ['NumberOfLineNumbers', 34, 2, None],
            ['Characteristics', 36, 4, None]
        ]
        Structure.__init__(self)



#
class ExportDirectoryTable(Structure):
    def __init__(self):
        self.fields = [
            ['ExportFlags', 0, 4, None],
            ['TimeDateStamp', 4, 4, None],
            ['MajorVersion', 8, 2, None],
            ['MinorVersion', 10, 2, None],
            ['NameRVA', 12, 4, None],
            ['OrdinalBase', 16, 4, None],
            ['AddressTableEntries', 20, 4, None],
            ['NumberOfNamePointers', 24, 4, None],
            ['ExportAddressTableRVA', 28, 4, None],
            ['NamePointerRVA', 32, 4, None],
            ['OrdinalTableRVA', 36, 4, None],
        ]
        Structure.__init__(self)


class ImportDirectoryTable(Structure):
    def __init__(self):
        self.fields = [
            ['ImportLookupTableRBA'],
            ['TimeDateStamp'],
            ['ForwarderChain'],
            ['NameRVA'],
            ['ImportAddressTableRVA'],
        ]
        Structure.__init__(self)


#
class ImportLookupTable(Structure):
    def __init__(self):
        self.fields = [
            ['OrdinalNameFlag'],
            ['OrdinalNumber'],
            ['HintNameTableRVA']
        ]
        Structure.__init__(self)

    
#
class ImportHeader(Structure):
    def __init__(self):
        self.fields = [
            ['Sig1', 0, 2, None],
            ['Sig2', 2, 2, None],
            ['Version', 4, 2, None],
            ['Machine', 6, 2, None],
            ['TimeDateStamp', 8, 4, None],
            ['SizeOfDate', 12, 4, None],
            ['OrdinalHint', 16, 2, None],
            ['Type', 18, bits(2), None],
            ['NameType', , bits(3), None],
            ['Reserverd', , bits(11), None]
        ]
        Structure.__init__(self)
    

#
class ImportPages(Structure):
    def __init__(self):
        self.fields = [
            [],
        ]
        Structure.__init__(self)




#
class LoadConfigurationStructure(Structure):
    def __init__(self):
        self.fields = [
            ['Characteristics'],
            ['TimeDateStamp'],
            ['MajorVersion'],
            ['MinorVersion'],
            ['GlobalFlagsClear'],
            ['GlobalFlagsSet'],
            ['CriticalSectionDefaultTimeout'],
            ['DeCommitFreeBlockThreshold'],
            ['DeCommitTotlaFreeThreshold'],
            ['LockPrefixTable'],
            ['MaximumAllocationSize'],
            ['VirtualMemoryThreshold'],
            ['ProcessAffinityMask'],
            ['ProcessHeapFlags'],
            ['CSDVersion'],
            ['Reserved'],
            ['EditList'],
            ['SecurityCookie'],
            ['SEHandlerTable'],
            ['SEHandlerCount'],
        ]
        Structure.__init__(self)


#
class ProtableExecutable(object):
    def __init__(self):

    
    magic_doc_chars = b'MZ'
    magic_pe_chars = b'PE\x00\x00'
    pe_header_offset_loc = b'\x3c'
    
    def __init__(self, filename):
        self.fields = [
            ['MSDOSSection', 0, 0, MSDOSSection],
            ['PEHeader', None, 0, PEHeader],
            ['COFFFileHeader', None, 22, COFFFileHeader],
            ['OptionalHeader', None, 96, OptionalHeader],
            ['ImportPages', None, 0, ImportPages]
        ]
        self.file_name = filename
        self.file_handle = None
        self.exe_type = None
        self.has_dos_header = None
        self.offset_to_pe_header = None
        self.oset_coff_header = None
        self.oset_opt_header = None
        Structure.__init__(self)









EXE = None
        
def sanityCheck0(args):
    pass


def procArgs(args):
    pass


def sanityCheck1():
    pass

    
def openFileRaw(exe):
    pass


def sanityCheck2():
    pass


def isPEFile(exe):
    return False


def sanityCheck3():
    pass


def readPEAttrs(exe):
    pass

    
def sanityCheck4():
    pass


def printPEAttrs(exe):
    pass

    
def sanityCheck5():
    pass



if __name__ == '__main__':
    global EXE
    sanityCheck0(sys.args)
    procArgs(sys.args)
    sanityCheck1()
    openFileRaw(EXE)
    sanityCheck2()
    if isPEFile(EXE):
        sanityCheck3()
        readPEAttrs(EXE)
        sanityCheck4()
        printPEAttrs(EXE)
    sanityCheck5()
    return 0