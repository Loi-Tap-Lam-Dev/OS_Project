import binascii

class BootSectorFAT32:
    def __init__(self) -> None:
        self.bytePerSector = 0
        self.sectorPerCluster = 0
        self.sectorBeforeFAT = 0
        self.cntFAT = 0
        self.sizeVol = 0
        self.sectorPerFAT = 0
        self.firstClusterinRDET = 0
        self.FATtypeEach = 0
        self.FATtype = ""
    def ReadBootSector(self, drive):
        with open(drive, 'rb') as fp:
            fp.read(11)
            self.bytePerSector = int.from_bytes(fp.read(2), byteorder='little')
            self.sectorPerCluster = int.from_bytes(fp.read(1), byteorder='little')
            self.sectorBeforeFAT = int.from_bytes(fp.read(2), byteorder='little')
            self.cntFAT = int.from_bytes(fp.read(1), byteorder='little') # End At 0x11
            fp.seek(15,1)
            self.sizeVol = int.from_bytes(fp.read(4), byteorder='little')
            self.sectorPerFAT = int.from_bytes(fp.read(4), byteorder='little') # End At 0x28
            fp.seek(4,1)
            self.firstClusterinRDET = int.from_bytes(fp.read(4), byteorder='little') #End At 0x30
            fp.seek(34,1)
            #self.FATtypeEach = int.from_bytes(fp.read(8), byteorder='little')
            for i in range(8):
                self.FATtypeEach = int.from_bytes(fp.read(1), byteorder='little')
                self.FATtype += chr(self.FATtypeEach)
        return 0
    
    def PrintBootSector(self):
        print("Byte per sector: ", self.bytePerSector)
        print("Sector per cluster: ", self.sectorPerCluster)
        print("Sector before FAT: ", self.sectorBeforeFAT)
        print("Count of FAT: ", self.cntFAT)
        print("Size of volume: ", self.sizeVol)
        print("Sector per FAT: ", self.sectorPerFAT)
        print("First cluster in RDET: ", self.firstClusterinRDET)
        print("FAT type: ", self.FATtype)

class MBR:
    def __init__(self) -> None:
        self.status = 0
        self.startAdd = 0
        self.patitionType = 0
        self.endAdd = 0
        self.startSector = 0
        self.totalSector = 0
    def readMBR(self, drive):
        with open(drive, 'rb') as fp:
            fp.read(446)
            self.status = hex(int.from_bytes(fp.read(1), byteorder = 'big'))
            self.startAdd = hex(int.from_bytes(fp.read(3), byteorder = 'big'))
            self.patitionType = hex(int.from_bytes(fp.read(1), byteorder = 'big'))
            self.endAdd = hex(int.from_bytes(fp.read(3), byteorder = 'big'))
            self.startSector = (int.from_bytes(fp.read(4), byteorder='little'))
            self.totalSector = (int.from_bytes(fp.read(4), byteorder='big'))
        return 0
    def PrintMBR(self):
        print("Status: ", self.status)
        print("Start Address: ", self.startAdd)
        print("Partition Type: ", self.patitionType)
        print("End Address: ", self.endAdd)
        print("Start Sector: ", hex(int(self.startSector)))
        print("Total Sector: ", self.totalSector)

