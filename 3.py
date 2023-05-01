cities = [[line.split()[0], int(line.split()[2])] for line in open('input.txt')]

cur = 0

data = {}

while len(cities):
    name, number = cities.pop()

    group = number // 100000 * 100
    if group not in data:
        data[group] = []
    data[group].append(name)

for key in sorted(list(data.keys())):
    print(f"{key} - {key + 100}: {', '.join(sorted(data[key]))}")