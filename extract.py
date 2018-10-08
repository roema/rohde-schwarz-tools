#!/usr/bin/python3

import sys
import notify2


pngStart = 0x89504e470d0a1a0a
pngEnd = 0x49454E44AE426082
fsh4 = 0x46534834	#FSH4
fsh8 = 0x46534838	#FSH8
magicFound = 0
maxFileSize = 500000

i = 0

if(len(sys.argv) < 2):
	print("file needed")
	exit(0)

def sendmessage(message):
	n = notify2.Notification("R&S Converter",
			message,
			"notification-message-im"   # Icon name
			)

	n.show()
	return

notify2.init('R&S converter')

try:

	with open(sys.argv[1], "rb") as binary_file:
		while(magicFound == 0):
			binary_file.seek(i)
			bytes = binary_file.read(1)
			data = int.from_bytes(bytes, byteorder='big')
			if(data == 0x46):
				binary_file.seek(i)
				bytes = binary_file.read(4)
				data = int.from_bytes(bytes, byteorder='big')
				if(data == fsh4):
					sendmessage("found FSH-4 .set file %s"%sys.argv[1])
				if(data == fsh8):
					sendmessage("found FSH-8 .set file %s"%sys.argv[1])
			if(data == 0x89):
				binary_file.seek(i)
				bytes = binary_file.read(8)
				data = int.from_bytes(bytes, byteorder='big')
				if(data == pngStart):
					start = i
			if(data == 0x49):
				binary_file.seek(i)
				bytes = binary_file.read(8)
				data = int.from_bytes(bytes, byteorder='big')
				if(data == pngEnd):
					stop = i
					magicFound = 1
			i = i + 1
			if(magicFound):
				binary_file.seek(start)
				bytes = binary_file.read((stop+8)-start)
				filename = sys.argv[1] + ".png"
				out_file = open(filename, 'wb')
				out_file.write(bytes)
				out_file.close()
				sendmessage("png extracted")
			if(i>=maxFileSize):
				sendmessage("[-] png magic not found!")
				exit(0)

except Exception as e:
    print("[-] type error: " + str(e))
