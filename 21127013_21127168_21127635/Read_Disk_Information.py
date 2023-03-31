import os
import string
import Data

import NTFS

"""FAT32"""
def ReadInfoFromBootSector(drive):
    BOOT = Data.BootSectorFAT32()
    BOOT.ReadBootSector(drive) # Read Boot Sector
    return BOOT

def ReadInfoRDET(drive, BOOT, FirstClusterDATA):
    
    # Read Root Directory Entry Table
    RDET = Data.RDET()
    res = RDET.ReadRDET(FirstClusterDATA, drive)
    
    """ Read all directory in RDET """
    for x in RDET.RootEntry.ListEntry:
        
        # 1 Of Entry in RDET contain the information of the disk, so we need to get it
        str = x.name.split('\x00')[0]
        if (str == 'System Volume Information'): 
            RDET.RootEntry.attr = x.attr
            RDET.RootEntry.createDate = x.createDate
            RDET.RootEntry.createTime = x.createTime
            
        # Besides, We still continute to the full Information of Each Entry in Root Directory Entry Table
        ReadAllDirectory_FromRDET(x, FirstClusterDATA, BOOT, drive)
        
    return RDET # Return Value

def ReadAllDirectory_FromRDET(Entry, FirstClusterDATA, bootSector, drive, depth = 0):
    if depth >= 10: return None # The Depth can be adjusted to fit the requirement
    
    # Goal: Read data in the Directory Entry
    # We just use Recursive to go further in the DataZone If only the Entry is a Regular Directory with no extra attributes
    if Entry.attr[3] == 'DIRECTORY' and Entry.attr[4] == 'NULL' and Entry.attr[5] == 'NULL' and Entry.attr[6] == 'NULL' and Entry.attr[7] == 'NULL': 
        
        # Locate the Cluster contain the chosen Entry data
        EntryInsideDir_Address = (Entry.startCluster - 2 ) * bootSector.sectorPerCluster * bootSector.bytePerSector + FirstClusterDATA
        Entry.ReadDET(EntryInsideDir_Address, drive) # Read it
        
        for x in Entry.ListEntry:
            if x.attr[3] == 'DIRECTORY' and x.attr[4] == 'NULL' and x.attr[5] == 'NULL' and x.attr[6] == 'NULL' and x.attr[7] == 'NULL':       
                    ReadAllDirectory_FromRDET(x, FirstClusterDATA, bootSector, drive, depth + 1)
                
    return None

def Load_FAT_DATA(Entry, isROOT = False):
    
    path = [] # List of Children
    
    if isROOT == True: # If the Entry is the Root Directory, we load all info of it even it is a hidden file or system file
        for x in Entry.ListEntry:
            res =Load_FAT_DATA(x)
            if res != '': #If the Entry is not a hidden file or system file, we load it
                path.append(res) 
                
        dict_path = {} # Dictionary of the Entry, Help located the data easier with calling the key
        dict_path["Name"] = Entry.name
        
        str = ''
        for i in range(len(Entry.attr)): 
            if Entry.attr[i] != "NULL" and i != 4 and i != 5 and i != 6: # Only load the attribute that is not Hidden File or System File
                if str != '': str += ',' + Entry.attr[i]
                else: str += Entry.attr[i]
        
        dict_path["Attribute"] = str
        dict_path["Date_Created"] = Entry.createDate
        dict_path["Time_Created"] = Entry.createTime
        dict_path["Size"] = Entry.size
        dict_path["Children"] = path
        dict_path["Type"] = "FAT32"
        
    else:
        if Entry.attr[3] == 'DIRECTORY' and Entry.attr[4] == 'NULL' and Entry.attr[5] == 'NULL' and Entry.attr[6] == 'NULL' and Entry.attr[7] == 'NULL' :
            
            for x in Entry.ListEntry:
                res =Load_FAT_DATA(x)
                if res != '': # If the Entry is not a hidden file or system file, we load it
                    path.append(res) 
                    
            dict_path = {} #Dictionary of the Entry, Help located the data easier with calling the key
            dict_path["Name"] = Entry.name
            
            str = ''
            for i in range(len(Entry.attr)): 
                if Entry.attr[i] != "NULL": #Only load the attribute that is not Hidden File or System File
                    if str != '': str += ',' + Entry.attr[i]
                    else: str += Entry.attr[i]
            
            dict_path["Attribute"] = str
            dict_path["Date_Created"] = Entry.createDate
            dict_path["Time_Created"] = Entry.createTime
            dict_path["Size"] = Entry.size
            dict_path["Children"] = path
            dict_path["Type"] = "FOLDER"
            
        elif Entry.attr[4] == 'VOLUME LABEL' or Entry.attr[5] == 'SYSTEM FILE' or Entry.attr[6] == 'HIDDEN FILE': #If the Entry is a Hidden File or System File
                return ''
        else: #If the Entry is a File
            dict_path = {} #Dictionary of the Entry, Help located the data easier with calling the key
            dict_path["Name"] = Entry.name
            
            str = ''
            for i in range(len(Entry.attr)): 
                if Entry.attr[i] != "NULL": #Only load the attribute that is not Hidden File or System File
                    if str != '': str += ',' + Entry.attr[i]
                    else: str += Entry.attr[i]
            
            dict_path["Attribute"] = str
            dict_path["Size"] = Entry.size
            dict_path["Date_Created"] = Entry.createDate
            dict_path["Time_Created"] = Entry.createTime
            dict_path["Size"] = Entry.size
            TypeofFile = Entry.name.split('.')[-1]
            dict_path["Type"] = TypeofFile + " FILE"
            
            return dict_path
        
    return dict_path

