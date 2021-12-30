print("enter the details to check the eligibilty and cost for the ride")
h=int(input("enter the height "))
a=int(input("enter the age"))
if h>120:
    print("your eligile for the ride")
    if a<12:
        print("cost per ride is $5")
    elif a>12 or a<18:
         print("cost per ride is $7")
    else:
        print("cost is $12")
else:
    print(f"not eligible{a}")
