from math import fmod

def format_input(pt):
    n, d = (i.split(',') for i in (open(f'1-{pt}.txt').read().split()))
    for i in range(len(d)):
        if d[i][0] == "R":
            d[i] = int(d[i][1:])
        else:
            d[i] = int(d[i][1:]) * -1
    return n, d

names, dirs = format_input(1)
pos = 0
for i in dirs:
    pos += i
    if pos > len(names)-1:
        pos = len(names)-1
    elif pos < 0:
        pos = 0
  
print(f"Part 1 : {names[pos]}")


names, dirs = format_input(2)
print(f"Part 2 : {names[(sum(dirs) % len(names))]}")


names, dirs = format_input(3)
        
for num in dirs:
    swap = int(fmod(num, len(names)))
    names[0], names[swap] = names[swap], names[0]
    
print(f"Part 3 : {names[0]}")