import random
random_set = set()
while len(random_set) < 5:
    random_set.add(random.randint(10, 50))
print(random_set)