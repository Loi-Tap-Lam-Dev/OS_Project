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
    #print("Reading RDET FAT32... ")
    RDET = Data.RDET()
    res = RDET.ReadRDET(RDET_Address, drive)
    RDET.PrintRDET()
    
    """ Read all directory in RDET """
    for x in RDET.RootEntry.ListEntry:
        ReadAllDirectory_FromRDET(x, RDET_Address, BOOT, drive)
        y = 1
    #     if x.attr[3] == 'Directory' and x.attr[4] == 'NULL' and x.attr[5] == 'NULL' and x.attr[6] == 'NULL' and x.attr[7] == 'NULL':
    #         EntryInsideDir_Address = (x.startCluster - 2 ) * BOOT.sectorPerCluster * BOOT.bytePerSector + RDET_Address
    #         x.ReadDET(EntryInsideDir_Address, drive)
            # print ("Directory: ", x.name, '\n')
            # for i  in x.ListEntry:
            #     i.PrintAttribute()
    
    """ Print Directory Tree """
    i = 0
    print(drive, '\n')
    Print_Directory_Tree(RDET.RootEntry, i)
    
    #print(drive, '\n')
    # for x in RDET.RootEntry.ListEntry:
    #     if x.attr[3] == 'Directory' and x.attr[4] == 'NULL' and x.attr[5] == 'NULL' and x.attr[6] == 'NULL' and x.attr[7] == 'NULL':
    #         print('|','-'*i,x.name,'\n')
    #         for y in x.ListEntry:
    #             print(' ',' '*i,'|','-'*i,y.name,'\n')
    #     else:
    #         print('|','-'*i,x.name,'\n')

def ReadAllDirectory_FromRDET(Entry, RDET_Address, bootSector, drive):
    if Entry.attr[3] == 'Directory' and Entry.attr[4] == 'NULL' and Entry.attr[5] == 'NULL' and Entry.attr[6] == 'NULL' and Entry.attr[7] == 'NULL': 
        EntryInsideDir_Address = (Entry.startCluster - 2 ) * bootSector.sectorPerCluster * bootSector.bytePerSector + RDET_Address
        Entry.ReadDET(EntryInsideDir_Address, drive)
        for x in Entry.ListEntry:
            if x.attr[3] == 'Directory' and x.attr[4] == 'NULL' and x.attr[5] == 'NULL' and x.attr[6] == 'NULL' and x.attr[7] == 'NULL':       
                    ReadAllDirectory_FromRDET(x, RDET_Address, bootSector, drive)
                
    return None

def Print_Directory_Tree(Entry,i):
    y = 1
    for x in Entry.ListEntry:
        if x.attr[3] == 'Directory' and x.attr[4] == 'NULL' and x.attr[5] == 'NULL' and x.attr[6] == 'NULL' and x.attr[7] == 'NULL':
            print(' ' * (i + 1),'|','-'*4,x.name,'\n')
            for y in x.ListEntry:
                print(' ' * (i + 6),'|','-'*4,y.name,'\n')
                Print_Directory_Tree(y, i + 8 + 4 )
        else:
            print(' ' * (i + 1),'|','-'*4,x.name,'\n')
    return None

main()