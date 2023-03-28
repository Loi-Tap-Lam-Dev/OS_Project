import os
import Data1
import Data
import NTFS

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


def main():
    
    """ Drive Path """
    drive = r"\\.\E:"
    with open (drive,'rb') as fp:
        BOOT = NTFS.VBR()
        BOOT.ReadVBR(drive,fp)
        BOOT.PrintVBR()
        print("-----------------------")
        MFTAddress = BOOT.FirstClusterInMFT * BOOT.BytesPerSector * BOOT.SectorPerCluster
        MFT = NTFS.MFT()
        MFT.ReadMFT(drive,fp,MFTAddress,BOOT.BytesPerSector*BOOT.SectorPerCluster)
        #MFT.PrintMFT()
        
    print("-----------------------")    
    LocatedRoot(MFT)
    CheckIsFolder(MFT)
    
    for i in range(len(MFT.MFT)):
        if (MFT.MFT[i].isROOT == True):
            PrintDirectory(MFT.MFT[i],0,"", True)
            break
    #for i in range(len(MFT.MFT)):
        

main()