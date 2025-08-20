Howdy y'all,

These are the ROM photographs of the Casio FX2500 and its clone, the
Електроника МК51.  All bits are marked, but these do not yet have
documented decoding settings in [Mask Rom
Tool](https://github.com/travisgoodspeed/maskromtool/).

See my article on page 32 of
[pocorgtfo22.pdf](https://github.com/angea/pocorgtfo/blob/master/releases/pocorgtfo22.pdf)
for details of the photography.

Tomek Malesinski has a repository on
[mk51fx2500re](https://github.com/tmalesinski/mk51fx2500re), that
includes a functioning emulator and documentation of the chip and its
instructions.
[mk51fx2500rom](https://github.com/tmalesinski/mk51fx2500rom) contains
his decoder for the ROM images.  He was the first to reverse engineer
both the bit ordering and the instruction set.

Tomek's decoder script works like this, taking the ASCII-ordered bits
and shuffling them into an array of words.  In MaskRomTool and
GatoROM, this is `-w 22 --decode-cols-downl -i`; or, 22 bits words,
cols-downl decoder with inverted bits and no rotations.

```
for i, line in enumerate(f.readlines()):
    line = line.strip()
    assert len(line) == 16 * 22, len(line)
    for r in range(16):
        code[64 * r + i] = (int(line[r::16][::-1], base=2) ^
                            ((1 << 22) - 1))
```

To produce your own decodings, first install [Mask Rom
Tool](https://github.com/travisgoodspeed/maskromtool/) to your `$PATH`
and then run `make clean all`.  You can also export the words from the
MaskRomTool GUI, producing 24-bit little endian files of the 22-bit
ROM words.

--Travis Goodspeed
