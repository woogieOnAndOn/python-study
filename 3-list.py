numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
days = ['Mon', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
time_zone = ['morning', 'afternoon', 'evening', 'night']

numbers[1:3] = time_zone;
print(numbers)
# -> [0, 'morning', 'afternoon', 'evening', 'night', 3, 4, 5, 6, 7, 8, 9]

del numbers[0:5] 
print(numbers) # -> [5, 6, 7, 8, 9]

numbers.append(10)
print(numbers) # -> [5, 6, 7, 8, 9]

time_zone.clear()
print(time_zone) # -> []

days_copy = days.copy()
print(days_copy) # -> ['Mon', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

days.extend(time_zone);
print(days)
# -> ['Mon', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun', 'morning', 'afternoon', 'evening', 'night']

double_time = time_zone * 2
print(double_time)
# -> ['morning', 'afternoon', 'evening', 'night', 'morning', 'afternoon', 'evening', 'night']

numbers.insert(3, 10)
print(numbers) # -> [0, 1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

time_zone.pop()
print(time_zone) # -> ['morning', 'afternoon', 'evening']

days.remove('Mon')
print(days) # -> ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

numbers.reverse()
print(numbers) # -> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]