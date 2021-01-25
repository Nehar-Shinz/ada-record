def gcde(m,n):
    if m<n:
        (m,n)=(n,m)
    while n!=0:
        r=m%n
        m=n
        n=r
    return m
def gcdc(m,n):
    s=min(m,n)
    while s>0:
        if m%s==0 and n%s==0:
            return s
        else:
            s=s-1
print("To find gcd of two numbers")
print("Using Euclid's Algorithm")
m=int(input("Enter 1st number"))
n=int(input("Enter 2nd number"))
print(gcde(m,n))
print("Using consecutive Integer Checking Algorithm")
m1=int(input("Enter 1st number"))
n1=int(input("Enter 2nd number"))
print(gcdc(m1,n1))