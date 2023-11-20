def main(n:int) -> int:
    if n==0:
        return 1
    else :
        k=0
        while n>0:
            if n%10==0:
                k+=1
            elif n%10!=0:
                break
            n//=10
        return k
a=int(input())
print(main(a))
