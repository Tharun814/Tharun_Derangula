
nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = {i: 0 for i in range(1, 10)}

for i in range(1, 10):
    result[i] = sum(1 for num in nums if num % i == 0)

print(result)
