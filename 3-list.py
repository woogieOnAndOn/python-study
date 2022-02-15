list_empty_01 = []
print(list_empty_01) # -> []

list_empty_02 = list()
print(list_empty_02) # -> []

list_01 = list('abc')
print(list_01) # -> ['a', 'b', 'c']

list_02 = list((1, 2, 3))
print(list_02) # -> [1, 2, 3]

list_03 = [num for num in list_02]
print(list_02) # -> [1, 2, 3]