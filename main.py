import os
import Data1
import Data
import NTFS

def main():
    
    """ Drive Path """
    drive = r"\\.\E:"
    with open (drive,'rb') as fp:
        BOOT = NTFS.VBR()
        BOOT.ReadVBR(drive,fp)
        BOOT.PrintVBR()
        MFTAddress = BOOT.FirstClusterInMFT * BOOT.BytesPerSector * BOOT.SectorPerCluster
        MFT = NTFS.MFT()
        MFT.ReadMFT(drive,fp,MFTAddress)
        MFT.PrintMFT()
    # """ Boot Sector """
    # print ("Reading boot sector FAT32...")
    # BOOT = Data.BootSectorFAT32()
    # res = BOOT.ReadBootSector(drive) # Read Boot Sector
    # print(BOOT.PrintBootSector())
    
    # """ Address of FAT1, FAT2, RDET (Including Data part) """
    # FAT1_Address = BOOT.sectorBeforeFAT * BOOT.bytePerSector
    # FAT2_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT) * BOOT.bytePerSector    
    # RDET_Address = (BOOT.sectorBeforeFAT + BOOT.sectorPerFAT * 2) * BOOT.bytePerSector
    
    # # print(FAT1_Address)
    # # print(FAT2_Address)
    # # print(RDET_Address)
    
    # """ RDET """
    # print("Reading RDET FAT32... ")
    # RDET = Data.RDET()
    # res = RDET.ReadRDET(RDET_Address, drive)
    # RDET.PrintRDET()
    
main()