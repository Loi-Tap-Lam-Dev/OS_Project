import Data
import os

def main():
    drive = r"\\.\D:"
    print ("Reading boot sector...")
    BOOT = Data.BootSectorFAT32()
    res = BOOT.ReadBootSector(drive)
    BOOT.PrintBootSector()
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