print("Enter two or more numbers separated by spaces: ")
try:
    l = list(map(float,input().split()))
    total = 0;
    total = sum(l)
    print(total)
except ValueError:
    print("Error! Enter two or more numbers and no strings")
#total = sum(l)
# total = 0
#for num in range(0,len(l)):
#    total = total + l[num]
#print(total)
