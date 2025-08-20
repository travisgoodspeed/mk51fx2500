#!/usr/bin/env python3

## Tomek's decoder to make program words from the bits.  He was the
## first to determine the word order and the intruction set.
## https://github.com/tmalesinski/mk51fx2500re/blob/master/program.py
code = [0] * 1024
with open("mk51.txt") as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        assert len(line) == 16 * 22, len(line)
        for r in range(16):
            code[64 * r + i] = (int(line[r::16][::-1], base=2) ^
                                ((1 << 22) - 1))

## Tomek never makes a binary, so here we export as little-endian
## 24-bit words.  This should exactly match the MaskRomTool and
## GatoRom decodings.
frame=bytearray()
with open("mk51-tomek.bin","wb") as f:
    for w in code:
        #print("%06x"%w)
        frame.append(w&0xff)
        frame.append((w>>8)&0xff)
        frame.append((w>>16)&0xff)
    f.write(frame);
    