def Push_To_GUI(Entry, TypePartition, file_path):
    
    if TypePartition == 'FAT32':
        file_path.append(Load_FAT_DATA(Entry,True))
    else:
        file_path.append(Load_NTFS_DATA(Entry,True))
    

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

def Load_NTFS_DATA(Entry, isROOT = False):
    
    path = [] #List of Children
    NTFS_CreateTime = "" #Create Time of the Entry
    Check_Is_Folder = False #Check if the Entry is a Folder
    
    for j in range(len(Entry.attributes)): #Scan all the attribute of the Entry
        if(Entry.attributes[j].typeHeader == 'STANDARD_INFORMATION' ): 
            NTFS_CreateTime = Entry.attributes[j].content.standard_information.create_time
            
        if(Entry.attributes[j].typeHeader == 'FILE_NAME'):#If the attribute contain important information about the Entry
            if(Entry.attributes[j].content.file_name.attr[1] != "NULL" or Entry.attributes[j].content.file_name.attr[2] != "NULL"):
                if(isROOT != True): return "" 
                
                dict_path = {} # Dictionary of the Entry, Help located the data easier with calling the key
                dict_path["Name"] = Entry.attributes[j].content.file_name.Name #Name of the Entry
                
                str = ''
                for x in range(len(Entry.attributes[j].content.file_name.attr)):
                    if Entry.attributes[j].content.file_name.attr[x] != "NULL" and x != 1 and x != 2: #Only load the attribute that is not Hidden File or System File
                        if str != '': str += ',' + Entry.attributes[j].content.file_name.attr[x]
                        else : str += Entry.attributes[j].content.file_name.attr[x]
                        
                dict_path["Attribute"] = str #Attribute of the Entry
                dict_path["Date_Created"] = NTFS_CreateTime.split(" ")[0] #Date of the Entry
                dict_path["Time_Created"] = NTFS_CreateTime.split(" ")[1] #Time of the Entry
                dict_path["Size"] = Entry.SizeofusedMFTE #Size of the Entry
                dict_path["Type"] = "NTFS"
                Check_Is_Folder = True
                                
            else: 
                dict_path = {} # Dictionary of the Entry, Help located the data easier with calling the key
                dict_path["Name"] = Entry.attributes[j].content.file_name.Name #Name of the Entry
                
                str = '' #Attribute of the Entry
                for x in range(len(Entry.attributes[j].content.file_name.attr)):
                    if Entry.attributes[j].content.file_name.attr[x] != "NULL": #Only load the attribute that is not Hidden File or System File
                        if str != '': str += ',' + Entry.attributes[j].content.file_name.attr[x]
                        else : str += Entry.attributes[j].content.file_name.attr[x]
                        
                dict_path["Attribute"] = str #Attribute of the Entry
                dict_path["Date_Created"] = NTFS_CreateTime.split(" ")[0] #Date of the Entry
                dict_path["Time_Created"] = NTFS_CreateTime.split(" ")[1] #Time of the Entry
                dict_path["Size"] = Entry.SizeofusedMFTE #Size of the Entry
                
                if Entry.attributes[j].content.file_name.attr[4] != "NULL": 
                    Check_Is_Folder = True #Check if the Entry is a Folder
                    dict_path["Type"] = "FOLDER"
                else: dict_path["Type"] = "FILE"
            break
    
    
    for x in Entry.listEntry:
        res = Load_NTFS_DATA(x)
        if res != '': #If data is not empty
            path.append(res)
            
    if len(path) == 0: path = ""   
    if Check_Is_Folder == True: #If the Entry is a Folder
        dict_path["Children"] = path
    
    return dict_path

def Get_InFo_From_All_Disk():
    
    """ Detect all drive """
    drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

    """ File Path"""
    file_path = []

    """ Drive Path """
    for d in drives: # LOOP Through All Available Drive
        
        drive = r"\\.\{}".format(d) # Format The Name That Will Be Used To Open The Drive
    
        """ Boot Sector """
        BOOT = ReadInfoFromBootSector(drive)
        
        if BOOT.FATtype.split(" ")[0] == 'FAT32': 
            
            """ Address of FAT1, FAT2, DATA, RDET (Including Data part) """
            FAT1_Address = BOOT.sectorBeforeFAT * BOOT.bytePerSector
            FAT2_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT) * BOOT.bytePerSector   
            FirstCluster_Data_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT * 2) * BOOT.bytePerSector
            RDET_Address = (BOOT.firstClusterinRDET- 2 ) * BOOT.sectorPerCluster * BOOT.bytePerSector + FirstCluster_Data_Address
            
            """ RDET """
            RDET = ReadInfoRDET(drive, BOOT, RDET_Address)
            
            """ Print Directory Tree """
            RDET.RootEntry.name = drive[4:]
            
            #Directory Tree Gui
            Push_To_GUI(RDET.RootEntry, "FAT32", file_path)

        else: 
            if drive[4:] == 'C:' : continue
            with open (drive,'rb') as fp:
                NTFS_BOOT = NTFS.VBR()
                NTFS_BOOT.ReadVBR(drive,fp)
                #NTFS_BOOT.PrintVBR()
                
                MFTAddress = NTFS_BOOT.FirstClusterInMFT * NTFS_BOOT.BytesPerSector * NTFS_BOOT.SectorPerCluster
                MFT = NTFS.MFT()
                MFT.ReadMFT(drive,fp,MFTAddress,NTFS_BOOT.BytesPerSector*NTFS_BOOT.SectorPerCluster)
                #MFT.PrintMFT()
                
            LocatedRoot(MFT)
            
            for i in range(len(MFT.MFT)):
                if (MFT.MFT[i].isROOT == True):
                    Push_To_GUI(MFT.MFT[i], "NTFS", file_path)
                    break

    """ Display GUI"""
    y = 1
    return file_path