# class RDET:
#     def __init__(self) -> None:
#         self.name = ""
#         self.attr = 0
#         self.reserved = 0
#         self.createTime = 0
#         self.createDate = 0
#         self.lastAccessDate = 0
#         self.firstCluster = 0
#         self.lastWriteTime = 0
#         self.lastWriteDate = 0
#         self.size = 0
#     def readRDET(self, drive, sector, offset):
#         with open(drive, 'rb') as fp:
#             fp.seek(sector*512 + offset*32)
#             self.name = fp.read(8)
#             self.attr = fp.read(1)
#             self.reserved = fp.read(1)
#             self.createTime = fp.read(2)
#             self.createDate = fp.read(2)
#             self.lastAccessDate = fp.read(2)
#             self.firstCluster = fp.read(2)
#             self.lastWriteTime = fp.read(2)
#             self.lastWriteDate = fp.read(2)
#             self.size = fp.read(4)
#         return 0
#     def ReadMainEntry(self, address):
#         with open(drive, 'rb') as fp:
#             fp.seek(address)
#             #check offset đầu của entry chính, E5 -> đã xóa, 00 -> rỗng, khác -> đang lưu trữ file/ thư mục khác
#             state = hex(int.from_bytes(fp.read(1), byteorder = 'little')) #end at 0x00
#             #Đọc tên chính
#             fp.seek(1,0)
#             for i in range(8):
#                 eachName  = int.from_bytes(fp.read(1), byteorder='little')
#                 self.name += chr(self.eachName)
#             #Đọc phần mở rộng
#             self.name += "."
#             for i in range(3):
#                 eachName  = int.from_bytes(fp.read(1), byteorder='little')
#                 self.name += chr(self.eachName)
#             #Đọc thuộc tính
#             bi = bin(int.from_bytes(fp.read(1), byteorder = 'little'))
#             for i in range(8):
#                 if bin[i] == '1':
#                     if i==2:
#                         self.attr = "Archive"
#                     elif i==3:
#                         self.attr = "Directory"
#                     elif i==4:
#                         self.attr = "Volume Label"
#                     elif i==5:
#                         self.attr = "System File"
#                     elif i == 6:
#                         self.attr = "Hidden File"
#                     elif i==7:
#                         self.attr = "Read Only"
#             fp.seek(8,1)
#             halfBin += bin(int.from_bytes(fp.read(2),byteorder='little'))
#             fp.seek(4,1)
#             halfBin += bin(int.from_bytes(fp.read(2),byteorder='little'))
#             self.firstCluster = int(halfBin,2)
#             #fp.seek(16,1)
#             self.size = int.from_bytes(fp.read(4),byteorder='little')
#read entry chinh
# class Entry:
#     def __init__(self) -> None:
#         self.name = ""
#         self.attr = 0
#         self.createTime = 0
#         self.createDate = 0
#         self.size = 0
#     def ReadMainEntry(self, address):
#             with open(drive, 'rb') as fp:
#                 #seek(1,0) -> ten chinh
#                 #read tung byte
#                 fp.seek(address)
#                 if(self.name == ""):
#                     for i in range(8):
#                         eachName  = int.from_bytes(fp.read(1), byteorder='little')
#                         self.name += chr(self.eachName)
#                     #read(3) -> ten phu
#                     self.name += "."
#                     for i in range(3):
#                         eachName  = int.from_bytes(fp.read(1), byteorder='little')
#                         self.name += chr(self.eachName)
#                 #read(1) -> attribute
#                 bi = bin(int.from_bytes(fp.read(1), byteorder = 'little'))
#                 for i in range(8):
#                     if bi[i] == '1':
#                         if i==2:
#                             self.attr = "Archive"
#                         elif i==3:
#                             self.attr = "Directory"
#                         elif i==4:
#                             self.attr = "Volume Label"
#                         elif i==5:
#                             self.attr = "System File"
#                         elif i == 6:
#                             self.attr = "Hidden File"
#                         elif i==7:
#                             self.attr = "Read Only"
#                 #seek(1) -> seek 1
#                 fp.seek(1,1)
#                 #read(1) -> create time
#                 time = bin(int.from_bytes(fp.read(3),'little'))
#                 self.createTime = time[0:5] + ":" + time[5:11] + ":" + time[11:16]
#                 #read(4) -> create date time
#                 date = bin(int.from_bytes(fp.read(4),'little'))
#                 self.createDate = date[0:7] + "/" + date[7:11] + "/" + date[11:16]
#                 #seek(10)
#                 fp.seek(10,1)
#                 #read(4) -> size
#                 self.size = int.from_bytes(fp.read(4),byteorder='little')
#     #read entry phu
#     def ReadExtraEntry(self, address):
#         with open(drive, 'rb') as fp:
#             #seek(1)
#             fp.seek(address)
#             fp.seek(1,1)
#             #read(10) -> 5 ky tu cua ten file utf-16
#             for i in range(5):
#                 eachName  = int.from_bytes(fp.read(2), byteorder='little')
#                 self.name += chr(self.eachName)
#             #seek(3)
#             fp.seek(3,1)
#             #read(12)-> 6 ky tu ten file
#             for i in range(6):
#                 eachName  = int.from_bytes(fp.read(2), byteorder='little')
#                 self.name += chr(self.eachName)
#             #seek(2)
#             fp.seek(2,1)
#             #read(4) -> 2 ky tu ten file
#             for i in range(2):
#                 eachName  = int.from_bytes(fp.read(2), byteorder='little')
#                 self.name += chr(self.eachName)

