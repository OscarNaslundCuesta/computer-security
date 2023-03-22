#!/usr/bin/env python3
import math
from Crypto.Cipher import AES


def hash_string(message):
    """ Compute the hash of message.

    if message = B1;B2;B3;...Bn and Bi are blocks of 128 bits
    computers DEC(....DEC(DEC(B1, B2), B3)...), Bn)
    where DEC is AES decryption
    """
    block = message[:16]
    # pad first block
    block = block + (" " * (16-len(block))).encode()
    for i in range(1, max(2, int(math.ceil(len(message)/16.0)))):
        # extract the i-th block
        key = message[i*16:i*16+16]
        # pad the i-th block
        key = key + (" " * (16-len(key))).encode()
        cipher = AES.new(key)
        block = cipher.decrypt(block)
    return block


if __name__ == '__main__':
    print (hash_string("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb".encode()))
    print (hash_string("bbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaa".encode()))
    print (hash_string("0123456789abcdefhello".encode()))
