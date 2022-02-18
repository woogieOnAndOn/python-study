str_01 = 'i\'m from Korea'
print(str_01.capitalize()) # -> I'm from korea

str_02 = 'abc'
str_03 = 'ABC'
print(str_03.casefold()) # -> abc
print(str_02 == str_03) # -> False
print(str_02.casefold() == str_03.casefold()) # -> True

str_04 = 'woogie'
print(str_04.center(10, '*')) # -> **woogie**

str_05 = 'A*AA*AAA*AAAA*AAA*AA*A'
print(str_05.count('AA')) # -> 6
print(str_05.count('AA', 5, 11)) # -> 2

str_06 = '가나다'
print(str_06.encode(encoding='utf-8', errors='strict'))
# -> b'\xea\xb0\x80\xeb\x82\x98\xeb\x8b\xa4'

str_07 = '나는 직장인입니다. 지금 파이썬 공부를 하고 있습니다.'
print(str_07.endswith('니다.')) # -> True
print(str_07.endswith('니다.', 0, 14)) # -> False (나는 직장인입니다. 지금)

str_08 = '01\t012\t0123\t01234'
print(str_08.expandtabs())  # -> 01      012     0123    01234
print(str_08.expandtabs(4)) # -> 01  012 0123    01234

str_09 = 'Python'
print(str_09.find('th')) # -> 2
print(str_09.find('th', 3, 5)) # -> -1

str_10 = 'The sum of 1 + 2 is {0}'
print(str_10) # -> The sum of 1 + 2 is {0}
print(str_10.format(1+2)) # -> The sum of 1 + 2 is 3

class Default(dict):
  def _missing_(self, key):
    return key

str_11 = '{name} was born in {country}'
print(str_11.format_map(Default(name='Woogie', country='Korea')))
# -> Woogie was born in Korea
print(str_11.format_map(Default(name='Tanaka', country='Japan')))
# -> Tanaka was born in Japan

str_12 = 'Python'
print(str_09.index('th')) # -> 2
# print(str_09.index('th', 3, 5)) # -> Exception has occurred: ValueError

print(''.isalnum()) # -> False
print('abc123'.isalnum()) # -> True

print(''.isalpha()) # -> False
print('abc'.isalpha()) # -> True

print(''.isascii()) # -> True
print('woogie'.isascii()) # -> True
print('우기'.isascii()) # -> False

print(''.isdecimal()) # -> False
print('123'.isdecimal()) # -> True
print('123a'.isdecimal()) # -> False

print(''.isdigit()) # -> False
print('123'.isdigit()) # -> True
print('a123'.isdigit()) # -> False


from keyword import iskeyword
from tkinter.ttk import Separator
print('hello'.isidentifier(), iskeyword('hello')) # -> True False
print('def'.isidentifier(), iskeyword('def')) # -> True True

print(''.islower()) # -> False
print('abc'.islower()) # -> True
print('ABC'.islower()) # -> False


print(''.isnumeric()) # -> False
print('123'.isnumeric()) # -> True
print('abc'.isnumeric()) # -> False

print(''.isprintable()) # -> True
print('abc'.isprintable()) # -> True
print('abc \n 123'.isprintable()) # -> False

print(''.isspace()) # -> False
print('  '.isspace()) # -> True
print('ABC'.isspace()) # -> False

print(''.istitle()) # -> False
print('Abc'.istitle()) # -> True
print('abc'.istitle()) # -> False

print(''.isupper()) # -> False
print('Abc'.isupper()) # -> True
print('abc'.isupper()) # -> False

print(''.join(['A', 'B', 'C'])) # -> ABC

print('woogie'.ljust(10, '*')) # -> woogie****
print('woogie'.ljust(5, '*')) # -> woogie

print('AaBbCc'.lower()) # -> aabbcc

print('    spacious'.lstrip()) # -> spacious
print('www.example.com'.lstrip('cmowz.')) # -> example.com
print('ccmmoowwwzz.example.com'.lstrip('cmowz.')) # -> example.com
print('ccmmoowwwaazz.example.com'.lstrip('cmowz.')) # -> aazz.example.com

print('AAA-BBB-CCC'.partition('-')) # -> ('AAA', '-', 'BBB-CCC')
print('AAABBBCCC'.partition('-')) # -> ('AAABBBCCC', '', '')
first, separator, rest = 'AAA-BBB-CCC'.partition('-')
print(first) # -> AAA
print(separator) # -> -
print(rest) # -> BBB-CCC

print('First_line'.removeprefix('First_')) # -> line
print('First_line'.removeprefix('first_')) # -> First_line

print('First_line'.removesuffix('_line')) # -> First
print('First_line'.removesuffix('_Line')) # -> First_line

print('AAAA'.replace('A', 'B')) # -> BBBB
print('AAAA'.replace('A', 'B', 2)) # -> BBAA

print('ABCDEFG_ABCDEFG'.rfind('BCD')) # -> 9
print('ABCDEFG_ABCDEFG'.rfind('BCD', 0, 8)) # -> 1
print('ABCDEFG_ABCDEFG'.rfind('BCD', 5, 8)) # -> -1

print('ABCDEFG_ABCDEFG'.rindex('BCD')) # -> 9
print('ABCDEFG_ABCDEFG'.rindex('BCD', 0, 8)) # -> 1
# print('ABCDEFG_ABCDEFG'.rindex('BCD', 5, 8)) # -> Exception has occurred: ValueError

print('woogie'.rjust(10, '*')) # -> ****woogie
print('woogie'.rjust(5, '*')) # -> woogie

print('AAA-BBB-CCC'.rpartition('-')) # -> ('AAA-BBB', '-', 'CCC')
print('AAABBBCCC'.rpartition('-')) # -> ('', '', 'AAABBBCCC')
first, separator, rest = 'AAA-BBB-CCC'.rpartition('-')
print(first) # -> AAA-BBB
print(separator) # -> -
print(rest) # -> CCC

