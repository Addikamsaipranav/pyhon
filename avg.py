x=int(input("enter your telugu mark\n"))
y=int(input("enter your Hindi mark\n"))
z=int(input("enter your English mark\n"))
t=int(x+y+z)
a=float(t/3)
b=int(input(("do u want to know your marks if yes please enter 1 \n do u want to know ur marks total enter 2 \n do you want to know your marks total avg if enter 3\n")))
if b==1:
    print("Marks in telugu is "+x)
    print("Marks in hindi is "+y)
    print("Marks in englis is "+z)
elif b==2:
    print("total marks is "+t)
elif b==3:
    print("avg is"+a)
    



