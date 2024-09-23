import json


def unicode_to_char(unicode):
    with open('unicode.json', 'r') as f:
        unicode_table = json.load(f)
    return unicode_table[unicode]


def char_to_unicode(char, base=16):
    with open('unicode_inverted.json', 'r') as f:
        unicode_table_inverted = json.load(f)
    match base:
        case 16:
            return unicode_table_inverted[char]
        case 10:
            return int(unicode_table_inverted[char][2:], 16)
        case 8:
            return oct(int(unicode_table_inverted[char][2:], 16))[2:]
        case 2:
            return bin(int(unicode_table_inverted[char][2:], 16))[2:]


char = input('char: ')
unicode = input('unicode: ').upper()

print(char_to_unicode(char, 2))
print(unicode_to_char(unicode))
