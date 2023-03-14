# Python program to demonstrate
# seek() method
 
 
# Opening "GfG.txt" text file
f = open("GfG.txt", "r")
 
# Second parameter is by default 0
# sets Reference point to twentieth
# index position from the beginning
f.seek(1,0)
f.seek(20,0)
f.read(1)
f.tell()
print(chr(32))
# prints current position
print(f.read(1))
f.close()