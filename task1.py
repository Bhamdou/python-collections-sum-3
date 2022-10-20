# Task - Maths with dictionary elements

'''
You're given two dictionaries. Both have the same keys `a`, `b`, `c` with their values being random numbers. You need to multiply the values with the same key value in the other dict and sum all results.
'''



dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}
result = []

if dict1.keys() == dict2.keys():
  temp = {key: dict2[key] * dict1.get(key, 0) for key in dict2.keys()}
  for val in temp.values():
    result.append(val)
  """_summary_"""
print(sum(result))