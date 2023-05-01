for i, line in enumerate(open('data.txt')):
    if '#' in line:
        print(f"Line {i+1}: {line.split('#')[1].strip()}")