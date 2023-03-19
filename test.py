

def main():
    f = open("GfG.txt", "rb")
    # sets Reference point to tenth
    # position to the left from end
    print(int.from_bytes(f.read(20),'big'))
    f.seek(-20,1)
    print(f.tell())
    print(f.readline().decode('utf-8'))
    f.close()
    

main()