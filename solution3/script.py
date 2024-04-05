def get_function(object, key):
  if not key:
    return object
  if not isinstance(object, dict):
    return None
  keys = key.split("/")
  for key in keys:
    if key not in object:
      return None
    object = object[key]
  return object


object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
value1 = get_function(object1, key1)

object2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"
value2 = get_function(object2, key2)

object3 = {"a": {"b": {"c": "d"}}}
key3 = "a/b"
value3 = get_function(object3, key3)

object4 = {"x": {"y": {"z": "a"}}}
key4 = "x"
value4 = get_function(object4, key4)

print(value1)  
print(value2)  
print(value3)  
print(value4) 

#command python3 script.py
#Output
# d
# a
# {'c': 'd'}
# {'y': {'z': 'a'}}