# 대체로 변수명은 snake case로 쓴다
a_string = 'woogie'
a_number = 29
a_float = 73.5
a_boolean = True
a_none = None # js의 null에 가깝다
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']

print(type(a_string)) # -> <class 'str'>
print(type(a_number)) # -> <class 'int'>
print(type(a_float)) # -> <class 'float'>
print(type(a_boolean)) # -> <class 'bool'>
print(type(a_none)) # -> <class 'NoneType'>
print(type(days)) # -> <class 'list'>

print(days[3]) # -> Thur
print("Mon" in days) # -> True
print(len(days)) # -> 5

days.append('Sat')
print(days) # -> ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']