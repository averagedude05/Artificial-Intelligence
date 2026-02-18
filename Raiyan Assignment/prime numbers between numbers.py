start= int(input("Enter first number: "))
end= int(input("Enter second number: "))
prime=[]
for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break  
        else:
            prime.append(i)

print(prime)
    