#!/usr/bin/env python3
from insecure_hash import hash_string
from Crypto.Cipher import AES

def find_collision(message):
    hashed_msg = hash_string(message) #decrypts ("hashes") the message
    cipher = AES.new(b'XXXXXXXXXXXXXXXX') #creates arbitrary key
    unhashed = cipher.encrypt(hashed_msg) #encrypts ("dehashes") the message with arbitrary key
    return unhashed + b'XXXXXXXXXXXXXXXX' #returns the collision
 
if __name__ == '__main__':
    message = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb".encode()
    print("Hash of %s is %s" % (message, hash_string(message)))
    collision = find_collision(message)
    print("Hash of %s is %s" % (collision, hash_string(collision)))
