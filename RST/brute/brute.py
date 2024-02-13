import hashlib


fin = open("cuvinte.txt", "r")
fout = open("sha.txt", "w")

def bf():
    for wordy in fin:
        wordy = wordy.rstrip()
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    word = wordy + str(a) + str(b) + str(c)
                    print(word, hashlib.sha256(word.encode()).hexdigest(), file=fout)
                    word = wordy
        print(word, flush='true')
    return 0

bf()