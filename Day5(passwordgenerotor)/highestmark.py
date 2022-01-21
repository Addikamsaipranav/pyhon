stu_name = input("enter the name of the student ")
stu_marks =input("input a list of  marks scored by student ").split()
highest_mark= 0
for i in range(0,len(stu_marks)):
    stu_marks[i]= int(stu_marks[i])
for j in range(0,len(stu_marks)):
    if stu_marks[i] > highest_mark :
        highest_mark = stu_marks[i]
print("the highest mark of ",stu_name,"is ",highest_mark)        
