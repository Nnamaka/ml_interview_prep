import collections

dict1 = {'day1': 'mon', 'day2':'tue'}
dict2 = {'day3':'wed','day4':'thurs'}

combination = collections.ChainMap(dict1, dict2)

# print(combination.maps)

# print('Map keys = {}'.format(list(combination.keys())))
# print('Map keys = {}'.format(list(combination.values())))


# for key, val in combination.items():
#     print('{} = {}'.format(key, val))

# Find a specific value in the result
print('day3 in combination: {}'.format(('day1' in combination)))
print('day4 in combination: {}'.format(('day4' in combination)))