import binascii
import os
try:
	flag=0
	count =0
	Dex_start =0
	size = []
	with open('core.1924','rb') as data1:
		while 1:
			raw_byte = data1.read(8)
			byte = binascii.hexlify(raw_byte)
			
			if raw_byte ==binascii.unhexlify("6465780a30333500"):
				print(byte.strip())
				flag =1
				
				data1.read(24)
				size.append(binascii.hexlify(data1.read(1)))
				size.append(binascii.hexlify(data1.read(1)))
				size.append(binascii.hexlify(data1.read(1)))
				size.append(binascii.hexlify(data1.read(1)))
				dex_size = size[3]+size[2]+size[1]+size[0]
				print(int(size[2], 16))
				dex_size2 = int(size[3], 16) *16*16*16*16*16*16+int(size[2], 16) *16*16*16*16+int(size[1], 16)*16*16 +int(size[0], 16)
				data1.read(4)
				print("dex_size "+str(dex_size))
				print("dex_size2 "+str(dex_size2))
				print("Dex_start: "+str(Dex_start))
				print(raw_byte)
				os.system("dd if=core.1924 bs=1 count="+str(dex_size2)+" skip="+str(Dex_start)+" of=/home/peter/APKdeOB_tmp/"+str(count)+".dex")
				count = count+1
				Dex_start = Dex_start +40
				size.pop()
				size.pop()
				size.pop()
				size.pop()
			elif byte:
				Dex_start = Dex_start +8
				pass
			else:
				Dex_start = Dex_start +8
				if flag ==1:
					print("Find dex header!!!")
					print(count)
				break

	

	data1.close()
except IOError:
	print('The data file is missing!!!!')
