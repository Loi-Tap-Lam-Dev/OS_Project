import os
import string
import Data
import Layer
import NTFS

"""FAT32"""
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
        y = 1
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

def Print_Directory_Tree_v3(Entry,i, str, depth = 0):
    
    path = []
    if depth > 6: return None
    
    #print(str + Entry.name, [i for i in Entry.attr if i != "NULL"],'\n')    
    if Entry.attr[3] == 'Directory' and Entry.attr[4] == 'NULL' and Entry.attr[5] == 'NULL' and Entry.attr[6] == 'NULL' and Entry.attr[7] == 'NULL':
        
        for x in Entry.ListEntry:
            str = ' ' * i 
            res = Print_Directory_Tree_v3(x, i + 5, str + '|' + '-' * 4, depth + 1)
            if res != '':
                path.append(res)
                
        dict_path = {}
        dict_path["Name"] = Entry.name
        
        str = ''
        for i in range(len(Entry.attr)): 
            if Entry.attr[i] != "NULL": str += Entry.attr[i] + ','
        
        dict_path["Attribute"] = str
        dict_path["Size"] = Entry.size
        dict_path["Date_Created"] = Entry.createDate
        dict_path["Time_Created"] = Entry.createTime
        dict_path["Size"] = Entry.size
        dict_path["Children"] = path
        
    elif Entry.attr[4] == 'Volume Label' or Entry.attr[5] == 'System File' or Entry.attr[6] == 'Hidden File':
            return ''
    else: 
        dict_path = {}
        dict_path["Name"] = Entry.name
        
        str = ''
        for i in range(len(Entry.attr)):
            if Entry.attr[i] != "NULL": str += Entry.attr[i] + ','
        
        dict_path["Attribute"] = str
        dict_path["Size"] = Entry.size
        dict_path["Date_Created"] = Entry.createDate
        dict_path["Time_Created"] = Entry.createTime
        dict_path["Size"] = Entry.size
        
        return dict_path
    
    return dict_path

def GUI(Entry, i, str, depth = 0):
    file_path = []
    file_path.append(Print_Directory_Tree_v3(Entry, i, str))
    y = 1
    return file_path

"""NTFS"""
def LocatedRoot(MFT):

    for i in range(len(MFT.MFT)):
        if (MFT.MFT[i].isROOT == False):
            for j in range(len(MFT.MFT[i].attributes)):
                attr = MFT.MFT[i].attributes[j]
                if(attr.typeHeader == 'FILE_NAME'):
                    IdParent = attr.content.file_name.IdRootParentDirectory
                    MFT.Dictionary[IdParent].listEntry.append(MFT.MFT[i])
                
def CheckIsFolder(MFT):
    for i in range(len(MFT.MFT)):
        if (MFT.MFT[i].isROOT == False and MFT.MFT[i].listEntry != []):
            for j in range(len(MFT.MFT[i].attributes)):
                    if(MFT.MFT[i].attributes[j].typeHeader == 'FILE_NAME'):
                        if(MFT.MFT[i].attributes[j].content.file_name.attr[1] == "NULL" and MFT.MFT[i].attributes[j].content.file_name.attr[2] == "NULL"):
                                print(MFT.MFT[i].attributes[j].content.file_name.Name)

def PrintDirectory(Entry, i, str, isROOT = False):
    y = 1
    for j in range(len(Entry.attributes)):
        if(Entry.attributes[j].typeHeader == 'FILE_NAME'):
            if(Entry.attributes[j].content.file_name.attr[1] != "NULL" or Entry.attributes[j].content.file_name.attr[2] != "NULL"):
                if(isROOT != True): return None
                break
            else: 
                print(str + Entry.attributes[j].content.file_name.Name, '\n')
            break
    
    for x in Entry.listEntry:
        str = " " * i
        PrintDirectory(x, i + 5, str + '|' + '----')
    
    return None

def PrintDirectory_v2(Entry, i, str, isROOT = False):
    y = 1
    for j in range(len(Entry.attributes)):
        if(Entry.attributes[j].typeHeader == 'FILE_NAME'):
            if(Entry.attributes[j].content.file_name.attr[1] != "NULL" or Entry.attributes[j].content.file_name.attr[2] != "NULL"):
                if(isROOT != True): return None
                break
            else: 
                print(str + Entry.attributes[j].content.file_name.Name, '\n')
            break
    
    for x in Entry.listEntry:
        str = " " * i
        PrintDirectory(x, i + 5, str + '|' + '----')
    
    return None

def main():
    """ Detect all drive """
    drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

    """ Drive Path """
    for d in drives:
        
        drive = r"\\.\{}".format(d)
    
        """ Boot Sector """
        BOOT = ReadInfoFromBootSector(drive)
        
        if BOOT.FATtype.split(" ")[0] == 'FAT32': 
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
            #print("Directory Tree: \n")
            #Print_Directory_Tree_v2(RDET.RootEntry, i, "") #Print
            
            #Directory Tree Gui
            file_path = GUI(RDET.RootEntry, i, "")
            Layer.Display(file_path)
            
        else: 
            if drive[4:] == 'C:': continue
            with open (drive,'rb') as fp:
                NTFS_BOOT = NTFS.VBR()
                NTFS_BOOT.ReadVBR(drive,fp)
                #NTFS_BOOT.PrintVBR()
                #print("-----------------------")
                MFTAddress = NTFS_BOOT.FirstClusterInMFT * NTFS_BOOT.BytesPerSector * NTFS_BOOT.SectorPerCluster
                MFT = NTFS.MFT()
                MFT.ReadMFT(drive,fp,MFTAddress,NTFS_BOOT.BytesPerSector*NTFS_BOOT.SectorPerCluster)
                #MFT.PrintMFT()
                
            # print("-----------------------")    
            LocatedRoot(MFT)
            #CheckIsFolder(MFT)
            
            # for i in range(len(MFT.MFT)):
            #     if (MFT.MFT[i].isROOT == True):
            #         PrintDirectory(MFT.MFT[i],0,"", True)
            #         break

# def main1():
    
#     """ Drive Path """
#     drive = r"\\.\E:"
#     with open (drive,'rb') as fp:
#         BOOT = NTFS.VBR()
#         BOOT.ReadVBR(drive,fp)
#         BOOT.PrintVBR()
#         print("-----------------------")
#         MFTAddress = BOOT.FirstClusterInMFT * BOOT.BytesPerSector * BOOT.SectorPerCluster
#         MFT = NTFS.MFT()
#         MFT.ReadMFT(drive,fp,MFTAddress,BOOT.BytesPerSector*BOOT.SectorPerCluster)
#         #MFT.PrintMFT()
        
#     print("-----------------------")    
#     LocatedRoot(MFT)
#     CheckIsFolder(MFT)
    
#     for i in range(len(MFT.MFT)):
#         if (MFT.MFT[i].isROOT == True):
#             PrintDirectory(MFT.MFT[i],0,"", True)
#             break
#     #for i in range(len(MFT.MFT)):
        

main()