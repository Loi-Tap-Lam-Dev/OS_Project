import Data
import Test_readingSector

def main():
    drive = 3
    BOOT  = Data.BootSectorFAT32()
    #file = Test_readingSector.read_sector(drive)
    BOOT.ReadBootSector(r"\\.\D:")
    # if(res != 0):
    #     print("Error: ", res)
    #     return
    print ("Reading disk parameters...")
    print ("Bytes per sector: ", BOOT.bytePerSector)
    print ("Sectors per cluster: ", BOOT.sectorPerCluster)
    print ("Sectors before FAT: ", BOOT.sectorBeforeFAT)
    print ("Number of FATs: ", BOOT.cntFAT)
    print ("Size of volume: ", BOOT.sizeVol)
    print ("Sectors per FAT: ", BOOT.sectorPerFAT)
    print ("First cluster in RDET: ", BOOT.firstClusterinRDET)
    print ("FAT type: ", BOOT.FATtype)
    print ("Reading root directory entries...")
    # RDET = Data.RDET()
    # res = absread(drive, BOOT.firstClusterinRDET, 1, RDET)
    # if(res != 0):
    #     print("Error: ", res)
    #     return
    # print ("Name: ", RDET.name)
    # print ("Attribute: ", RDET.attr)
    # print ("Reserved: ", RDET.reserved)
    # print ("Create time: ", RDET.createTime)
    # print ("Create date: ", RDET.createDate)
    # print ("Last access date: ", RDET.lastAccessDate)
    # print ("First cluster: ", RDET.firstCluster)
    # print ("Last write time: ", RDET.lastWriteTime)
    # print ("Last write date: ", RDET.lastWriteDate)
    # print ("Size: ", RDET.size)
    # print ("Reading file...")
    # file = Data.File()
    # res = absread(drive, RDET.firstCluster, 1, file)
    # if(res != 0):
    #     print("Error: ", res)
    #     return
    # print ("File content: ", file.content)
    # print ("Done!")
    
    
