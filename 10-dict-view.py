dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}

keys = dishes.keys() # -> dict_keys(['eggs', 'sausage', 'bacon', 'spam'])
values = dishes.values() # -> dict_values([2, 1, 1, 500])
items = dishes.items() # -> dict_items([('eggs', 2), ('sausage', 1), ('bacon', 1), ('spam', 500)])

reversed_keys = reversed(keys)
print(reversed_keys)

print('eggs' in keys) # -> True
print(2 in values) # -> True
print(('eggs', 2) in items) # -> True

# iteration
n = 0
for val in values:
  n += val
print(n) # -> 504


# keys and values are iterated over in the same order (insertion order)
list(keys) # -> ['eggs', 'sausage', 'bacon', 'spam']
list(values) # -> [2, 1, 1, 500]


# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
list(keys) # -> ['bacon', 'spam']


# set operations
keys & {'eggs', 'bacon', 'salad'} # -> {'eggs', 'bacon'}
keys ^ {'sausage', 'juice'} # -> {'eggs', 'juice', 'bacon', 'spam'}


# get back a read-only proxy for the original dictionary
values.mapping # -> {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}

values.mapping['spam'] # -> 500