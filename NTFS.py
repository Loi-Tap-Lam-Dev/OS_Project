import os
import datetime

def as_datetime(windows_timestamp):
    return datetime.datetime.fromtimestamp((windows_timestamp - 116444736000000000) / 10000000)

SizeMFT = 0
class ContentOfStandardInformation:
    def __init__(self) -> None:
        # self.major_version = 0
        # self.minor_version = 0
        # self.flags = 0
        self.create_time = 0
        self.last_modification_time = 0
        self.last_mft_modification_time = 0
        self.last_access_time = 0
        # self.file_attribute = 0
        # self.max_version = 0
        # self.version = 0
        # self.class_id = 0
        # self.owner_id = 0
        # self.security_id = 0
        # self.quota_charged = 0
        # self.update_sequence_number = 0
        # self.reserved = 0
class ContentOfFileName:
    def __init__(self) -> None:
        self.IdRootParentDirectory = 0
        self.attr = ["NULL", "NULL", "NULL", "NULL", "NULL"]
        self.NameLength = 0
        self.Name = ''
        # self.parent_directory = 0
        # self.create_time = 0
        # self.last_modification_time = 0
        # self.last_mft_modification_time = 0
        # self.last_access_time = 0
        # self.logical_size = 0
        # self.logical_cluster_number = 0
        # self.flags = 0
        # self.real_size = 0
        # self.real_cluster_number = 0
        # self.file_name = 0
class Content:
    def __init__(self) -> None:
        self.standard_information = ContentOfStandardInformation()
        self.file_name = ContentOfFileName()
