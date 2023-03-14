import os
import Data1


def main():
    drive = r"\\.\D:"
    
    print ("Reading boot sector FAT32...")
    BOOT = Data1.BootSectorFAT32()
    res = BOOT.ReadBootSector(drive)
    BOOT.PrintBootSector()
    
    FAT1_Address = BOOT.sectorBeforeFAT * BOOT.bytePerSector
    # print(hex(FAT1_Address))
    FAT2_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT) * BOOT.bytePerSector
    # print(hex(FAT2_Address))
    RDET_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT * 2) * BOOT.bytePerSector
    #print(hex(RDET_Address))
    print ("\n")
    
    RDET = Data1.RDET()
    # 1 entry = 32 bytes
    res1 = RDET.ReadRDET(RDET_Address,drive)
    RDET.PrintRDET()
    
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