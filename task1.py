B= [1, 0, 8, 0, 456, 4, 58]
new_list = []
for elem in B:
    if elem != 0:
        new_list.append(elem)
for elem in B:
    if elem == 0:
        new_list.append(elem)
print(new_list)