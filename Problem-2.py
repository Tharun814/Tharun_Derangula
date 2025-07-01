
a = int(input("Enter a number: "))
series = [2 * i + 1 for i in range(a)]
print(", ".join(map(str, series)))
