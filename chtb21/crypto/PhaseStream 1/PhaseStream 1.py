string = '2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904'
string = [string[i:i+2] for i in range(0, len(string), 2)]
cipher = 'CHTB{'

key = ""

for i in range(len(cipher)):
    key += chr(int(string[i], 16)^ord(cipher[i]))
print(key)


ans = ""

for i in range(len(string)):
    ans += chr(int(string[i], 16)^ord(key[i%5]))

print(ans)
