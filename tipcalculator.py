print("welcome to tip calculator")
bill=float(input("What is the total bill"))
tip=int(input("what is the tip percentage? 10 12 14 16"))
x=int(input("how many people to split the bill"))
t=(tip/100)*bill
total=t+bill
split=float(total/x)
print(split)
