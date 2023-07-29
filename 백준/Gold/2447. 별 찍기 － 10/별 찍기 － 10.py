def star(len):
    if len == 1:
        return ['*']
    stars = star(len//3)
    l = []

    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s + ' '*(len//3) + s)
    for s in stars:
        l.append(s*3)
    return l

n = int(input())
print('\n'.join(star(n)))