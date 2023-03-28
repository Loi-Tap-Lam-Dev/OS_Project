

with open ("GfG.txt", rb) as f:
    fp.seek(2,1)
    highword = int.from_bytes(fp.read(2),byteorder='little') << 4
    fp.seek(4,1)
    lowword = int.from_bytes(fp.read(2),byteorder='little')