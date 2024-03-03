# write a python programm to print armstrong number in range using strings


def ams(n,m):
    for i in range(n,m+1):
        s=str(i)
        sum=0
        for j in s:
            sum+=int(j)**len(s)
            
        if str(sum) == s:
            
            
            print(i)
n,m=int(input("enter first number in the range:")),int(input("enter last number in the range:"))
ams(n,m)
