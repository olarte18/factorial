print("-----------------")
print("----FACTORIAL----")
print("-----------------")
#input
n=int(input("digite un numero: "))
#processing
c=n
n1=n
for i in range (n-1):
    c=c-1
    n=(n*c)
#output
print("El factorial de ",n1, " es ",n)