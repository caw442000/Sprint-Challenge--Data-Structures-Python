import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# runtime 6.4 secs
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# binary search tree requires an initial value chose first place value in names_1 list positon[0]
bst_names = BSTNode(names_1[0])
# run time 0.127 secs
for name in names_1:
    bst_names.insert(name)

for name in names_2:
    if bst_names.contains(name):
        duplicates.append(name)

# runtime 0.00598 secs
# duplicates = set(names_1) & set(names_2)



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# runtime 0.00598 secs
# duplicates = set(names_1) & set(names_2)

# runtime 0.00499 secs
duplicates = set(names_1).intersection(names_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")