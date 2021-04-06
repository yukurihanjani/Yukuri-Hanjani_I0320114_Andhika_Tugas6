print("=== Soal 2 ===")

x = int(input("Masukan data : "))
print()
data = []

i = 1
while i <= x:
    nilai = int(input("Masukan nilai ke-{} :".format(i)))
    data.append(nilai)
    i += 1

rata_rata = sum(data)/x
print("\nNilai rata-rata data adalah : {}".format(rata_rata))

