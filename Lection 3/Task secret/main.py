from hashlib import sha256
from itertools import product
import string

password = "e186022d0931afe9fe0690857e32f85e50165e7fbe0966d49609ef1981f920c6"

lowercaseAlph = string.ascii_lowercase

for variant in product (lowercaseAlph, repeat = 4):
    variant = "".join(variant)
    if password == sha256(variant.encode()).hexdigest():
        print(f"Result: {variant}")