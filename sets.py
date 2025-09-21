# Set - Collection of items, unordered({1, 2} same as {2, 1}) , not indexed , mutable , no duplicates

# names_set = {'Jane', 'Faith', 'Yuan', 'Jim'}

# # print(len(name_set[1])) # no index access on sets 
# names_set.add('Tom') # sets do not maintain any insertion/removal order
# print(names_set)

set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 7, 9}

print(set1.union(set2)) # All unique elements in either set1 or set2 (or both), all duplicates removed
print(set1.intersection(set2)) # Only what the sets have in common
print(set1.difference(set2)) # Only in set1 but not in set2