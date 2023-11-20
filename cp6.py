def m() -> int:
    for i in range(1000,9999+1):
        y=str(int(i))
        if int(str(y[::-1]))*4==i:
            return i
        else :
            continue
print(m())
print(2178)