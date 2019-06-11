import base64

# Convert hex to base64
def convert64(hex_value):
    return base64.b64encode(bytes.fromhex(hex_value))

# Fixed XOR
def xor(str1='1c0111001f010100061a024b53535009181c',
        str2='686974207468652062756c6c277320657965'):
    int1=int(str1, 16)
    int2=int(str2, 16)
    return hex(int1 ^ int2)[2:]

