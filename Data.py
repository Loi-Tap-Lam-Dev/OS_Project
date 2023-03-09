class BootSectorFAT32:
    def __init__(self) -> None:
        self.bytePerSector = 0
        self.sectorPerCluster = 0
        self.sectorBeforeFAT = 0
        self.cntFAT = 0
        self.sizeVol = 0
        self.sectorPerFAT = 0
        self.firstClusterinRDET = 0
        self.FATtype = 0
    def ReadBootSector(self, drive):
        with open(drive, 'rb') as fp:
            fp.seek(0)
            self.bytePerSector = int.from_bytes(fp.read(2), byteorder='little')
            self.sectorPerCluster = int.from_bytes(fp.read(1), byteorder='little')
            self.sectorBeforeFAT = int.from_bytes(fp.read(2), byteorder='little')
            self.cntFAT = int.from_bytes(fp.read(1), byteorder='little')
            self.sizeVol = int.from_bytes(fp.read(4), byteorder='little')
            self.sectorPerFAT = int.from_bytes(fp.read(4), byteorder='little')
            self.firstClusterinRDET = int.from_bytes(fp.read(4), byteorder='little')
            self.FATtype = int.from_bytes(fp.read(1), byteorder='little')
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

class RDET:
    def __init__(self,name,attr,reserved,createTime,createDate,lastAccessDate,firstCluster,lastWriteTime,lastWriteDate,size):
        self.name = name
        self.attr = attr
        self.reserved = reserved
        self.createTime = createTime
        self.createDate = createDate
        self.lastAccessDate = lastAccessDate
        self.firstCluster = firstCluster
        self.lastWriteTime = lastWriteTime
        self.lastWriteDate = lastWriteDate
        self.size = size
        
    
