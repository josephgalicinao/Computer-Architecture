# ROM Locator
- [Gameboy ROMs](https://legal-roms.fandom.com/wiki/List_of_Game_Boy_ROMs)
- [Gameboy Advance ROMs](https://legal-roms.fandom.com/wiki/List_of_Game_Boy_Advance_ROMs)

# How to Get Conditional Jump Commands CSV
- Possible conditional jumps: ```JP```, ```JR```, ```CALL```, ```RET```
1. Run Gearboy with the ROM of your choice
2. Quit Gearboy after running the game for a while
3. Run ```python(3) jump_limiter.py disassembled3.csv```
    - disassembled3.csv will generate where the gearboy executable is (ex. ```Gearboy/platforms/linux```)
    - Edit the paths of ```jump_limiter.py``` and ```disassembled3.csv``` to where they actually are bc I probs won't update this :)

