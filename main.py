import Data

def main():
    BootSectorFAT32 = Data.BootSectorFAT32()
    BootSectorFAT32.ReadBootSector(open("C:\Program Files\Adobe\Adobe Illustrator 2023\Crack\Readme.txt"))
    BootSectorFAT32.PrintBootSector()
