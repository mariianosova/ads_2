lines = open("alpha_oriona.csv").readlines()
data = [
    [f"{line.split(';')[0]} {line.split(';')[1]}", int(line.split(";")[2])]
    for line in lines[1:]
]

i = 0
ans = -1
ans_date = None

while i < len(data):
    cur = 1
    date = data[i][0]
    while i < len(data) - 1 and data[i][1] >= data[i + 1][1]:
        i += 1
        cur += 1
    if cur > ans:
        ans = cur
        ans_date = date
    i += 1

with open('result.txt', 'w') as file:
    file.write(f'{ans}\n')
    file.write(f'{ans_date}\n')
