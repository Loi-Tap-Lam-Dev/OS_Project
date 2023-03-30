#include<iostream>
#include<cstdlib>
#include<stdio.h>
#include<vector>
#include<windows.h>
#include<iomanip>
#include<sstream>
#include<map>
#include<string>
using namespace std;

int64_t Get_Bytes(BYTE* sector, int offset, int number)
{
    int64_t k = 0;
    memcpy(&k, sector + offset, number);
    return k;
}

int main()
{
    BYTE* MFT= new BYTE[512];
    int Entry_in4 = Get_Bytes(MFT, 0x014, 2);
    cout << "Attribute $INFORMATION Entry starts at: " << Entry_in4 << endl;
}