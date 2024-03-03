#writea python program to print the sum of n natural numbers using recursion

def printing(n):
    sum=0
    if n<1:
        return 1
    else:
        print(n)
        return n+printing(n-1)
n=int(input())
sum=printing(n)
print(sum)
