#!/usr/bin/env python3
'''TReich |  Alta3 Research
   Practicing list methods and indexing'''

# create a list of fruits
fruits = ["apple", "banana", "orange"]

# create a list of berries
berries = ["strawberries", "blueberries"]

# concatenate the two lists
print(fruits + berries)

# print fruits list
print(fruits) # notice that concatenation above does not change the original list! for that we can use append/extend...

# append fruits with berries
fruits.append(berries)
print(f"Appending fruits with berries results in an updated fruits list: {fruits}")

# In other words, append reassigns fruits to include berries, whereas concatenation (+) simply returns a copy of the combined lists

# Delete the berries sublist using .pop(), which by default deletes the last item in a list
fruits.pop()

# What is we want to insert each berry as it's own item in the fruits berry as opposed to a sublist? For that we can use extend
fruits.extend(berries)
print(f"Extending fruits with berries results in a new fruits list without a sublist: {fruits}")

# Let's return to the original fruits list and append berries as a sublist
fruits.pop()
fruits.pop()
fruits.append(berries)
print(fruits)

# The sublist berries is now at position 3 in fruits so we can index it
print(fruits[3])

# What about indexing 'strawberries' on its own? We can use chained indexing, since strawberries is position 0 of the sublist
print(fruits[3][0]) # this will return strawberries

# Note that strings can be indexed by position as well!
print(fruits[3][0][0]) # this will return only the first letter of strawberries

# In addition to lists, append and extend can also take in strings as arguments. Append will take an entire object (whether string or list) and add it to the end of the list, whereas extend will parse through the individual items of an object (string characters or list items) and insert them individually
fruits.extend("mango")
fruits.append("pineapple")

# We can index lists using negative positions as well! Position -1 will always be the last item in a list.
fruits[-1]

# The len() function counts the ITEMS in a list, so position 0 is item 1. In other words, len() will always be one more than the last position.
len(fruits)

fruits[len[fruits]-1] == fruits[-1]

# List slicing can include a start, end, AND step size parameter (default of 1)

fruits[::1] # this returns the entire list as normal

fruits[::-1] # this will REVERSE the order of the list, since we are counting backwards by a stepsize of -1

fruits[::2] # this will SKIP over every other item in the list
