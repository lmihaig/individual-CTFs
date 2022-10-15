from pwn import *

r = remote("34.159.208.78", 32254)


def TowerOfHanoi(n, source, target, aux):
    if n == 0:
        return
    TowerOfHanoi(n-1, source, aux, target)
    text = f"Move the top disk of tower {source} to tower {target}"
    r.sendline(text)
    TowerOfHanoi(n-1, aux, target, source)


n = 3
TowerOfHanoi(n, 1, 3, 2)

TowerOfHanoi(n, 1, 3, 2)

n = 5
TowerOfHanoi(n, 1, 3, 2)

n = 7
TowerOfHanoi(n, 1, 3, 2)

r.interactive()


# INKEM63DHA3DSMBVGAYDAMJVMQ4GKNBTHE2WGMBUGU4WGMRUMM3GCNZZMFRTCZBYGI4GIZBUGE4TAZLCGQ4GEOJVHBQWCZRVG5RGIYJYGNTDO7I=
# base32