class RDET:
    def __init__(self) -> None:
        self.name = ""
        self.attr = 0
        self.attr_Bin = 0
        self.createTime = 0
        self.createDate = 0
        self.size = 0
    def ReadMainEntry(self, address, drive, fp):
                #seek(1,0) -> ten chinh
                #read tung byte
                fp.seek(address,0)
                if(self.name == ""):
                    for i in range(8):
                        eachName  = int.from_bytes(fp.read(1), byteorder='little')
                        self.name += chr(eachName)
                    #read(3) -> ten phu
                    self.name += "."
                    for i in range(3):
                        eachName  = int.from_bytes(fp.read(1), byteorder='little')
                        self.name += chr(eachName)
                #read(1) -> attribute
                getbinary = lambda x, n: format(x, 'b').zfill(n)
                self.attr_Bin = getbinary(int.from_bytes(fp.read(1), byteorder = 'little'),8)
                bi = self.attr_Bin
                for i in range(len(bi)):
                    if bi[i] == '1':
                        if i==2:
                            self.attr = "Archive"
                        elif i==3:
                            self.attr = "Directory"
                        elif i==4:
                            self.attr = "Volume Label"
                        elif i==5:
                            self.attr = "System File"
                        elif i == 6:
                            self.attr = "Hidden File"
                        elif i==7:
                            self.attr = "Read Only"
                #seek(1) -> seek 1
                #read(1) -> create time
                fp.seek(1,1)
                time = getbinary((int.from_bytes(fp.read(3),'little')), 24)
                self.createTime = time[0:5] + ":" + time[5:11] + ":" + time[11:16]
                #read(4) -> create date time
                date = getbinary((int.from_bytes(fp.read(2),'little')), 16)
                self.createDate = date[0:7] + "/" + date[7:11] + "/" + date[11:16]
                #seek(10)
                fp.seek(10,1)
                #read(4) -> size
                self.size = int.from_bytes(fp.read(4),byteorder='little')
    #read entry phu
    def ReadExtraEntry(self, address, drive, fp):
            #seek(1)
            fp.seek(address,0)
            fp.seek(1,1)
            #read(10) -> 5 ky tu cua ten file utf-16
            for i in range(5):
                eachName  = int.from_bytes(fp.read(2), byteorder='little')
                self.name += chr(eachName)
            #seek(3)
            fp.seek(3,1)
            #read(12)-> 6 ky tu ten file
            for i in range(6):
                eachName  = int.from_bytes(fp.read(2), byteorder='little')
                self.name += chr(eachName)
            #seek(2)
            fp.seek(2,1)
            #read(4) -> 2 ky tu ten file
            for i in range(2):
                eachName  = int.from_bytes(fp.read(2), byteorder='little')
                self.name += chr(eachName)
                
    def PrintRDET(self):
        print("Name: ", self.name)
        # print("Bit Pattern of Attribute: ", self.attr_Bin)
        print("Attribute: ", self.attr)
        print("Create Time: ", self.createTime)
        print("Create Date: ", self.createDate)
        print("Size: ", self.size)
        
        print('\n')
        
    def setNull(self):
        self.name = ""
        self.attr = 0
        self.attr_Bin = 0
        self.createTime = 0
        self.createDate = 0
        self.size = 0
        
    def ReadRDET(self,address, drive):
        # B1: Offset xxxB (1 byte): kiểm tra xem là entry chính hay phụ từ RDET_address (byte)
        # seek(RDET_address,0) -> pointer dau bang
        # seek(11,1)
        with open (drive, 'rb') as fp:
            while True:
                
                fp.seek(address,0)
                fp.read(11)
                first_Byte_Main_Entry = int.from_bytes(fp.read(1), byteorder='little')
                
                if first_Byte_Main_Entry == 0: break
                
                if  first_Byte_Main_Entry == 0x0F:
                    self.ReadExtraEntry(address, drive, fp)
                else:
                    self.ReadMainEntry(address, drive, fp)
                    
                address += 32
                
                self.PrintRDET()
                self.setNull()
    # def PrintRDET(self):
    #     print("Name: ", self.name)
    #     # print("Bit Pattern of Attribute: ", self.attr_Bin)
    #     print("Attribute: ", self.attr)
    #     print("Create Time: ", self.createTime)
    #     print("Create Date: ", self.createDate)
    #     print("Size: ", self.size)
            # Đọc entry phụ từ dưới lên trên
            # Đọc entry chính
            # B2: Offset xxx0 (1 byte) - byte đầu tiên: kiểm tra trạng thái của entry
            # seek(1,0)
    # def ReadMainEntry(self, address):
    #         with open(drive, 'rb') as fp:
    #             #seek(1,0) -> ten chinh
    #             #read tung byte
    #             fp.seek(address)
    #             for i in range(8):
    #                 eachName  = int.from_bytes(fp.read(1), byteorder='little')
    #                 self.name += chr(self.eachName)
    #             #read(3) -> ten phu
    #             self.name += "."
    #             for i in range(3):
    #                 eachName  = int.from_bytes(fp.read(1), byteorder='little')
    #                 self.name += chr(self.eachName)
    #             #read(1) -> attribute
    #             bi = bin(int.from_bytes(fp.read(1), byteorder = 'little'))
    #             for i in range(8):
    #                 if bi[i] == '1':
    #                     if i==2:
    #                         self.attr = "Archive"
    #                     elif i==3:
    #                         self.attr = "Directory"
    #                     elif i==4:
    #                         self.attr = "Volume Label"
    #                     elif i==5:
    #                         self.attr = "System File"
    #                     elif i == 6:
    #                         self.attr = "Hidden File"
    #                     elif i==7:
    #                         self.attr = "Read Only"
    #             #seek(1) -> seek 1
    #             fp.seek(1,1)
    #             #read(1) -> create time
    #             time = bin(int.from_bytes(fp.read(3),'little'))
    #             self.createTime = time[0:5] + ":" + time[5:11] + ":" + time[11:16]
    #             #read(4) -> create date time
    #             date = bin(int.from_bytes(fp.read(4),'little'))
    #             self.createDate = date[0:7] + "/" + date[7:11] + "/" + date[11:16]
    #             #seek(10)
    #             fp.seek(10,1)
    #             #read(4) -> size
    #             self.size = int.from_bytes(fp.read(4),byteorder='little')
    # #read entry phu
    # def ReadExtraEntry(self, address):
    #     with open(drive, 'rb') as fp:
    #         #seek(1)
    #         fp.seek(address)
    #         fp.seek(1,1)
    #         #read(10) -> 5 ky tu cua ten file utf-16
    #         for i in range(5):
    #             eachName  = int.from_bytes(fp.read(2), byteorder='little')
    #             self.name += chr(self.eachName)
    #         #seek(3)
    #         fp.seek(3,1)
    #         #read(12)-> 6 ky tu ten file
    #         for i in range(6):
    #             eachName  = int.from_bytes(fp.read(2), byteorder='little')
    #             self.name += chr(self.eachName)
    #         #seek(2)
    #         fp.seek(2,1)
    #         #read(4) -> 2 ky tu ten file
    #         for i in range(2):
    #             eachName  = int.from_bytes(fp.read(2), byteorder='little')
    #             self.name += chr(self.eachName)

