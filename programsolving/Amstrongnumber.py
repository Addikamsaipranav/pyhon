ip= int(input("enter the number to check wheather its a amstrong number or not"))
# n is the number of digits in the entered input
str1=str(ip)
n=len(str(ip))
num = ip
result=0
for i in str1:
    x=int(i)
    result = result + x**n
if(result == ip):
    print("The number entered is amstrong number")
else:
   print("The number is not an amstrong number")




    








