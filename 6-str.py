str_triple_quote = '''첫 번째 줄
두 번째 줄
세 번째 줄'''
print(str_triple_quote) # ->
'''
첫 번째 줄
두 번째 줄
세 번째 줄
'''

str_01 = str(object='가나다')
print(str_01) # -> 가나다

str_02 = str(object=b'abc',encoding='utf8', errors='strict')
print(str_02) # -> abc
