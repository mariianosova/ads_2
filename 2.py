from itertools import product

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
masti = ["пик", "треф", "бубен", "червей"]

masti.remove(input())

for elem in product(cards,masti):
    print(*elem)
