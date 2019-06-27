from binascii import unhexlify
import base64
import pdb

'''
Return the binary data represented by the hexadecimal string hex_str.
'''
def hex_to_byte_array(hex_str):
    return unhexlify(hex_str)

'''
Convert a hex string to base64 string
'''
def convert64(hex_value):
    return base64.b64encode(hex_to_byte_array(hex_value))

def solution1():
    given_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected_output = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    print("Result: %s", convert64(given_input))

    # Python sidenote 1
    assert convert64(given_input) == expected_output, 'Incorrect result'

'''
XOR two equal length buffers
'''
def xor(byte_str1, byte_str2):
    assert len(byte_str1) == len(byte_str2), 'Byte arrays are of different lengths!'

    try:
        #Python sidenote 2
        return bytearray([b1 ^ b2 for (b1, b2) in zip(byte_str1, byte_str2)])
    except:
        pdb.set_trace()

def solution2():
    given_input1 = hex_to_byte_array("1c0111001f010100061a024b53535009181c")
    given_input2 = hex_to_byte_array("686974207468652062756c6c277320657965")

    expected_output = hex_to_byte_array("746865206b696420646f6e277420706c6179")

    print('Result: %s', xor(given_input1, given_input2))
    assert xor(given_input1, given_input2) == expected_output, 'Incorrect result'

"""
Score a string based on letter frequency of human readable characters.
"""
def hr_score(astr):
    score = 0
    letter_freqs = {
            'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339,
            'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881,
            'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094,
            'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490,
            'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302,
            'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563,
            's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
            'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692,
            'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182}

    for char in astr:
        char = chr(char)
        if char in letter_freqs:
            score += letter_freqs[char]
        else:
            score -= .05
    return score

'''
XOR a byte array with a single character
'''
def single_char_xor(buff, char):
    #python sidenote 3
    return xor(hex_to_byte_array(buff), bytearray([ord(char)] * len(hex_to_byte_array(buff))))

"""
Returns the best element of a list, sorted by a given key.
"""
def best(l, key):
    return sorted(l, key = key, reverse=True)[0]

"""
Find the best possible single char xor decoding of a string.
https://en.wikipedia.org/wiki/Frequency_analysis
"""
def bruteforce_xor_single_char(astr):
    POSS_KEYS = ''.join([chr(i) for i in range(256)])

    results = []
    for poss_key in POSS_KEYS:
        guess = single_char_xor(astr, poss_key)

        print("Guessing... ", (hr_score(guess), poss_key, guess))

        results.append((hr_score(guess), poss_key, guess))

    return best(results, lambda result: result[0])

def solution3():
    print("Best guess: ", bruteforce_xor_single_char('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))