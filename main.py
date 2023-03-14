import os
import Data1
import Data


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
    
    RDET = Data.RDET()
    # 1 entry = 32 bytes
    res1 = RDET.ReadRDET(RDET_Address,drive)
    RDET.PrintRDET()
    
    
main()