var = int(input("enter : "))
n1,n2 = 0,1

count = 0

if var <= 0:
    print("please, Enter a Positive integer")
elif var == 1:
    print("Sequence upto ",var)
    print(n1)
else:
    print("Sequence is ")
    while(count<var):
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count+=1

