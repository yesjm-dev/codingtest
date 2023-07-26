n, k = map(int, input().split())
index = 0
queue = [i for i in range(1, n+1)]
result = []
while queue:
    index += k-1
    if index >= len(queue):
        index %= len(queue)
    result.append(str(queue.pop(index)))
print('<' + ', '.join(result) + '>')