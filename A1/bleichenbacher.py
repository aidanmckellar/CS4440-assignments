#!/usr/bin/python3
from pyroots import *
import hashlib
import sys
import base64
message = sys.argv[1]

#n= "0x00b06004b3528bfd2d187f48e6cb9f3fe79afade6cc3c428dd0577b8bb3e752824b632d100d28b396726a887c5189ded3fe9717d959730dadbf468b2bc76eea3c15091a38b61fdfa46b1510ef885ea3105ae7d7f3007e97c6761bc47e715ba32464c77f7d0cfd2c88c0f53d45404a110d6951d3f4255edc3523921237a86f35fed200c7e45870b822d7652dc896d0de064617dbb48eb9b1d47103f12911b0dab3d91e0fdb847f0b87cf2b20b19d3b951cae86cab611893f6f4cd016c68607e970fc2db800f981d9bb4441fe5d70299693a8ae51f2e9b2656f0c279bf87ecb96a753f231739eb1f9a9d7dd01f15f283dd2da2887e7fdef6aedd61c4ca7b3be1b1cd"
e= 3

#print(message)
#signature = open('sig.b64').read()
#signature = int.from_bytes(base64.b64decode(signature), byteorder="big")
#pkcs = pow(signature, e, n)
#f'{pkcs:0128x}'
m = hashlib.sha1()
m.update(b"cs4440+jdoe+1.23") #todo change from hardcode to message.encode()
m.hexdigest()
print(m)

m = "0001ff003021300906052b0e03021a05000414" + m.hexdigest() + "00"*217 
print(m)
m_int = int(m, 16)

cubed_root = integer_nthroot(m_int, e)

print(integer_to_base64(cubed_root[0] + 1))
#----------------------------------------------
# TODO: Your signature forgery code goes here!
#----------------------------------------------

#forged_sig = ""
#print(integer_to_base64(forged_sig))
