awal = input("Input : ")
pnjg = len(awal)
print("Output : ", end="")

for a in range(0, pnjg, 1):
    for b in range(0, a, 1):
        print(awal[b], end='')
    print('')
for a in range(pnjg, 0, -1):
    for b in range(0, a):
        print(awal[b], end='')
    print('')
