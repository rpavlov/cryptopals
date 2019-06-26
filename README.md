# Cryptopals solutions

I've been meaning to 1. Learn more python, 2. Increase my understanding of cryptography and 3. Prune my backlog of 'interesting stuff to checkout someday maybe'. To that end, I'm gonna jump into the https://cryptopals.com challenges.

Accompanying blog post with concepts and notes over yonder: https://rpavlov.com/2019/06/07/cryptopals/

## Notes

### Why is XOR important in cryptography?
XOR represents the inequality function, i.e., the output is true if the inputs are not alike otherwise the output is false. A way to remember XOR is "one or the other but not both".

Imagine you have a string of binary digits 10101 and you XOR the string 10111 with it you get 00010

now your original string is encoded and the second string becomes your key if you XOR your key with your encoded string you get your original string back.

### Python sidenotes

#### Statements vs functions

In python we have statements and functions, which is a little confusing. Certain things, in this case
`assert` are functions in other languages. In python assert is a statement! Crazy!

So `assert(False, "Oh no, something is wrong)` will deceptively not trigger the error message.

`assert False, "Oh no..."` will behave as expected.

In the switch from python2->python3 this is even more confusing, because `print` went from being an expression to a function. Coming from ruby, `puts 'hey'` and `puts('hey')` behave exactly the same.

#### zip()

The zip() function in Python 3 returns an iterator. It's typically used to interleave two lists.

```
numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numbersList, numbersTuple)

# Converting to set
resultSet = set(result)
print(resultSet)

result = zip(numbersList, strList, numbersTuple)

# Converting to set
resultSet = set(result)
print(resultSet)
```

```
{(2, 'TWO'), (3, 'THREE'), (1, 'ONE')}
{(2, 'two', 'TWO'), (1, 'one', 'ONE')}
```

#### bytearray([ord(char)] * len(hex_to_byte_array(buff)))

The purpose of this line is to expand a single character to a byte string of the same length as the one we want to xor against.

### Misc notes

* Ciphertext: result of running a piece of text throught a Cipher, otherwise known as an algorithm.
* In cryptanalysis, frequency analysis (also known as counting letters) is the study of the frequency of letters or groups of letters in a ciphertext. The method is used as an aid to breaking classical ciphers.
* Summarize the example in https://en.wikipedia.org/wiki/Frequency_analysis