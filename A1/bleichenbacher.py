#!/usr/bin/python3
from pyroots import *
import hashlib
import sys
import base64
message = sys.argv[1]

# Exponent hard coded to 3
e = 3

# Convert message to an int
m = hashlib.sha1()
m.update(message.encode())
m.hexdigest()
m = "0001ff003021300906052b0e03021a05000414" + m.hexdigest() + "00"*217 
m_int = int(m, 16)

# Take root of message integer value (m_int)
cubed_root = integer_nthroot(m_int, e)

# Add 1 to root value
print(integer_to_base64(cubed_root[0] + 1))
