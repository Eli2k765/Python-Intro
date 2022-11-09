#pwntools is a CTF framework and exploit development library that makes it easy to write exploits for binary vulnerabilities.

from pwn import *

#We can generate a debruijn sequence using the cyclic function
print(cyclic(100))
print(cyclic_find(0x6161616c)) #find the offset of the cyclic pattern

#We can connect to a local process using the process function
#p = process('./vuln')
#p.recvuntil('>')
#p.sendline('A'*64)
#p.interactive()

#We can connect to a remote process using the remote function

#r = remote('10.10.10.10', 1337)
#r.recvuntil('>')
#r.sendline('A'*64)
#r.interactive()
#r.close()

#We can also use pwntools to pack and unpack data
print(p32(0xdeadbeef))
print(p64(0xdeadbeef))
print(u32(b'\xef\xbe\xad\xde'))
print(u64(b'\xef\xbe\xad\xde\x00\x00\x00\x00'))

#If we want to use pwntools to write an exploit, we can use the ELF class to load the binary
elf = ELF('./vuln')

print(hex(elf.address)) #The address of the binary in memory
print(hex(elf.entrypoint)) #The entrypoint of the binary
print(elf.symbols) #The symbols in the binary
print(elf.symbols['vuln']) #The address of the vuln function)
print(elf.got) #The global offset table
print(elf.plt) #The procedure linkage table
print(elf.search('/bin/sh')) #Search for a string in the binary
for address in elf.search('/bin/sh'):
    print(hex(address))

rop = ROP(elf) #Create a ROP chain
print(rop.dump()) #Dump the ROP chain
print(rop.search(regs=['eax'], order='regs')) #Search for gadgets that set eax
print(rop.find_gadget(['pop eax', 'ret'])) #Find a gadget that pops eax and rets

#We can also use pwntools to create a shellcode
shellcode = asm(shellcraft.sh()) #Create a shellcode
print(shellcode)
print(disasm(shellcode)) #Disassemble the shellcode

#We can also use pwntools to create a payload
payload = flat(['A'*64, elf.symbols['vuln']]) #Create a payload
print(payload)

#We can also use pwntools to create a format string
print(fmtstr_payload(4, {elf.got['puts']: elf.symbols['system']})) #Create a format string payload


