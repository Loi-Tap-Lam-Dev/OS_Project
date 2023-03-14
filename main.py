import os
import Data

def main():
    drive = r"\\.\D:"

    print ("Reading boot sector FAT32...")
    BOOT = Data.BootSectorFAT32()
    res = BOOT.ReadBootSector(drive)
    print(BOOT.PrintBootSector())
    FAT1_Address = BOOT.sectorBeforeFAT * BOOT.bytePerSector
    FAT2_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT) * BOOT.bytePerSector
    RDET_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT * 2) * BOOT.bytePerSector
    print(FAT1_Address)
    print(FAT2_Address)
    print(RDET_Address)
    print("Reading RDET FAT32... ")
    RDET = Data.RDET()
    res = RDET.ReadRDET(RDET_Address, drive)
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
    
main()