import sys

if len(sys.argv) < 2:
    print("Необходимо указать имя файла в качестве аргумента командной строки!")
    sys.exit(1)

file_name = sys.argv[1]

with open("example.txt", "r") as file:
    numbers = []

    for line in file:
        numbers.extend(map(int, line.split()))

corv = []
sr_num = sum(numbers) / len(numbers)
count = 0

for i in numbers:
    while True:
        if i < int(sr_num):
            i += 1
            count += 1
        if i == int(sr_num):
            corv.append(i)
            break
        if i > int(sr_num):
            i -= 1
            count += 1

print(count)

