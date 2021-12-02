awal = int(input("input : "))
print("Output :")
a = 2

for kolom in range(1, awal+1):
    for baris in range(1, 2*awal):
        if kolom+baris == awal+1 or baris-kolom == awal-1:
            print("*", end="")
        elif kolom == awal and baris != a:
            print("*", end="")
            a = a+2
        else:
            print(end=" ")
    print()
