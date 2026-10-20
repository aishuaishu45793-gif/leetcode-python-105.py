numbers = [2, 4, 3, 5, 7, 8, 1]
target = 9

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pair = tuple(sorted((numbers[i], numbers[j])))

            if pair not in pairs:
                pairs.append(pair)

print("Target:", target)
print("Pairs:", pairs)