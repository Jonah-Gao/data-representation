# char digit to integer value
char = input()
# also works for alphabet characters
print(ord(char) & 0xF)  # 1111 -> 15 -> F

# lower to upper case
char = input()
print(chr(ord(char) & 0x4F))  # 01001111 -> 79 -> 4F
# or alternatively
print(chr(ord(char) ^ 0x20))  # 00100000 -> 32 -> 20

# upper to lower case
char = input()
print(chr(ord(char) | 0x60))  # 01100000 -> 96 -> 60
# or alternatively
print(chr(ord(char) ^ 0x20))  # 00100000 -> 32 -> 20

# print unicode character
characters = input()
characters_list = [f"\\u{hex(ord(char))[2:].zfill(4)}" for char in characters]
print(characters_list)
for char in characters_list:
    print(char.encode().decode('unicode-escape'), end='')
