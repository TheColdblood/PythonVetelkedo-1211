def OtodikA():
    szam1 = input("Kérem adjon meg egy számot:")
    szam2 = input("Kérem adjon meg mégegy számot:")

    if szam1 > szam2:
        for szam in range(int(szam1), int(szam2), 1):
            print(szam, end="*")
        print(szam2)
    elif szam1 < szam2:
        for szam in range(int(szam2), int(szam1), 1):
            print(szam, end="*")
        print(szam1)
    elif szam1 == szam2:
        print(szam1)