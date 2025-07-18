initial_num = 10
rows = 5
for i in range(rows):
    num=initial_num
    for j in range(i + 1):
        print(num, end=" ")
        num -= 2
    print()

