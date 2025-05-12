#Using Recursion
def factorial1(a):
    if (a<1):
        return (1)
    else:
        return (a*factorial1(a-1))
z = int(input("Enter a Number:"))
ans = factorial1(z)
print("Factorial of",z,"is:",ans)