class Attribute: #type,size,
    def __init__(self) -> None:
        self.typeHeader = ''
        self.SizeOfAttributeIncludeHeader = 0 #bytesperAttributes
        self.NonResidentFlag = 0
        self.LengthOfContent = 0
        self.OffsetToContent = 0
        self.content = Content()
    # def __init__(self, type, name, size, data):
    #     self.type = type
    #     self.name = name
    #     self.size = size
    #     self.data = data
    def ReadAttribute(self,fp):
            #read type of attribute
            HeaderTypeHex = hex(int.from_bytes(fp.read(4),byteorder='little'))
            if(HeaderTypeHex == '0x10'):
                self.typeHeader = "STANDARD_INFORMATION"
            elif(HeaderTypeHex == '0x30'):
                self.typeHeader = "FILE_NAME"
            elif(HeaderTypeHex == '0x80'):
                self.typeHeader = "DATA"
            elif(HeaderTypeHex == '0x90'):
                self.typeHeader = "INDEX_ROOT"
            elif(HeaderTypeHex == '0xa0'):
                self.typeHeader = "INDEX_ALLOCATION"
            elif(HeaderTypeHex == '0xb0'):
                self.typeHeader = "BITMAP"
            elif(HeaderTypeHex == '0x100'):
                self.typeHeader = "VOLUME_NAME"
            elif(HeaderTypeHex == '0x120'):
                self.typeHeader = "VOLUME_INFORMATION"
            elif(HeaderTypeHex == '0xffffffff'):
                self.typeHeader = "END"
                return
            #read size of attribute
            self.SizeOfAttributeIncludeHeader = int.from_bytes(fp.read(4),byteorder='little')
            if(self.typeHeader == "DATA"):
                #if data attribute, read size of MFT (only in MFTentry[0])
                global SizeMFT
                fp.seek(16,1)
                SizeMFT = int.from_bytes(fp.read(8),byteorder='little')
                #seek to end of attribute
                fp.seek(self.SizeOfAttributeIncludeHeader-32,1)
                return
            #if not standard_information, file_name, end, data attribute -> seek to end of attribute
            elif(self.typeHeader != "STANDARD_INFORMATION" and self.typeHeader != "FILE_NAME" and self.typeHeader != "END" and self.typeHeader != "DATA"):
                fp.seek(self.SizeOfAttributeIncludeHeader-8,1)
                return
            #read NonResidentFlag
            self.NonResidentFlag = int.from_bytes(fp.read(1),byteorder='little')
            fp.seek(7,1)
            #read length of content
            self.LengthOfContent = int.from_bytes(fp.read(4),byteorder='little')
            #read offset to content
            self.OffsetToContent = int.from_bytes(fp.read(2),byteorder='little')
            #header 16 bytes, size of content 4 bytes, offset to content 2 bytes
            #fp dang o vi tri offset cuoi content
            #fp phai seek qua backup -> seek(vitri content -(16+4+2))
            fp.seek(self.OffsetToContent-22,1) 
            self.content = Content()
            if(self.typeHeader == "STANDARD_INFORMATION"):
                #read information of standard_information
                self.content.standard_information.create_time = as_datetime(int.from_bytes(fp.read(8),byteorder='little'))
                self.content.standard_information.create_time = self.content.standard_information.create_time.strftime("%d/%m/%Y %H:%M:%S")
                self.content.standard_information.last_modification_time = as_datetime(int.from_bytes(fp.read(8),byteorder='little'))
                self.content.standard_information.last_modification_time = self.content.standard_information.last_modification_time.strftime("%d/%m/%Y %H:%M:%S")
                self.content.standard_information.last_mft_modification_time = as_datetime(int.from_bytes(fp.read(8),byteorder='little'))
                self.content.standard_information.last_mft_modification_time = self.content.standard_information.last_mft_modification_time.strftime("%d/%m/%Y %H:%M:%S") 
                self.content.standard_information.last_access_time = as_datetime(int.from_bytes(fp.read(8),byteorder='little'))
                self.content.standard_information.last_access_time = self.content.standard_information.last_access_time.strftime("%d/%m/%Y %H:%M:%S")
                fp.seek(self.LengthOfContent-32,1)
            elif(self.typeHeader == "FILE_NAME"):
                #read information of file_name
                self.content.file_name.IdRootParentDirectory = int.from_bytes(fp.read(6),byteorder='little')
                fp.seek(50,1)
                getbinary = lambda x, n: format(x, 'b').zfill(n)
                attr = getbinary(int.from_bytes(fp.read(4),byteorder='little'),32)
                attr = attr[::-1]
                for i in range(len(attr)):
                    if(attr[i] == '1'):
                        if(i == 0):
                            self.content.file_name.attr[0] = "READ_ONLY"
                        elif(i == 1):
                            self.content.file_name.attr[1] = "HIDDEN"
                        elif(i == 2):
                            self.content.file_name.attr[2] = "SYSTEM"
                        elif(i == 5):
                            self.content.file_name.attr[3] = "ARCHIVE"
                        elif(i== 28):
                            self.content.file_name.attr[4] = "DIRECTORY"
                fp.seek(4,1)
                self.content.file_name.NameLength = int.from_bytes(fp.read(1),byteorder='little')
                fp.seek(1,1)
                for i in range(self.content.file_name.NameLength):
                    eachName = fp.read(2)
                    if eachName != b'\xff\xff':
                        self.content.file_name.Name += eachName.decode('utf-16')
                self.content.file_name.Name = self.content.file_name.Name.replace('\x00','')
                fp.seek(self.SizeOfAttributeIncludeHeader - (self.OffsetToContent+self.LengthOfContent),1)
            else:
                fp.seek(self.SizeOfAttributeIncludeHeader-4,1)
