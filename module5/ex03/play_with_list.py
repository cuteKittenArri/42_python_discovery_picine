#!/usr/bin/env python3
list1 = [4, 69, 420, 69, 666]
list2 = list()
for item in list1:
        if item > 5:
                list2.append(item + 2)
dupGone = set(list2)
print(list1)
print(dupGone)
