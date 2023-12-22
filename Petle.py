x = 0
y = 200
results = []
for i in range(x, y):
    if i % 2 != 0 | i % 3 != 0 | i % 5 != 0 | i % 7 != 0:
        results.append(i)

print(results)
