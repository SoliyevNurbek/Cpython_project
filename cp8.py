def x(a):
    k=0
    for i in range(2,a+1):
        if a%i==0:
            k+=1
    return "Yes" if k==1 else "No"
a=int(input())
print(x(a))