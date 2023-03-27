import os
import string
import Data

def ReadInfoFromBootSector(drive):
    BOOT = Data.BootSectorFAT32()
    BOOT.ReadBootSector(drive) # Read Boot Sector
    return BOOT

def ReadInfoRDET(drive, BOOT, RDET_Address):
    #print("Reading RDET FAT32... ")
    RDET = Data.RDET()
    res = RDET.ReadRDET(RDET_Address, drive)
    
    #RDET.PrintRDET()
    
    """ Read all directory in RDET """
    for x in RDET.RootEntry.ListEntry:
        ReadAllDirectory_FromRDET(x, RDET_Address, BOOT, drive)
        
    return RDET

def ReadAllDirectory_FromRDET(Entry, RDET_Address, bootSector, drive, depth = 0):
    if depth >= 10: return None
    if Entry.attr[3] == 'Directory' and Entry.attr[4] == 'NULL' and Entry.attr[5] == 'NULL' and Entry.attr[6] == 'NULL' and Entry.attr[7] == 'NULL': 
        EntryInsideDir_Address = (Entry.startCluster - 2 ) * bootSector.sectorPerCluster * bootSector.bytePerSector + RDET_Address
        Entry.ReadDET(EntryInsideDir_Address, drive)
        for x in Entry.ListEntry:
            if x.attr[3] == 'Directory' and x.attr[4] == 'NULL' and x.attr[5] == 'NULL' and x.attr[6] == 'NULL' and x.attr[7] == 'NULL':       
                    ReadAllDirectory_FromRDET(x, RDET_Address, bootSector, drive, depth + 1)
                
    return None

def Print_Directory_Tree(Entry,i):
    y = 1
    for x in Entry.ListEntry:
        if x.attr[3] == 'Directory' and x.attr[4] == 'NULL' and x.attr[5] == 'NULL' and x.attr[6] == 'NULL' and x.attr[7] == 'NULL':
            print(' ' * (i + 1),'|','-'*4,x.name,'\n')
            for y in x.ListEntry:
                print(' ' * (i + 6),'|','-'*4,y.name,'\n')
                Print_Directory_Tree(y, i + 8 + 4)
        else:
            print(' ' * (i + 1),'|','-'*4,x.name,'\n')
    return None

def Print_Directory_Tree_v2(Entry,i, str, depth = 0):
    y = 1
    if depth > 6: return None
    
    #print(str + Entry.name, [i for i in Entry.attr if i != "NULL"],'\n')
    print(str + Entry.name, '\n')
    
    if Entry.attr[3] == 'Directory' and Entry.attr[4] == 'NULL' and Entry.attr[5] == 'NULL' and Entry.attr[6] == 'NULL' and Entry.attr[7] == 'NULL':
        for x in Entry.ListEntry:
            str = ' ' * i 
            Print_Directory_Tree_v2(x, i + 5, str + '|' + '-' * 4, depth + 1)
    
    return None

def main():
    """ Detect all drive """
    drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

    """ Drive Path """
    for d in drives:
        
        drive = r"\\.\{}".format(d)
    
        """ Boot Sector """
        BOOT = ReadInfoFromBootSector(drive)
        
        if BOOT.FATtype.split(" ")[0] != 'FAT32': continue
        #print ("Reading boot sector FAT32...")
        
        """ Address of FAT1, FAT2, RDET (Including Data part) """
        FAT1_Address = BOOT.sectorBeforeFAT * BOOT.bytePerSector
        FAT2_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT) * BOOT.bytePerSector    
        RDET_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT * 2) * BOOT.bytePerSector
        
        """ RDET """
        RDET = ReadInfoRDET(drive, BOOT, RDET_Address)
        
        """ Print Directory Tree """
        i = 0
        RDET.RootEntry.name = drive[4:]
        RDET.RootEntry.attr[3] = 'Directory'
        print("Directory Tree: \n")
        Print_Directory_Tree_v2(RDET.RootEntry, i, "") #Print

main()