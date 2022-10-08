import random

listA = [random.randint(0, 100) for i in range(random.randint(5,20))]
random.shuffle(listA)

print(listA)