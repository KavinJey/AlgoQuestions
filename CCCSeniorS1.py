n = int(input().strip()) + 1
n = str(n)

while True:

    if len(n) == 4:
        if n[0] != n[1]:
            if n[1] != n[2]:
                if n[2] != n[3]:
                    if n[1] != n[3]:
                        if n[2] != n[1]:
                            if n[1] != n[3]:
                                if n[0] != n[2]:
                                    if n[0] != n[3]:
                                        print(n)
                                        break
    if len(n) == 3:
        if n[0] != n[1]:
            if n[0] != n[2]:
                if n[1] != n[2]:
                    print(n)
                    break

    if len(n) == 2:
        if n[0] != n[1]:
            print(n)

    if len(n) == 1:
        print(n)

    n = int(n)
    n += 1
    n = str(n)