

all: mk51.bin fx2500.bin mk51-tomek.bin
## Check that the files are all correct.
	md5sum -c md5.txt
clean:
	rm -f fx2500.txt mk51.txt *.bin *~

mk51.txt mk51.bin: mk51.tif mk51.tif.json
## Here we have MaskRomTool export ASCII, then have GatoROM decode it to binary.
	maskromtool -e mk51.tif -a mk51.txt
	gatorom -w 22 --decode-cols-downl -i mk51.txt -o mk51.bin

mk51-tomek.bin: mk51.txt
## Here we reproduce Tomek's decoding for comparison.
	python3 tomek.py

fx2500.txt fx2500.bin: fx2500.bmp fx2500.bmp.json
## Here we have MRT decode both to ASCII and to binary.
	maskromtool -e fx2500.bmp -a fx2500.txt -o fx2500.bin

