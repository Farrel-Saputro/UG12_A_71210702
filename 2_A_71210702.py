nm = []
kl = []

while (True):
    nama = input("Masukkan nama: ")
    if nama == "STOP":
        break
    kursi = int(input("Masukkan nomor kursi " + nama + ": "))

    if kursi in kl:
        print("Mohon maaf kursi tersebut telah terisi!")
    if kursi not in kl:
        nm.append(nama)
        kl.append(kursi)

print()
print("List kursi yang telah terisi : ")

for a in range(0, len(kl), 1):
    print("Kursi nomor", kl[a], "telah diisi oleh", nm[a])
