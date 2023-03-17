import os
import Data1
import Data

def main():
    
    """ Drive Path """
    drive = r"\\.\D:" 
    
    """ Boot Sector """
    print ("Reading boot sector FAT32...")
    BOOT = Data.BootSectorFAT32()
    res = BOOT.ReadBootSector(drive) # Read Boot Sector
    print(BOOT.PrintBootSector())
    
    """ Address of FAT1, FAT2, RDET (Including Data part) """
    FAT1_Address = BOOT.sectorBeforeFAT * BOOT.bytePerSector
    FAT2_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT) * BOOT.bytePerSector    
    RDET_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT * 2) * BOOT.bytePerSector
    
    # print(FAT1_Address)
    # print(FAT2_Address)
    # print(RDET_Address)
    
    """ RDET """
    print("Reading RDET FAT32... ")
    RDET = Data.RDET()
    res = RDET.ReadRDET(RDET_Address, drive)
    RDET.PrintRDET()
    
    x = RDET.RootEntry.ListEntry[5] # Access to the 3rd entry in the RDET
    x.PrintAttribute()
    EntryInsideDir_Address = (x.startCluster - 2 ) * BOOT.sectorPerCluster * BOOT.bytePerSector + RDET_Address
    print("EntryInsideDir_Address: ", EntryInsideDir_Address)
    x.ReadDET(EntryInsideDir_Address, drive)
    
    for i  in x.ListEntry:
            i.PrintAttribute()
main()