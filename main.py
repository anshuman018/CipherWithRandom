from encode import encryption
from decode import decryption

a = str(input("Enter any text: "))

ey = encryption(a)
print(f"after encryption : {ey}")

dy = decryption(ey)
print(f"after decryption : {dy}")
