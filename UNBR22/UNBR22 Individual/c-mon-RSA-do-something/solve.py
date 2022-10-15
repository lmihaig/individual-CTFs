from base64 import b64decode
import math
from Crypto.PublicKey import RSA

key1 = """-----BEGIN PUBLIC KEY-----
MDowDQYJKoZIhvcNAQEBBQADKQAwJgIgZa/m178r2GwrV61tZ0fqHk8330SkC8AO
EGFxf2uX5R8CAhV9
-----END PUBLIC KEY-----"""

key2 = """-----BEGIN PUBLIC KEY-----
MDowDQYJKoZIhvcNAQEBBQADKQAwJgIgZa/m178r2GwrV61tZ0fqHk8330SkC8AO
EGFxf2uX5R8CAhmB
-----END PUBLIC KEY-----"""

pubkey1 = RSA.importKey(key1)
pubkey2 = RSA.importKey(key2)


cd = math.gcd(pubkey1.n, pubkey2.n)
print(cd)
# 45994389161427102410734410840509040257157994451816379381112868343320621344031
