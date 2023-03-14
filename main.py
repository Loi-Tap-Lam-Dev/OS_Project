import os
import Data


def main():
    drive = r"\\.\D:"
    # with open(drive, 'rb') as fp:
    #     fp.read(446)
    #     for i in range(int(512 / 16)):
    #         print (hex(int.from_bytes(fp.read(1), byteorder = 'big')))
    print ("Reading master boot sector...")
    BOOT = Data.BootSectorFAT32()
    res = BOOT.ReadBootSector(drive)
    BOOT.PrintBootSector()
    # BOOT = Data.MBR()
    # res = BOOT.readMBR(drive)
    # BOOT.PrintMBR()
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