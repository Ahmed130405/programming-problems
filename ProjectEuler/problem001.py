sum = 0
for i in range(1000):
    if i % 3 | i % 5:
        sum += i
print(sum)