class MFTEntry:
    def __init__(self) -> None:
        self.MFTEntry = ''
        self.OffSetFirstAttri = 0
        self.Flag = ''
        self.SizeofusedMFTE = 0
        self.SizeofMFTE = 0
        self.IDofMFTEntry = 0
        self.sizeMFT = 0
        self.isROOT = False
        self.attributes = []
        self.listEntry = []
    def ReadMFTEntry(self,fp, driveName):
        #each MFT Entry has 1024 bytes but MFT Entry can have 1024 bytes 00
        #check if MFT Entry has 1024 bytes 00 -> seek to next MFT Entry
        #else -> seek back to the beginning of MFT Entry and read
        if(int.from_bytes(fp.read(1024), byteorder = 'little') != 0):
            fp.seek(-1024,1)
        else:
            return
        #read MFT Entry is FILE or BAAD
        for i in range(4):
            temp = fp.read(1)
            self.MFTEntry += temp.decode('ascii')
        self.MFTEntry = self.MFTEntry.replace('\x00','')
        #seek to 16 bytes from the beginning of MFT Entry to offset 14
        fp.seek(16,1)
        #read offset to first attribute
        self.OffSetFirstAttri = int.from_bytes(fp.read(2),byteorder='little') #luu tru = bytes
        #read 2 bytes flag
        flag = hex(int.from_bytes(fp.read(2),byteorder='little'))
        if(flag == '0x0'):
            self.Flag = "File has already deleted"
        elif(flag == '0x1'):
            self.Flag = "File is in use"
        elif(flag == '0x2'):
            self.Flag = "Directory has already deleted"
        elif(flag == '0x3'):
            self.Flag = "Directory is in use"
        #read 4 bytes Size of used MFT Entry
        self.SizeofusedMFTE = int.from_bytes(fp.read(4),byteorder='little')
        #read 4 bytes Size of MFT Entry
        self.SizeofMFTE = int.from_bytes(fp.read(4),byteorder='little')
        fp.seek(12,1)
        #read 4 bytes ID of MFT Entry
        self.IDofMFTEntry = int.from_bytes(fp.read(4),byteorder='little')
        #seek to offfset first attribute but minus 48 bytes (48 bytes which we have already read over)
        fp.seek(self.OffSetFirstAttri-48,1)
        while(True):
            temp = Attribute()
            #read attribute
            temp.ReadAttribute(fp)
            if(temp.typeHeader == 'STANDARD_INFORMATION' or temp.typeHeader == 'FILE_NAME'):
                #add attribute to list attribute
                self.attributes.append(temp)
                #check if MFT Entry is ROOT
                if temp.content.file_name.IdRootParentDirectory == self.IDofMFTEntry:
                    self.isROOT = True
                    #is ROOT = true -> this is MFT of Drive -> change name from '.' to drivename
                    for i in range(len(self.attributes)):
                        if self.attributes[i].typeHeader == 'FILE_NAME':
                            self.attributes[i].content.file_name.Name = driveName
            if(temp.typeHeader == "END"): #if attribute is END -> break
                break
        fp.seek(self.SizeofMFTE - self.SizeofusedMFTE+4,1) #seek to next MFT Entry 
        return self
class MFT:
    def __init__(self) -> None:
        self.MFT = []
        self.Dictionary = {}
        self.MFTsize = 0
    def ReadMFT(self,drive,fp,offset,bytePerCluster):
        #seek to First Cluster in MFT
        fp.seek(offset)
        #Read MFT entry[0] to get the size of MFT
        temp = MFTEntry()
        temp.ReadMFTEntry(fp, drive[4:])
        self.MFTsize = SizeMFT #size of MFT is VCN in attribute data (virtual cluster number)
        #Read each MFT entry, IF fp pointer > size of MFT, break
        while(True and fp.tell() <= (offset + self.MFTsize*bytePerCluster)):
            temp = MFTEntry()
            temp.ReadMFTEntry(fp, drive[4:])
            #IF MFT entry is FILE, add to MFT and Dictionary
            if(temp.MFTEntry == 'FILE'):
                self.MFT.append(temp)
                self.Dictionary[temp.IDofMFTEntry] = temp
                continue
            elif(temp.MFTEntry == 'BAAD'):
                self.MFT.append(temp)
                continue
        return self
    
    def PrintMFT(self):
        for i in range(len(self.MFT)):
            print("MFT Entry: ",i)
            print("MFT Entry: ",self.MFT[i].MFTEntry)
            print("Offset First Attribute: ",self.MFT[i].OffSetFirstAttri)
            print("Flag: ",self.MFT[i].Flag)
            print("Size of used MFT Entry: ",self.MFT[i].SizeofusedMFTE)
            print("Size of MFT Entry: ",self.MFT[i].SizeofMFTE)
            print("ID of MFT Entry: ",self.MFT[i].IDofMFTEntry)
            for j in range(len(self.MFT[i].attributes)):
                self.typeHeader = ''
                print("Attribute: ",j)
                print("Type Header: ",self.MFT[i].attributes[j].typeHeader)
                print("Length of Attribute: ",self.MFT[i].attributes[j].SizeOfAttributeIncludeHeader)
                print("Nonresident: ",self.MFT[i].attributes[j].NonResidentFlag)
                print("Length of Name: ",self.MFT[i].attributes[j].LengthOfContent)
                print("Offset to Name: ",self.MFT[i].attributes[j].OffsetToContent)
                if(self.MFT[i].attributes[j].typeHeader == 'STANDARD_INFORMATION'):
                    print("Creation Time: ",self.MFT[i].attributes[j].content.standard_information.create_time)
                    print("Last Modified Time: ",self.MFT[i].attributes[j].content.standard_information.last_modification_time)
                    print("Last MFT Modified Time: ",self.MFT[i].attributes[j].content.standard_information.last_mft_modification_time)
                    print("Last Accessed Time: ",self.MFT[i].attributes[j].content.standard_information.last_access_time)
                if(self.MFT[i].attributes[j].typeHeader == 'FILE_NAME'):
                    print("Parent Directory: ",self.MFT[i].attributes[j].content.file_name.IdRootParentDirectory)
                    print("Name: ",self.MFT[i].attributes[j].content.file_name.Name)
                    for k in range(len(self.MFT[i].attributes[j].content.file_name.attr)):
                        print("Attribute: ",self.MFT[i].attributes[j].content.file_name.attr[k])
            print("--------------------------------------------")
    
    # def PrintMFT(self):
    #         y = 1
    #         for i in range(len(self.MFT)):
    #             for j in range(len(self.MFT[i].attributes)):
    #                 if(self.MFT[i].attributes[j].typeHeader == 'FILE_NAME'):
    #                     if(self.MFT[i].attributes[j].content.file_name.attr[1] == "NULL" and self.MFT[i].attributes[j].content.file_name.attr[2] == "NULL"):
    #                             print(self.MFT[i].attributes[j].content.file_name.Name)
                            
