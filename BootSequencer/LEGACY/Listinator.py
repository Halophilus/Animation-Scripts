import random

lst = []
'''
for i in range(1, 717):
    if (1 <= i <= 125) or (135 <= i <= 177) or (184 <= i <= 221) or (226 <= i <= 279) or (298 <= i <= 332) or (338 <= i <= 377) or (388 <= i <= 458) or (464 <= i <= 506) or (513 <= i <= 552) or (557 <= i <= 600) or (611 <= i <= 659) or (667 <= i <= 716):
        lst.append(random.randint(1, 5))
    else:
        lst.append(random.randint(1, 60))
'''
lst = [random.randint(1, 5) for i in range(2129)]

print(lst)
