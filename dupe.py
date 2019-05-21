sample = [3, 5, 7, 6, 5, 5, 9, 3, 10]
dupe = []
sample.sort()
for i in range(0, (len(sample)-1)):
    if sample[i] == sample[i+1] and sample[i] not in dupe:
        dupe.append(sample[i])

print(dupe)