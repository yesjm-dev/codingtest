n = input()
prev = '2'
count = 0
for i in n:
    if i != prev:
        prev=i
        count+=1
print(count//2)