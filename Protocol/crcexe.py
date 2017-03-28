#sender function
#takes payload as argument,output is crc value of payload in bytes 

import crcmod


def crcfunc(payload):
    crc32 = crcmod.Crc(0x104c11db7, initCrc=0, xorOut=0xFFFFFFFF)
    crc32.update(payload)
    msgcrc=crc32.crcValue
    crc=bytes(str(hex(msgcrc)),'ascii')
    print('crc')    #for
    print(crc)      #verification
    return crc

#receiver function
'''crc will be obtained as a 32-bit hex value(but will be sent as a byte string)
convert it to int
received-b'0xcbf43926'
convert==> crc=int(msg.decode())
use crc function on payload and verify it with crc sent'''
