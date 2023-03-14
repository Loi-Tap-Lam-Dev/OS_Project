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
            self.cntFAT = int.from_bytes(fp.read(1), byteorder='little') # 0x11
            fp.seek(15,1)
            self.sizeVol = int.from_bytes(fp.read(4), byteorder='little')
            self.sectorPerFAT = int.from_bytes(fp.read(4), byteorder='little') #0x28
            fp.seek(4,1)
            self.firstClusterinRDET = int.from_bytes(fp.read(4), byteorder='little') #0x30
            fp.seek(34,1)
            #self.FATtypeEach = int.from_bytes(fp.read(8), byteorder='little')
            for i in range(8):
                self.FATtypeEach = int.from_bytes(fp.read(1), byteorder='little')
                self.FATtype += chr(self.FATtypeEach )
        return 0
    # def __init__(self, bytePerSector, sectorPerCluster, sectorBeforeFAT, cntFAT, sizeVol, sectorPerFAT, firstClusterinRDET, FATtype):
    #     self.bytePerSector=bytePerSector
    #     self.sectorPerCluster = sectorPerCluster
    #     self.sectorBeforeFAT = sectorBeforeFAT
    #     self.cntFAT = cntFAT
    #     self.sizeVol = sizeVol
    #     self.sectorPerFAT = sectorPerFAT
    #     self.firstClusterinRDET=firstClusterinRDET
    #     self.FATtype = FATtype
    # def ReadBootSectorNTFS(self, drive):
    #     with open(drive, 'rb') as fp:
    #         fp.seek(3)
    #         self.bytePerSector = int.from_bytes(fp.read(2), byteorder='little')
    #         self.sectorPerCluster = int.from_bytes(fp.read(1), byteorder='little')
    #         self.sectorBeforeFAT = int.from_bytes(fp.read(2), byteorder='little')
    #         self.cntFAT = int.from_bytes(fp.read(1), byteorder='little')
    #         self.sizeVol = int.from_bytes(fp.read(4), byteorder='little')
    #         self.sectorPerFAT = int.from_bytes(fp.read(4), byteorder='little')
    #         self.firstClusterinRDET = int.from_bytes(fp.read(4), byteorder='little')
    #         self.FATtype = int.from_bytes(fp.read(1), byteorder='little')
    #     return 0
    # def ReadBootSectork(self, file):
    #     file.seek(11)
    #     self.bytePerSector = int.from_bytes(file.read(2), byteorder='little')
    #     self.sectorPerCluster = int.from_bytes(file.read(1), byteorder='little')
    #     self.sectorBeforeFAT = int.from_bytes(file.read(2), byteorder='little')
    #     self.cntFAT = int.from_bytes(file.read(1), byteorder='little')
    #     self.sizeVol = int.from_bytes(file.read(4), byteorder='little')
    #     self.sectorPerFAT = int.from_bytes(file.read(4), byteorder='little')
    #     self.firstClusterinRDET = int.from_bytes(file.read(4), byteorder='little')
    #     self.FATtype = int.from_bytes(file.read(1), byteorder='little')
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

#class RDET:
    #def __init__(self) -> None:
        # self.name = name
        # self.attr = attr
        # self.reserved = reserved
        # self.createTime = createTime
        # self.createDate = createDate
        # self.lastAccessDate = lastAccessDate
        # self.firstCluster = firstCluster
        # self.lastWriteTime = lastWriteTime
        # self.lastWriteDate = lastWriteDate
        # self.size = size
        
    