class VBR:
    def __init__(self) -> None:
        self.BytesPerSector = 0
        self.SectorsPerCluster = 0
        self.SectorsPerTrack = 0
        self.NumberOfHead = 0
        self.TotalSector = 0
        self.FirstClusterInMFT = 0 
        self.FirstClusterInMFTMirr = 0
        self.BytesPerEntryMFT = 0 #Byte per MFT Entry
    def ReadVBR(self,drive,fp):
            #BytesPerSector in offset 0B -> read or seek 11 bytes -> 0B 00
            fp.read(11)
            #BytesPerSector in offset 0B -> read 2 bytes, fp pointer after read at 0D
            self.BytesPerSector = int.from_bytes(fp.read(2),byteorder='little')
            #SectorsPerCluster in offset 0D -> read 1 byte, fp pointer after read at 0E
            self.SectorPerCluster = int.from_bytes(fp.read(1),byteorder='little')
            #SectorsPerTrack in offset 18 -> from 0E to 18 seek 10 bytes
            fp.seek(10,1)
            #SectorsPerTrack in offset 18 -> read 2 bytes, fp pointer after read at 1A
            self.SectorPerTrack = int.from_bytes(fp.read(2),byteorder='little')
            #NumberOfHead in offset 1A -> read 2 bytes, fp pointer after read at 1C
            self.NumberOfHead = int.from_bytes(fp.read(2),byteorder='little')
            #TotalSector in offset 28 -> from 1C to 28 seek 12 bytes
            fp.seek(12,1)
            #TotalSector in offset 28 -> read 8 bytes, fp pointer after read at 30
            self.TotalSector = int.from_bytes(fp.read(8),byteorder='little')
            #FirstClusterInMFT in offset 30 -> from 30 to 38 seek 8 bytes
            self.FirstClusterInMFT = int.from_bytes(fp.read(8),byteorder='little')
            #FirstClusterInMFTMirr in offset 38 -> from 38 to 40 seek 8 bytes
            self.FirstClusterInMFTMirr = int.from_bytes(fp.read(8),byteorder='little')
            #BytesPerEntryMFT in offset 40 -> from 40 to 48 seek 8 bytes
            BinPerMFTEntry = int.from_bytes(fp.read(1),byteorder='little',signed=True)
            #move to 2^bù 2
            self.BytesPerEntryMFT = 2**abs(BinPerMFTEntry) #so byte cua 1 entry MFT
    def PrintVBR(self):
        print("Byte per Sector: ",self.BytesPerSector)
        print("Sector Per Cluster: ",self.SectorPerCluster)
        print("Sector Per Track: ",self.SectorPerTrack)
        print("Number Of Head: ",self.NumberOfHead)
        print("Total Sector: ",self.TotalSector)
        print("MFT First Cluster: ",self.FirstClusterInMFT)
        print("MFT First Mirr Cluster: ",self.FirstClusterInMFTMirr)
        print("Bytes Per Entry MFT: ",self.BytesPerEntryMFT)
