print("=== Soal 3 ===")

for i in range(10, 25):
    if i == 1:
        print(i, "bukan prima")
    elif i == 2:
        print(i, "adalah bilangan prima")
    else:
        for n in range(2, i):
            if i % n == 0:
                print(i, "bukan prima")
                break
        else:
            print(i, "adalah bilangan prima")