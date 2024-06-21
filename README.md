# CrossmapConverter
A Python tool to convert GTA 5 native crossmaps to C++ array format. 
# Usage
1. Open with Python (Made with 3.11)
2. Input where you have stored your raw crossmaps
3. Input where you want to put your formatted crossmaps
# Formatting
This tool converts crossmaps styled like:

    0x4EDE34FBADD967A6, 0x4EDE34FBADD967A6,
    0xE81651AD79516E48, 0xE81651AD79516E48,
    0xB8BA7F44DF1575E1, 0xB8BA7F44DF1575E1,

To a C++ array crossmap styled like:

    {0x4EDE34FBADD967A6, 0x4EDE34FBADD967A6},
    {0xE81651AD79516E48, 0xE81651AD79516E48},
    {0xB8BA7F44DF1575E1, 0xB8BA7F44DF1575E1},
