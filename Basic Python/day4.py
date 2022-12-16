star = [4, 2, 4, 8, 9]
for i in star:
    print('*' * i)

print("\nPrint using nested loop")
for i in star:
    out = ''
    for j in range(i):
        out += "*"
    print(out)


list = ["Liakot", "Shisir", "Shawon"]
i = 0
while i < len(list):
    print(list[i])
    i += 1
matrix = [
    ['liakot', 'rajul', 'bappy'],
    [5, 2, 7],
    [True, False, False],
    [3.53, 3.05, 3.1]
]
print("\nOutput of 2D matrix")
for i in matrix:
    out = ''
    for item in i:
        out += str(item) + " "
    print(out)