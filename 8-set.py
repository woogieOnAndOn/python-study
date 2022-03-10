from copy import copy


set_01 = {'jack', 'sjoerd'}
# -> {'jack', 'sjoerd'}

set_02 = {c for c in 'abracadabra' if c not in 'abc'}
# -> {'d', 'r'}

set_03 = set()
# -> set()

set_04 = set('foobar')
# -> {'b', 'o', 'f', 'a', 'r'}

set_05 = set(['a', 'b', 'c'])
# -> {'c', 'b', 'a'}

len({1, 2, 3})
# -> 3
1 in {1, 2, 3}
# -> True
1 not in {1, 2, 3}
# -> False
{1, 2, 3}.isdisjoint({4, 5, 6})
# -> True
{1, 2, 3}.issubset({1, 2, 3})
# -> True
{1, 2, 3} <= {1, 2, 3}
# -> True
{1, 2, 3} < {4, 5, 6}
# -> False
{1, 2, 3}.issuperset({1, 2, 3})
# -> True
{1, 2, 3} >= {1, 2, 3}
# -> True
{1, 2, 3} > {1, 2, 3}
# -> False
{1, 2, 3}.union({3, 4})
# -> {1, 2, 3, 4}
{1, 2, 3} | {3, 4} | {4, 5, 6}
# -> {1, 2, 3, 4, 5, 6}
{1, 2, 3}.intersection({3, 4})
# -> {3}
{1, 2, 3} & {1, 3} & {1, 4}
# -> {1}
{1, 2, 3}.difference({3, 4})
# -> {1, 2}
{1, 2, 3} - {3, 4}
# -> {1, 2}
{1, 2, 3}.symmetric_difference({3, 4})
# -> {1, 2, 4}
{1, 2, 3} ^ {3, 4}
# -> {1, 2, 4}
copy({1, 2, 3})
# -> {1, 2, 3}

frozen_set = frozenset([1, 2, 3])
# -> frozenset({1, 2, 3})

# frozen_set.update({3, 4, 5})
'''
Exception has occurred: AttributeError
'frozenset' object has no attribute 'update'
'''

set_06 = {1, 2, 3}

set_06.update({3, 4, 5})
# -> {1, 2, 3, 4, 5}

set_06 |= {3, 4, 5} | {6, 7}
# -> {1, 2, 3, 4, 5, 6, 7}

set_07 = {1, 2, 3}

set_07.intersection_update({2, 3, 4})
# -> {2, 3}

set_07 &= {2, 3, 4} & {2, 4}
# -> {2}

set_08 = {1, 2, 3, 4, 5, 6, 7}

set_08.difference_update({2, 3, 4})
# -> {1, 5, 6, 7}

set_08 -= {2, 3, 4} | {6, 7}
# -> {1, 5}

set_09 = {1, 2, 3}

set_09.symmetric_difference_update({3, 4})
# -> {1, 2, 4}

set_09 ^= {3, 4}
# -> {1, 2, 4}

{1, 2, 3}.add(4)
# -> {1, 2, 3, 4}

{1, 2, 3}.remove(10)
# -> Exception has occurred: KeyError

{1, 2, 3}.discard(10)
# -> {1, 2, 3}

set_random = {1, 2, 3}.pop()
# -> ex) 1

{}.pop()
'''
Exception has occurred: TypeError
pop expected at least 1 argument, got 0
'''

{1, 2, 3}.clear()
# -> set()
