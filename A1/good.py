#!/usr/bin/env python3
# coding: latin-1
MSG = bytes(r"""


    ���`�KSB	{�H����'��~�)4����`
���������9�.�u)-�v��Bw)��`����j����̍��m4M�R��Y����)Y��g�-˂בP��zjc�|��E�aϧw�8l
""", "latin-1")
from hashlib import sha256
hexVal = sha256(MSG).hexdigest()
if hexVal[-2:] !=  '8b':
 print("Prepare to be destroyed!")
else:
 print("I come in peace")
