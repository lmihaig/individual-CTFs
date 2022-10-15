import string
target = "Dd|oli|QlP|ewj}~f"
# target = target[::-1]

ans = ""

scale = -4
for i in range(len(target)):
    ans += chr((ord(target[i]) ^ 15) + scale)
    scale = scale * -1

print(ans)


trial = string.ascii_letters
ans = ""
for i in range(len(target)):
    for letter in trial:
        if chr((ord(letter)-4) ^ 15) == target[i] or chr((ord(letter)+4) ^ 15) == target[i]:
            # print(chr((ord(letter)-4) ^ 15), chr((ord(letter)+4) ^ 15))
            ans += letter
            break

print(ans)
