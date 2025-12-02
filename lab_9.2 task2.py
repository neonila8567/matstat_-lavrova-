numbers = []
for с in range(3):
    n = int(input())
    numbers.append(n)
for number in numbers:
    count = 0
    for i in range(1, number + 1):
        if str(i) == str(i)[::-1]:
            count += 1
    print(count)
