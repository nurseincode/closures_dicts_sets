# List - ordered (indexed) collection of items - mutable - can have duplicates
# Dictionary(dict) - collection of items, mutable, unordered, not indexed
# It is keyed: uses key/value pairs. Keys cannot have duplicates

person1 = {
    "name": "Jane",
    "last_name": "Maina",
    "age": 50
}

# print(person1)
# print(type(person1))
# # print(person1['age']) # Square brackets notation to access the keys
# print(person1.get('age')) # Alternatively use the get method 
# print(person1.get('foo', 'Key not found')) # Provide a default value if key not found

# person1['address'] = 'Melbourne' # As assigning a variable to add k-v pairs to a declared dict
person1['address'] = {'state': 'vic', 'postcode': 3000, 'city': 'Melbourne'} # The value of address is itself a dict
# person1['name'] = 'Melbourne' # Also used to update the value of existing key, now replaces  "name": "Jane"
print(person1['address']['postcode']) # Accessing postcode

print(person1)
person1.update({ 'name': 'James', 'age': 55, 'height': 180 }) # updates k-v if it exists, if not, adds
print(person1)

# Loop through the dict

# for key in person1: 
#     print(f'Key: {key}')
#     print(f'value: {person1[key]}')

# Same result using a method
for key, val in person1.items(): # k-v pairs, as enumerate on a list
    print(f'Key: {key}')
    print(f'value: {val}')