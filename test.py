a = []
for i in range(3):
    print(*a)
    a.append(int(input()))
a.insert(1, 4)
print(a)