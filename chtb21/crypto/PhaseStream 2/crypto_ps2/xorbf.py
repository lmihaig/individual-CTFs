fin = open("output.txt", "r", encoding="utf-8")
fout = open("realoutput.txt", "w", encoding="utf-8")
lines = fin.read().split()


for line in lines:
    line = [line[i:i+2] for i in range(0, len(line), 2)]
    for key in range(256):
        ans = ""
        if chr(int(line[0], 16)^key) == 'C' and chr(int(line[1], 16)^key) == 'H' and chr(int(line[2], 16)^key) == 'T':
            for i in range(len(line)):
                ans += chr(int(line[i], 16)^key)
            print(ans, file=fout)

