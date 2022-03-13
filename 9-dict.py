dict_01 = dict(one=1, two=2, three=3)
dict_02 = {'one': 1, 'two': 2, 'three': 3}
dict_03 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
dict_04 = dict([('two', 2), ('one', 1), ('three', 3)])
dict_05 = dict({'three': 3, 'one': 1, 'two': 2})
dict_06 = dict({'one': 1, 'three': 3}, two=2)

dict_01 == dict_02 == dict_03 == dict_04 == dict_05 == dict_06 
# => True

list(dict(one=1, two=2, three=3))# -> ['one', 'two', 'three']
len({'one': 1, 'two': 2, 'three': 3})# -> 3

dict_01 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
dict_01['two']# -> 2
dict_01['four']# -> KeyError

dict_02 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
dict_02['one'] = 'first'
dict_02['four'] = 4
dict_02# -> {'one': 'first', 'two': 2, 'three': 3, 'four': 4}

dict_03 = dict([('one', 1), ('two', 2), ('three', 3)])
del dict_03['three']
dict_03# -> {'one': 1, 'two': 2}

'one' in {'one': 1, 'two': 2, 'three': 3}# -> True
'one' not in {'one': 1, 'two': 2, 'three': 3}# -> False

iter({'one': 1, 'two': 2, 'three': 3})# -> <dict_keyiterator object at 0x1026525c0>

dict_04 = dict(one=1, two=2, three=3)
dict_04.clear()
dict_04# -> {}

dict_05 = dict({'one': 1, 'three': 3}, two=2)
dict_06 = dict_05.copy()
dict_05 == dict_06# -> True

dict_07 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
dict_07.get('two')# -> 2
dict_07.get('four')# -> None
dict_07.get('four', 0)# -> 0

{'one': 1, 'two': 2, 'three': 3}.items()# -> dict_items([('one', 1), ('two', 2), ('three', 3)])

{'one': 1, 'two': 2, 'three': 3}.keys()# -> dict_keys(['one', 'two', 'three'])

dict_08 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
dict_08.pop('one')# -> 1
dict_08.pop('four')# -> KeyError
dict_08.pop('four', 0)# -> 0

dict([('one', 1), ('two', 2), ('three', 3)]).popitem()# -> ('three', 3)

reversed({'one': 1, 'two': 2, 'three': 3})# -> <dict_reversekeyiterator object at 0x10433e4d0>

dict_09 = {'one': 1, 'two': 2, 'three': 3}
dict_09.setdefault('three')# -> 3
dict_09.setdefault('four')# -> None
dict_09.setdefault('five', 5)# -> 5
dict_09# -> {'one': 1, 'two': 2, 'three': 3, 'four': None, 'five': 4}

dict_10 = {'one': 1, 'two': 2, 'three': 3}
dict_10.update({'one': 'first', 'two': 'second', 'three': 'third', 'four': 'fourth'})
dict_10# -> {'one': 'first', 'two': 'second', 'three': 'third', 'four': 'fourth'}

dict_11 = {'one': 1, 'two': 2, 'three': 3}
dict_11.values()# -> dict_values([1, 2, 3])
dict_11.values() == dict_11.values()# -> False

{'one': 1, 'two': 2, 'three': 3} | {'three': 'third', 'four': 'fourth'}# -> {'one': 1, 'two': 2, 'three': 'third', 'four': 'fourth'}

dict_12 = {'one': 1, 'two': 2, 'three': 3}
dict_12 |= {'three': 'third', 'four': 'fourth'}
dict_12# -> {'one': 1, 'two': 2, 'three': 'third', 'four': 'fourth'}