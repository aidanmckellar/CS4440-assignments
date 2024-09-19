#!/usr/bin/python3
from pyroots import *
import hashlib
import sys
import base64
message = sys.argv[1]

e= 3
m = hashlib.sha1()
m.update(message.encode())
m.hexdigest()

m = "0001ff003021300906052b0e03021a05000414" + m.hexdigest() + "00"*217 
m_int = int(m, 16)

cubed_root = integer_nthroot(m_int, e)
print(integer_to_base64(cubed_root[0] + 1))
